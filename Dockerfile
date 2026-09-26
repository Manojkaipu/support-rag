# syntax=docker/dockerfile:1
# Build with the vecsearch repo as a named context:
#   docker build --build-context vecsearch=../vecsearch -t support-rag-api .
FROM python:3.12-slim AS build
RUN apt-get update && apt-get install -y --no-install-recommends build-essential cmake \
    && rm -rf /var/lib/apt/lists/*
COPY --from=vecsearch . /vecsearch
ENV CMAKE_ARGS="-DVECSEARCH_ARCH=x86-64-v3 -DVECSEARCH_BUILD_TESTS=OFF"
RUN pip wheel --no-deps -w /wheels /vecsearch
WORKDIR /src
COPY pyproject.toml ./
COPY rag rag
RUN pip wheel --no-deps -w /wheels .

FROM python:3.12-slim
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN --mount=type=bind,from=build,source=/wheels,target=/wheels \
    pip install --no-cache-dir --find-links /wheels support-rag
ENV HF_HOME=/models
RUN python -c "from sentence_transformers import SentenceTransformer; \
SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')" && chmod -R a+rX /models
WORKDIR /app
COPY eval eval
RUN useradd --uid 10001 app
USER app
ENV DATA_DIR=/data HF_HUB_OFFLINE=1
EXPOSE 8000
CMD ["uvicorn", "rag.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
