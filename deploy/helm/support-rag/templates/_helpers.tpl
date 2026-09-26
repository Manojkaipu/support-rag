{{- define "rag.labels" -}}
app.kubernetes.io/part-of: support-rag
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}

{{- define "rag.selector" -}}
app.kubernetes.io/name: {{ . }}
{{- end }}

{{/* Env shared by the API and the ingest job. $(PGPASSWORD) is expanded by the kubelet. */}}
{{- define "rag.dbEnv" -}}
- name: PGPASSWORD
  valueFrom:
    secretKeyRef: { name: postgres, key: password }
- name: DATABASE_URL
  value: postgresql+psycopg://{{ .Values.postgres.user }}:$(PGPASSWORD)@postgres:5432/{{ .Values.postgres.database }}
- name: DATA_DIR
  value: /data
{{- end }}
