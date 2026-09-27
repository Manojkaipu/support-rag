# Hand grading

For each answer, judge only from the cited conversations (and the reference answer):
- **grounded**: every factual claim is said (or fairly paraphrased) by a company agent in a cited conversation
- **correct**: it conveys the reference answer's main point (for unanswerable questions: it declined)
- **abstained**: it says the history doesn't answer the question

Record true/false for each in eval/human_grades.jsonl (the item with the same id), plus notes.

## q013

**Question:** How do I hide the Find Friends panel in the Spotify app on my Mac?

**Reference:** Click View and uncheck Right Sidebar.

**System answer:**

In 2017, Spotify support said you can hide the “Find Friends” window on the Mac app by clicking View and unchecking Right Sidebar. That was the only instruction agents gave for this in the support history, so the menu path may have changed since then.

<details><summary>cited conversation #369000</summary>

```
Customer: How do we hide this “Find Friends” window on the Mac app? I don’t use it and it’s a waste of space.
SpotifyCares: Hey Michael! You can hide that section by clicking View &gt; unchecking Right Sidebar. If there's anything else, just give us a shout /RH
Customer: SpotifyCares Thanks!
SpotifyCares: You're welcome! Stay awesome /KL
```
</details>

## q095

**Question:** Can I take my small dog in the cabin on a Ryanair flight?

**Reference:** Not covered: Ryanair isn't in the corpus. The assistant must not substitute other airlines' pet policies.

**System answer:**

Ryanair is not among the companies in this 2017 Twitter support history, so there are no Ryanair agent replies about taking a small dog in the cabin. I can’t answer from this dataset, and other airlines’ pet policies don’t apply.

_(no conversations cited)_

## q060

**Question:** A PS4 trophy I earned won't unlock even after reinstalling the game. What can I do?

**Reference:** AskPlayStation suggested using Restore Licenses to refresh your purchases.

**System answer:**

In 2017, PlayStation Support’s usual first public step when a trophy would not unlock was to sync trophies manually. One agent spelled that out as: go to Trophies, press Options, and choose Sync with PlayStation Network [#351667]. Other threads gave the same sync advice, often via a link [#616359] [#348804] [#541322] [#236580] [#300640].

In the only thread where a customer said they had already reinstalled the game and repeating the unlock still did not award the trophy, that note came after the sync suggestion. There was no further public reply from the agent after the reinstall note [#541322].

If syncing did not help, some agents next suggested Restore Licenses to refresh purchases. Only one thread stated the menu path: Settings > Account Management > Restore Licenses [#566649]. In another, the agent only linked Restore Licenses after the customer said a manual sync (game off and on) did not work; the customer never said they restored licenses [#300640].

When sync alone did not fix it, agents often moved the case off the public thread: they said they had already sent a Twitter DM [#616359], or told the customer to check DMs [#236580]. In [#236580] that came after the customer said they had already synced and had no error code. In [#616359] it came after the customer said the trophy still would not unlock following the sync advice. A similar “check your DMs” reply was given when a trophy went missing after a move from PS4 to PS4 Pro and a manual sync did not bring it back [#35200] — a different situation from a trophy that never unlocked.

In the Minecraft thread, the customer had already tried syncing (plus clearing cache and a new world). After they restored licenses and the trophies still did not pop, the agent said they had sent a DM with further instructions [#566649]. Separately, in the South Park thread, after the customer said they might not pursue the missing trophy, the agent asked them to follow PlayStation Support on Twitter and say when they had, so support could send a DM [#300640].

These replies are from PlayStation Support tweets in October–November 2017, so the steps may have changed.

<details><summary>cited conversation #351667</summary>

```
Customer: AskPlayStation who do i talk to about trophys not unlocking?
AskPlayStation: Sorry to hear that, Please try manually sync trophies. Pls Go to Trophies – Press “Options” – Sync with PlayStation Network
```
</details>

<details><summary>cited conversation #616359</summary>

```
Customer: AskPlayStation I am having an issue where I am achieving the goals of a trophy on GT Sport but the trophy will not unlock. What can I do to get it to work??
AskPlayStation: Hello Steven. Sorry to hear that. Try to manually sync your trophies by following the steps in this link: [link]
Customer: AskPlayStation I’m still having trouble unfortunately. I’m doing everything that is asked to unlock the trophies, however they still won’t unlock. Is it something that has happened on my PS4 or is there a further issue with GT Sport?
AskPlayStation: We have sent you a Direct Message via Twitter with further instructions.
```
</details>

<details><summary>cited conversation #348804</summary>

```
Customer: askplaystation PlayStation is not awarding me the fully bloated trophy for " Southpark the fractured but whole". Even though I've done it. [link]
AskPlayStation: Hi there. Let's look into that. Try to sync the trophies manually by following the steps in the link [link]
```
</details>

<details><summary>cited conversation #541322</summary>

```
Customer: Dear AskPlayStation, i spent 5 hours trying to winning 2 trophies is ffix...but when i did it...i dont get the trophies because the ps is under manteniance....what can i do to win this trophies now????
AskPlayStation: Hi Rolando. Sorry to hear that. Try to manually sync your trophies by following the steps in this link: [link]
Customer: AskPlayStation Thank for answer, but that don't work. I fix the problem with the conection with PSN, but my problem is that if a repeat the action to get the trophy, i don't get it, please help me with this (I reinstalled the game, but it did not work/I try with another game and i get a trophy)
```
</details>

<details><summary>cited conversation #236580</summary>

```
Customer: AskPlayStation hi I just finished South park on mastermind difficulty for my last trophy and I did not get my trophy please help
AskPlayStation: Hello Chris. Let's look into that. Do you see an error message or an error code?
Customer: AskPlayStation No I beat it but just no trophy and no error code or anything
AskPlayStation: Thank you for the information. Please try to sync the trophies manually, steps here: [link]
Customer: AskPlayStation I've already tried that
AskPlayStation: Totally understand. Please check your DM's for further instructions.
```
</details>

<details><summary>cited conversation #300640</summary>

```
Customer: Hey AskPlayStation I got all combat fart powers in the fractured but whole game but I didn’t get the trophy. Others have this problem. Help
AskPlayStation: Sorry to know that. Did you try to sync the trophies manually? Steps here: [link]
Customer: AskPlayStation Just tried with game off and on. Didn’t work. Any other tips?
AskPlayStation: Please try Restore Licenses to refresh your purchases: [link]
Customer: AskPlayStation Sounds more like an issue with the game than psn I’d try hitting up Ubisoft
Customer: AskPlayStation Ehh, it’s not worth the trouble over one trophy. I’ll just replay it on a harder difficulty. If it keeps me from platinum I’ll ask em
AskPlayStation: Please follow us on Twitter and let us know once you do, so we can send you a DM.
```
</details>

<details><summary>cited conversation #566649</summary>

```
Customer: AskPlayStation Hello, I am having problems with my trophies on minecraft ps4 edition. Me and my friends are all not earning them. I have tried clearing the cache, playing on a new world and syncing our trophies and none of it has worked.
AskPlayStation: That's not good. Please try Restore Licenses to refresh your purchases: [link]
Customer: AskPlayStation Sorry, Im new to playstation I don't know how to restore my licences?
AskPlayStation: Please go to Settings&gt; Account Management&gt; Restore Licenses.
Customer: AskPlayStation I just did that but the trophies still did not pop.
AskPlayStation: We have sent you a Direct Message via Twitter with further instructions.
```
</details>

<details><summary>cited conversation #35200</summary>

```
Customer: AskPlayStation Is it possible to get help with a disappearing trophy? When changing from PS4 to PS4 Pro one trophy got lost!
AskPlayStation: That's odd. Please try to sync the trophies manually. Steps here: [link]
Customer: AskPlayStation I've tried this and its still missing, please help.
AskPlayStation: Thanks for trying that. Please check your DM's for further instructions.
```
</details>

## q085

**Question:** Someone called saying they're from Safaricom and asked about my M-Pesa. How can I tell if it's really them?

**Reference:** Safaricom only contacts customers from 0722000000 (or 0729333333 during promotions). Don't share personal details with other numbers; report fraud by SMS to 333, free of charge.

**System answer:**

According to Safaricom support in 2017, you can tell by the number they call from: agents repeatedly said Safaricom only calls customers from 0722000000. If the caller is using any other number, they said it is not them.

They also told people not to share M-Pesa or other personal details with anyone purporting to be from Safaricom, not to give personal information to strangers, and not to follow instructions from other callers. In one reply they said M-Pesa money is safe if you keep your PIN secret, and that calls from numbers other than 0722000000 should not be given private information.

If you are unsure, they asked customers to text the calling number and a short description to 333 (free) so the fraud team can investigate. In one case where a customer said a caller knew their second name and claimed to be from Safaricom, the agent did not confirm the call and instead told them to text the number to 333 and beware of fraudsters. This is from late 2017 and their calling number or process may have changed since.

<details><summary>cited conversation #402335</summary>

```
Customer: Safaricom_care This number 0723915677 calling me claiming it's you. Are they for real?
Safaricom_Care: Report received. Safaricom only calls you from 0722000000. In future share such contacts via SMS to 333 at no charge. ^AB
Customer: Safaricom_Care #Safaricomboycott #Resist [link]
```
</details>

<details><summary>cited conversation #466984</summary>

```
Customer: For one more last time Safaricom_Care is our money safe in our Mpesa ACCOUNTS.
Safaricom_Care: Yes it is if you keep your mpesa pin secret. Please note that we only call our customers using 0722000000 so if you recieve...
Safaricom_Care: cont... calls from other callers do not follow any instructions given or share your private information. Report any...
Safaricom_Care: cont... attempted fraud via sms to 333. ^CK
```
</details>

<details><summary>cited conversation #252569</summary>

```
Customer: Safaricom_Care kindly blacklist the number +254 721 563424 that's trying to con people by seeking their pin numbers.
Safaricom_Care: Our official number is 0722000000. Don't give personal information to strangers or follow instructions given by strangers on(cont)
Safaricom_Care: ...phone. Please forward No. via SMS to 333 (free) for our fraud team to investigate. ^CW
```
</details>

<details><summary>cited conversation #124342</summary>

```
Customer: Safaricom_Care this no. calling me asking for m-pesa details assist if this is your customer care no.0726 600513. my number is 0728202573
Safaricom_Care: Hi, sorry for that. Please don�t share your details with anyone purporting to be from Safaricom. We have forwarded ...
Safaricom_Care: ..the number for investigation. You can also send the details in an SMS to 333 (free) for our fraud team to investigate. ^KW
```
</details>

<details><summary>cited conversation #358137</summary>

```
Customer: Safaricom_Care URGENTLY please track this no 0780 038 327 they purport to be calling on behalf of Safaricom
Safaricom_Care: We only call from 0722000000, please forward the number to 333 with a brief of the issue for investigation.^WO
Customer: Safaricom_Care I have done that already.
Safaricom_Care: Okay. All reported cases on 333 will be investigated further. ^WS
```
</details>

<details><summary>cited conversation #713477</summary>

```
Customer: Conmen calling from this number 0706 623 048 posing as Safaricom employees requiring SIM card registration details. Investigate this Safaricom_Care
Safaricom_Care: Hi, thanks for the report. Safaricom only calls from 0722000000. Forward such numbers/text to 333 at no cost in the future.^WW
```
</details>

<details><summary>cited conversation #359689</summary>

```
Customer: Safaricom_Care Please check +254728364227. Guy called me (and had my details - specifically second name) claiming to be from Safaricom.
Safaricom_Care: Kindly share the number via text to 333 (free) for our fraud team to investigate, kindly beware of fraudsters. ^ST
Customer: Safaricom_Care Thanks sent.
```
</details>

<details><summary>cited conversation #632494</summary>

```
Customer: Safaricom_Care hello? whose no. is this? 0711133110 huyu anafungia mtu line aje safaricom please?
Safaricom_Care: Hi, Kindly send fraud related issues via sms to 333(free) our fraud team will investigate and action.^ BD
Customer: Safaricom_Care ok i did so,how is her line got to be okay? since then she cant call or receive any call,help on that
Customer: Safaricom_Care poa safaricom protect ur customers against fraud,sijaelewa vipi a simple person switch off a line!! mjikaze
Safaricom_Care: All calls made from safaricom come from 0722000000. ^KL
```
</details>

## q089

**Question:** Are Marks & Spencer's pumpkin Percy Pigs vegan?

**Reference:** No. M&S said they're suitable for vegetarians but not vegans (the customer pointed to beeswax).

**System answer:**

No. In October 2017, Marks & Spencer support said their pumpkin Percy Pigs are suitable for vegetarians but not vegans [#100151]. (This is from 2017 and the recipe may have changed since.)

<details><summary>cited conversation #100151</summary>

```
Customer: marksandspencer are tour pumpkin Percy pigs accidentally vegan?
Customer: marksandspencer They're not vegan 😨 please remove the beeswax!
marksandspencer: They're suitable for vegetarians but not vegans - we'll still have other treats you can enjoy in store!
Customer: marksandspencer 💔💔💔💔
```
</details>

## q016

**Question:** Delta still hasn't found my delayed bag. Can I get reimbursed for things I buy in the meantime?

**Reference:** Yes. Delta said you can use the delayed-bag file you created to be reimbursed for purchases made while waiting for the bag.

**System answer:**

Yes. In 2017, Delta’s agents told customers whose bags were still delayed that they could seek reimbursement for things they bought while waiting.

Agents described this as reimbursement for “purchases while waiting,” “items re-purchased,” “interim expenses,” or “out of pocket expenses” due to the bag delay. Customers who raised clothes, toiletries, or a swimsuit were pointed to that same process. To claim, agents said to use the delayed-bag file you already opened, or a baggage claim form / the reimbursement link they provided, and to submit receipts and any supporting documentation.

It is not an automatic payout. When a customer said airport staff had refused reimbursement for any expenses while the bag was still delayed and they still needed to buy clothes, the Twitter agent did not confirm that refusal; they directed the customer to submit receipts and supporting documentation “for reimbursement consideration.” When asked for the exact policy, an agent pointed to a link rather than stating dollar limits or item rules in the tweet, so those details are not in this history.

After you file, agents said processing can take about 4–6 weeks, or 30–45 days for a response, and that you should get a notification on the claim. This is what Delta support said in October–December 2017 and may have changed since.

<details><summary>cited conversation #246100</summary>

```
Customer: Delta "... due to extreme weather events, you can expect to receive substantive response from our office w/in 30 days." THIS DOESNT CUT IT
Delta: I'm sorry that your bag has been delayed for so long. So far, there's no new info on the bag, but we're working hard to find it &amp; get... 1/3
Delta: ...the bag's arrival. *HWG 3/3
Delta: ...it back to you quickly. In the meantime, you can use the file you created to be reimbursed for your purchases while waiting on... 2/3
```
</details>

<details><summary>cited conversation #342522</summary>

```
Delta: Mary, I apologize for your bag delay. Please click this link for any reimbursement for items re-purchased. [link] *TAC
Customer: Delta Thanks, don't need to purchase clothes. Due miles / refund for Delta leaving my bag in PHX. I was told to contact cust service. Pls advise.
```
</details>

<details><summary>cited conversation #524502</summary>

```
Customer: Delta What exactly is your policy for reimbursing expenses incurred when baggage is delayed for several days?
Delta: Hi James, I apologize for the baggage delay. The following link will explain our expense reimbursement policy along with a baggage claim form for receipt of your request. Thank you. *TMB
```
</details>

<details><summary>cited conversation #797604</summary>

```
Customer: Delta wish I knew where my 3 bags are. Agent promised update hours ago. Wondering how much I’ll have to spend on clothes&amp;toiletries before meetings...what’s platinum for??
Delta: Your frustrations are understood, Matthew. Please be assured that our Baggage team is working diligently to reunite you with your bags asap. You can apply for expense reimbursement due to to the delay of your bags. *TCH
```
</details>

<details><summary>cited conversation #803144</summary>

```
Customer: Hey Delta you left our car seat &amp; luggage in EWR now we r in OKC. What 2 do till luggage arrives? Will you reimbrse xpnses. Agnts say no!
Delta: I am sorry to hear that, Jason. Please reach out to the Baggage Service Office at the Airport for further assistance. *AFM
Customer: Delta I did and they located bag which will only get here earliest by 3pm tom, but also said I couldn't get reimbursed for any expenses.
Customer: Delta how is that right? We have an event tomorrow at 1pm and now need to buy clothes.
Delta: Again, my apologies. For reimbursement consideration of your out of pocket expenses, please provide receipts and any supporting documentation using the link provided. Start the process by selecting Voice a Complaint under Category and After Trip under Subcategory.... 1/2
Delta: ...[link] *AFM 2/2
Customer: Delta plus we don't even have proper car seat for our child.
```
</details>

<details><summary>cited conversation #149584</summary>

```
Customer: Delta "mishandled" my wife's luggage on our connecting flight to Cancun! First day of vacation with nothing but the clothes on her back.
Delta: Hi Brain, I'm sorry to hear your wife did not receive her bag. If she needs assistance, pls DM her file #. *TJW [link]
Customer: Delta I paid $50 for checked baggage and another $50 for a "lost" bathing suit when we arrived in Cancun. Money wasted.
Delta: Hi Brian, I'm very sorry to hear you had delayed baggage on your arrival in Cancun. 1/2 *TJW
Delta: Pls use the attached form to submit receipts for reimbursement for interim expenses. 2/2 [link] *TJW
Customer: Delta My reference number is no longer valid. #CUNDL47212 I have my bag but I would like to claim for checked bag fee and cost of new swimsuit.
Delta: Brian, I am sorry about that, try using this page instead for post travel.[link] *TBW
```
</details>

<details><summary>cited conversation #339611</summary>

```
Customer: delta, you lost my bag and you don't have any representatives at the SeaTac international arrivals baggage claim! What gives?
Delta: Oh no, Peter. Have you filed a Lost Bag Report? If not, please file one here. [link] *ACJ
Customer: Delta Yep! Only problem is that all my toiletries are in there, and I have work tomorrow. What are my options?
Delta: Peter, I regret the inconvenience this has caused you. Here is a link to the reimbursement process.[link] *TLT
```
</details>

<details><summary>cited conversation #166354</summary>

```
Customer: sent you a complaint about lost baggage claim, days past, and no response whatsoever...
Delta: Kristy, I'm very sorry for the delay in response to your baggage claim. Reimbursement for interim expenses can take 4-6 wks to process. *TJW
```
</details>

<details><summary>cited conversation #665688</summary>

```
Customer: Delta where can I find the updated details of my delayed baggage expense claim? If the receipts were accepted?
Delta: Hi Jessie, once you submit receipts for reimbursement, it can take 30-45 days for a response regarding your claim. *TJW
Customer: Delta Ok thank you! Will I be notified?
Delta: You are welcome, Jessie. You will receive a notification of your claim. *AJL
```
</details>

## q070

**Question:** I bought a product at Sainsbury's that turned out to be bad. How do I get a refund?

**Reference:** Sainsbury's either asks you to take it back to the store with your receipt for an exchange or refund, or asks which store it was from (and sometimes for a barcode photo) and then for your Nectar card number by DM so they can add the refund, sometimes with extra, as points.

**System answer:**

For a product bought in a Sainsbury’s store that was poor quality or faulty, 2017 agents’ advice depended on whether you still had proof of purchase.

With the receipt, they said to return the item to the store for a refund or exchange. [#160720] [#61657]

If you no longer had the receipt, other proof was accepted:
- Take the card you paid with and the product back into the store so they can get a duplicate receipt. One agent said to advise them the product is faulty so they can resolve it. [#721776]
- A bank statement can be used as proof of purchase if it shows the product price or higher; the store can then track the transaction and see what was bought. [#748771] Another agent said a bank or Nectar statement showing the transaction is enough, and to return to the same store you bought it from. [#61657] If you paid by debit or credit card, or swiped a Nectar card, one agent said any of those statements can be used as proof, and that a larger shop is fine as long as the total spend on the card is more than the cost of the item. Take it to customer service colleagues and advise them it is faulty. [#648231]
- A Nectar card number can be used by colleagues to find a copy of the receipt from the last 3 months. [#544979] A Nectar statement was also described as alternative proof of purchase; take that and the item to customer service and say it is faulty. [#809745]

Without any proof of purchase, a refund or exchange was at the store’s discretion. [#544979]

One agent, answering about a record player bought the day before whose sound was awful, said you can take it back for a refund or exchange only if it is still in a resellable condition. [#629001] Other replies did not all use that wording; several only said to bring the item back with a receipt or other proof.

For food that had gone mouldy or off, Twitter agents asked which store it came from and then offered a refund if the customer DM’d their Nectar card number. [#448523] [#108013] [#547578] Only one of those also asked for a photo of the barcode, and only that thread said they would put a full refund on the Nectar balance along with some goodwill. [#547578] In a separate case, after asking for the barcode and store, an agent offered to add points if the customer DM’d their Nectar number. [#270439]

For an online grocery order (for example cracked eggs or bruised bananas), they asked the customer to DM the order number, account holder’s name, postcode and email so they could look into a refund. [#202984]

This is what Sainsbury’s support said in October–December 2017, so the process may have changed since.

<details><summary>cited conversation #160720</summary>

```
Customer: sainsburys I bought a sound bar for my TV from your Ely store yesterday. The sound from it is awful. Can I get a refund?
sainsburys: Hi there, do you still have the receipt for this product? Robbie
Customer: sainsburys Hi Robbie Yes I do. Regards Nigel
Customer: sainsburys Sorry, I know you're busy. Is it a yes or no?
Customer: sainsburys Pity no-one saw this through to a conclusion
sainsburys: I'm sorry about the late reply, we have been very busy! If you return to the store with your receipt you will be able to get a refund. Gabby
```
</details>

<details><summary>cited conversation #61657</summary>

```
Customer: sainsburys Dog bed falling to bits! Very disappointed. Can we ask for replacement? [link]
sainsburys: Oh no, I'm sorry about that. Can you send me the product code for this please? This should be on the label. Aisha
Customer: sainsburys [link]
sainsburys: Thanks, sadly the code is not there. Are you able to confirm the product from our website - [link] Goldie
Customer: sainsburys Item code: 7530782
sainsburys: Hi there, if you return the bed to store with your receipt my colleagues will sort you out with an exchange/refund. Liz
Customer: sainsburys Receipt gone......
sainsburys: ...your proof of purchase. All you need to do it return to same store you purchased from. Aisha 2/2
sainsburys: Did you pay by card or use a Nectar card for this? As you can use a bank or Nectar statement showing transaction as...1/2
```
</details>

<details><summary>cited conversation #721776</summary>

```
Customer: sainsburys I bought one of your Apple chargers and, I don’t mean to beat about the bush, but, it is completely useless, it is unable to charge my phone which was one of the main reasons I bought it, I will not be able to see your reply Tommorow, as my phone will be dead, cheers.
sainsburys: Sorry about this Sam, do you still have the receipt for it? What store did you get it from? Maclaine
Customer: sainsburys I don’t no
Customer: sainsburys And Weymouth
sainsburys: Thanks Sam. Can you confirm when you bought the charger and did you pay by card/cash? Thanks Guzala
Customer: sainsburys I think 19th October, and I paid by card (contactless, Apple Pay)
sainsburys: That's great. If you take your card and the product back into store, they will be able to get a duplicate receipt of your transaction. If you advise them the product is faulty, they will be able to resolve this for you...1/2
sainsburys: ... Hope this helps. Guzala 1/2
```
</details>

<details><summary>cited conversation #748771</summary>

```
Customer: sainsburys can I get a refund on something if I don't have the receipt but have used my bank card? x
sainsburys: Hi there, of course Rosie. As long as the bank statement shows the product price or higher then this can be used as proof of purchase. Robbie
Customer: sainsburys Thank you. I did buy some other bits at the same time is this ok still? x
sainsburys: The store can track the transaction and see what was purchased. Hope this helps! Ewan
Customer: sainsburys Yes thank you x
```
</details>

<details><summary>cited conversation #648231</summary>

```
Customer: Pretty sure this isn’t meant to happen is it sainsburys ? Only had it just over a month and used it 4 times? [link]
sainsburys: Hi there, sorry about that. We'd definitely expect more from our products. Can you confirm the store you bought this from? Robbie
Customer: sainsburys Cobham, Surrey but I don’t have the receipt any more
Customer: sainsburys Hi, is there a reason why you asked where I bought it from? Is there anything I can do?
Customer: sainsburys I'd find it odd to be asked which specific store you bought a product from, I didn't realise specific stores received the defective goods 🙄 perhaps if we knew which stores to be "safe" to buy from, people would shop there more often? 🤔
sainsburys: Did you use a debit/credit card to purchase this or swipe your Nectar card? Any of these statements can be used as proof of purchase. You can take this with the item back to the store. Thanks, Karen
Customer: sainsburys Thanks, I bought it as part of a larger shop so my debit card receipt won’t have that individual item.
sainsburys: That's okay. As long as the total spend on your card is more than the cost of the item you're returning. You can take this to our customer service colleagues and advise this is faulty. Thanks, Karen
Customer: sainsburys Thank you
```
</details>

<details><summary>cited conversation #544979</summary>

```
Customer: sainsburys - just tried taking a faulty low energy projector bulb back to your Sittingbourne store; it only lasted a couple of weeks. Apparently you don’t swap faulty goods without the packaging or a receipt. It’s got Sainsbury’s stamped on it?! #saleofgoods #confused
sainsburys: Sorry about this, without a proof of purchase a refund or exchange of the item would be at the store's discretion. Did you pay by card or swipe a Nectar card when getting it? Maclaine
Customer: sainsburys - Hi Maclaine, thanks for the response. Paid cash but almost certainly swiped the Nectar card.
sainsburys: How long ago did you pick it up? Using your Nectar card number our colleagues can find a copy of your receipt within the last 3 months. Maclaine
Customer: sainsburys - only a few weeks. Good to know that; it’s just a shame your colleagues in-store didn’t seem to know/want to do this.
sainsburys: Do you still have the barcode for the product? If so, can you please send me a photo of this? Thanks, Gabby
Customer: sainsburys - no problem. Here’s the barcode from an identical pack - [link]
sainsburys: Thanks, could you DM me on the below link your Nectar card number please? I'd like to feed this back and also pop a full refund onto your balance. Mariya [link]
```
</details>

<details><summary>cited conversation #809745</summary>

```
Customer: But if a complicated one sainsburys Bought a tin opener from you (£3) about a month ago. Didn’t work. Thought maybe I dishwasherd it and messed it up. Fair enough. Bought another one last week (also £3) didn’t dishwasher - also doesn’t work :( I shop near daily so don’t keep
Customer: sainsburys My receipts, and not 100% which day it will have been, but will show up on my nectar card. Would I be able to bring it in (only have most recent - threw other away) and exchange for the slightly more expensive one? (I’ll pay the difference) I just don’t have proof of purchase.
sainsburys: Hi there. I'm sorry you've had issues with the tin opener. You can use your Nectar statement as an alternative proof of purchase. If you take...1/2
sainsburys: ...this to our store with the tin opener and advise our customer service colleagues that this is faulty, they can help. Thanks, Karen 2/2
```
</details>

<details><summary>cited conversation #629001</summary>

```
Customer: sainsburys Hello. Recently bought a portable record player in store. The quality of it is awful plus terrible sound... not happy at all. Have my receipt and only purchased one day ago. Can I return this for a full refund?
sainsburys: Hi Jonathan, you can take it back to the store for a refund/exchange as long as it's in a resellable condition. Faiza.
```
</details>

<details><summary>cited conversation #448523</summary>

```
Customer: sainsburys no out of date yet and gone mouldy and horrible 😩 [link]
sainsburys: Sorry Shannon, can you tell us what store you bought these in? Rob
Customer: sainsburys Harpenden
sainsburys: Thank you, if you DM me your Nectar card number via this link I can get a refund added for you and make sure this is fed back. Robbie [link]
```
</details>

<details><summary>cited conversation #108013</summary>

```
Customer: sainsburys what's going on with your fruit at the moment? Woke up to take these to work, but I can't now... mouldy and rotten [link]
sainsburys: Hi Greg, I'm really sorry about this, it's certainly not up to our usual quality. What store did you buy them in? Angie
Customer: sainsburys Sainsbury's Chiswick.
sainsburys: Thanks Greg. If you DM us your Nectar card number on the below link I'd be happy to arrange a refund for you. Sam. [link]
```
</details>

<details><summary>cited conversation #547578</summary>

```
Customer: sainsburys have you changed supplier of sweet potato 3 weeks out of 4 sweet potatoes gone mouldy well before best before date? New record bought 11/11 mould on 12/11 best before 16/11? [link]
sainsburys: Hi there, I'm very sorry about this Craig. We'd definitely expect more from our products. Can you send me a pic of the barcode please? Which store did you buy these from? Robbie
Customer: sainsburys Also sending one of previous barcodes [link]
sainsburys: Is it always the same store these are from? Have you spoken to the Store Manager about this? Thanks, Karen
Customer: sainsburys Yes always same store and no I haven't. That is why I have contacted you on twitter
Customer: sainsburys In addition the Spinach bought same day when opened was slimey and off.its not acceptable [link]
Customer: sainsburys That is 3 packs of sweet potato and a pack of Spinach all not fit for consumption whilst been within their best before dates. I expect more for the price I pay. Not good enough
sainsburys: I completely understand the frustration. Could you DM me on the below link your Nectar card number please? I'd like to feed this back and pop a full refund onto your balance along with some goodwill. Mariya [link]
```
</details>

<details><summary>cited conversation #270439</summary>

```
Customer: I give up with sainsburys I'm always getting mouldy food from them. Bought yesterday, forgot to eat them, opened today and they've gone off [link]
sainsburys: Sorry Louise, that's not the quality we expect from our products. Can you send us the barcode? What store did you buy these in? Rob
Customer: sainsburys I've thrown them in the bin now, but they were from Stroud superstore.
sainsburys: No worries, can you confirm if this is the correct product via the link, [link] Aisha
Customer: sainsburys Yeah that's the product
sainsburys: Thanks! I'll get this logged, and if you DM your Nectar card number via the link I'll pop on some points for you. Dan [link]
```
</details>

<details><summary>cited conversation #202984</summary>

```
Customer: sainsburys how do I get a refund for certain items on an online order? Eggs cracked 🥚 and bananas bruised 🍌
sainsburys: Sorry Steph, can you DM your order number, account holder's name, postcode &amp; email address for security using the below link? I'll look..1/2 [link]
sainsburys: ... into this for you. Steven 2/2 [link]
```
</details>

## q076

**Question:** I've already used most of my O2 data a week into the month. How can I work out why?

**Reference:** O2 suggested checking your remaining balance on My O2, whether Wi-Fi Assist is turned on, and which apps use the most data.

**System answer:**

O2’s agents in these late-2017 chats said they cannot see what the data was used on. Usage is taken directly from the SIM and they treat that figure as correct, so they can’t itemise it for you ([#102796], [#174871], [#439724]).

What they told people who had burned through data early to do themselves:

- **Check the phone’s data settings.** On an iPhone: Settings → Mobile Data, then scroll down to see which apps have used the most data ([#102796], [#615416], [#544252]).
- **Check the allowance on My O2.** One agent asked whether the usage showed on My O2 and said usage is taken directly from the SIM, so it would be correct ([#174871]). Another said to use My O2 rather than the phone’s own settings for usage info ([#795408]). A separate reply said the figure from the SIM is right and the phone’s own counter isn’t accurate, without naming My O2 ([#103968]).
- **Wi-Fi Assist.** Agents asked whether it was turned on ([#140361], [#391252], [#439724]). One said it is at the bottom of Mobile Data settings ([#439724]), and one told a customer to switch it off ([#615416]). They did not explain in these chats how it uses data.
- **Background apps.** One agent asked whether apps had been running in the background ([#615416]).
- **Software updates.** An agent asked whether any updates had been done that month ([#391252]). Another asked if the phone was on the latest software and said that can affect data usage on the device ([#544252]).
- **Anything else new.** One agent asked if it was the first time this had happened, whether any new services were in use, and whether the phone was on Wi-Fi where possible ([#439724]).

If the allowance ran down very quickly, they also said the usual 80% warning text might not have been sent, and to keep an eye on My O2 rather than waiting for that text ([#323142]).

They often pointed people at a data-usage or data-saving guide (the links are no longer in these tweets) and, if it happens often, at adding a bolt-on or raising the monthly allowance in My O2 ([#102796], [#503064], [#563925]).

This is what O2 support said in October–December 2017, so menu names and My O2 may have changed since.

<details><summary>cited conversation #102796</summary>

```
Customer: O2 how is it I’ve managed to use almost all my 10gb data allowance in 5 days when I never usually use close to 4gb in a month?! 🙃🙃
O2: 😢 We're unable to confirm where the data has been used. Check out our data saving tips here: [link]
O2: If you're looking to add a data bolt on, you can check out your options here: [link]
Customer: O2 Data saving tips isn’t going to help when it’s all been used up and on top of a usual £55 bill I now have to buy more data. Rip off!!
O2: Which phone do you have? We'd recommend checking your phone settings, to see what's using the most data.
Customer: O2 Could you check your dm please O2
Customer: O2 iPhone 7 Plus
O2: Okay. Go to Settings, Mobile Data then scroll down to see what's using the most data.
Customer: O2 I have already done that. I’ve switched off data for every app I do no use. What I want to know is how 10GB has disappeared in 5 days
O2: Data usage is taken direct from the SIM card and will be correct, however we're not able to see what it's been used on.
```
</details>

<details><summary>cited conversation #174871</summary>

```
Customer: O2 Hi. Please help. Find it difficult to believe I've wiped 4GB of data in half an hour [link]
O2: Does it show on My O2 that you've used the data: [link] Usage is taken directly from your SIM so it would be correct.
```
</details>

<details><summary>cited conversation #439724</summary>

```
Customer: O2 this cant be possible, no way have i used up that much data in a few days [link]
O2: 🙁 Is this the first time this has happened? Are you using any new services at all? Do you connect to Wifi where possible?
Customer: O2 yes first time, no new services and yes always connect to wifi and have wifi at home so this much data shouldnt be used up
O2: What phone are you using? Have you checked the data usage settings? Check out these tips [link]
Customer: O2 an iphone and yes it says the same [link]
O2: 🤔 Do you have WiFi assist turned on? DM us here if you prefer: [link]
Customer: O2 Not sure what you mean? [link]
O2: If you scroll down to the bottom of your mobile data settings there's an option for WiFi assist.
Customer: O2 it is off [link]
O2: Okay, the data comes directly from the Sim so will be correct. If you need to add more data check here [link]
```
</details>

<details><summary>cited conversation #615416</summary>

```
Customer: My phone had 900mb of data a couple of hours ago and now I’ve only got 100mb?! What the hell O2 ?! 😡😡
O2: Hi Daniella, 😕 Have you had any apps running in the background? What phone do you have? This link should help with understanding your data usage [link]
Customer: O2 iPhone and this has never happened before! Not happy!
O2: If you go to Settings - Mobile Data and scroll down you'll be able to see which apps are using the most data. Also make sure Wi-Fi Assist is switched off.
```
</details>

<details><summary>cited conversation #544252</summary>

```
Customer: Might have to change network data on O2 has doubled but done nothing different
O2: 😔 Hi Charlie, thanks for taking the time to raise this with us. Have you checked out our handy data saving tips? [link] Is your phone on the latest software version? This can affect the data usage on the device. Let us know 👍
Customer: O2 It was after a software update 2 months ago that my battery started playing up and data usage increased
O2: Ah right, have you tried a full back-up and restore of the device to help with the battery issue? Data usage is pulled directly from the SIM, so it would be correct.
Customer: O2 But why has data use doubled when I am not doing anything different. I used to use up to 10gb and suddenly I am struggling to stay under 20gb. FB email and stagecoach and merseyrail app shouldn’t use that much
O2: Have you checked your phone settings to see what's using the most data?
Customer: O2 Do you have a guide on how to do that
O2: Go to settings, mobile data &amp; scroll down. You'll be able to see what apps are using the most data.
```
</details>

<details><summary>cited conversation #795408</summary>

```
Customer: O2 I pay for 5Gb of data a month. You tell me I’ve used 80% this month but my phone says just under 60%. Why the difference? [link]
O2: Hey Andrew 👎 Check here: [link] for accurate info on your data usage. We'd always recommend using My O2, rather than your phone settings. Do you run out of data often? Check here: [link] for some tips
```
</details>

<details><summary>cited conversation #103968</summary>

```
Customer: Okay so my data plan on O2 is for 10gb. I've used 7gb according to my phone which tracks it. According to O2 I've ran out of data though..
O2: ☹ Usage comes from the SIM, so it's right. The counter on the phone isn't accurate. Try these tips: [link]
```
</details>

<details><summary>cited conversation #140361</summary>

```
Customer: When you've used 80% of your data &amp; you only got it last week. How?!? O2 help me out here! [link]
O2: Have you looked at your remaining balance on My O2? [link] Have you got Wi-Fi assist turned on in the background?
Customer: O2 I have indeed. For what I pay I get minimal data
O2: Have you checked your settings to see what apps are using data up the most? Do you run out of data often? Please DM us more info. [link]
```
</details>

<details><summary>cited conversation #391252</summary>

```
Customer: O2 can you tell me why my data has ran out yet my average usage is only 1.6 gb a month?? I’ve not used it anymore this month than normal?? [link]
O2: Hi Karen, 😕 Have you checked your phone settings to see where the data is being used? Have you done any updates this month?
Customer: O2 I did the IOS update. Could it have been that although I did the update when I was on WiFi? Really frustrating as I haven’t ran out before
O2: Do you have Wi-Fi assist turned on? Check out these data saving tips: [link]
```
</details>

<details><summary>cited conversation #323142</summary>

```
Customer: SO annoyed that I got a text this morning to tell me that I had used up all of my data when I didn't even receive an 80% text O2
O2: 😞 If your data was used quickly, we may have been unable to send the 80% text. Keep updated via My O2: [link]
Customer: O2 I have My O2 installed. When I checked on Friday I had 2.31GB out of 3GB and don't understand how I could have used this amount in 48 hours
O2: Do you keep an eye on your settings to see where it's being used? Do you run out often? Have you looked to change your tariff?
Customer: O2 Yes I do. No, I hardly run out of data. I have just recently changed tariff to give me more data.
O2: Ah, okay. Does it show what's using the most data? Check here: [link] for some data saving tips.
O2: Ah, okay. Does it show what's using the most data? Check here: [link] for some data saving tips.
```
</details>

<details><summary>cited conversation #503064</summary>

```
Customer: Topped up my O2 data last nite at home, been out this morning and it’s all gone!! How!! I’ve barely used the phone and I’ve had to turn most of my apps off. That’s £25 extra this month in data &amp; I have no idea why 🙀
O2: 😮 Hi Collette, are you able to see what's using your data using the phones settings? Are you running out of data frequently? If so, you can increase your monthly allowance on My O2: [link] Check out our data tips here: [link] 👍
Customer: O2 I’ve never had a problem like this my data allowance has always been enough so I don’t understand why it changed this month all of a sudden
O2: Ah, okay. Just to clarify, have you checked into your settings to see what's used up your data? What phone are you using? Drop us a DM ✉ [link]
```
</details>

<details><summary>cited conversation #563925</summary>

```
Customer: How come my data usage has shot up from 6 – 9GB a month to 16GB this month? I’m still using WIFI at home and at work and I don’t download anything while I’m out… my usage is pretty much the same as it’s always been. O2
O2: 😕 Hi Andrew. Have you checked your phone settings to see what's using the most data? Take a look at our data usage guide on the link here: [link] We hope it helps.
Customer: O2 My phone settings tells me that in 13 months I’ve used on average ~9GB a month, at a total of 112GB since 2nd Oct 2016. I can see my last 6 months usage on My O2, but I can’t see the 6 months before that to compare the reported usage from my phone and what my settings say 🙁
O2: We'd advise to check the settings of your phone to see which apps use the most data, this way you can change the way you use the phone if you're looking to save data. Let us know how you get on.
```
</details>

## q005

**Question:** After updating to iOS 11 the Phone app on my iPhone only shows a blank screen. What should I try?

**Reference:** AppleSupport suggested force-closing the Phone app, restarting the iPhone and opening it again. When that didn't work they asked whether it started with the update and recommended making a current iCloud or iTunes backup before further steps.

**System answer:**

In 2017, Apple Support’s public steps for a Phone app problem after an iOS update were: force-close the Phone app, restart the iPhone, and open the app again. If that didn’t fix it, they asked for a current iCloud or iTunes backup before any further steps, and recommended making one if there wasn’t one. They also asked whether a reset had been Settings > General > Reset > “Reset All Settings” or “Erase All Content and Settings,” and whether a computer with iTunes was available, then continued in DM rather than giving more steps publicly [#767041].

In another Phone app thread, they asked which iOS version was installed, whether it was the only app affected, and whether the iPhone had already been turned off and back on [#525263].

This is from late 2017 and may not match current troubleshooting.

<details><summary>cited conversation #767041</summary>

```
Customer: AppleSupport Since upgrading to iOS 11.1.2 my phone app won’t work? Tried resets and nothing. Any other ideas? Having to use Siri to make calls and get VM.
AppleSupport: We'll be happy to assist with this. When you try to use the Phone app, does it simply exit directly to the home screen?
Customer: AppleSupport No, it just opens to a blank screen. The icon still tells me I have VM or missed calls. [link]
AppleSupport: Have you forced the Phone app to closed, restarted your iPhone, and tried to open it again? Let's start off by doing that: [link]
Customer: AppleSupport Several times
AppleSupport: Did this issue happen on this current iOS or did you notice it before you updated?
Customer: AppleSupport Noticed it after updating to iOS 11
AppleSupport: Do you have a current backup of your iPhone in iCloud or iTunes? If not, we recommend completing one now before our next steps: [link]
Customer: AppleSupport Yes, I already completely reset my phone and it didn’t correct the problem if that was your next move...
AppleSupport: When you say you "reset" your device, could you tell us if you went to Settings &gt; General &gt; Reset &gt; 'Reset All Settings' or 'Erase All Content and Settings'? Also, do you have access to a computer that has or could be used for iTunes?
Customer: AppleSupport I actually did both. Yes, I have my phone backed up to iTunes on home laptop
AppleSupport: We'd like to work with you further in DM. Use the link below to send us a message and we'll go from there. [link]
```
</details>

<details><summary>cited conversation #525263</summary>

```
Customer: This is literally what the phone app on my iPhone X looks like right now. It just does this and crashes. Can’t make calls. No voicemail access. Uh... [link]
AppleSupport: We want to make sure you’re able to make calls and access your voicemails successfully. Which iOS version are you currently running? Is this the only app with the issue? Have you completed any troubleshooting steps like turning the device off and back on?
Customer: AppleSupport 11.1 - yep that’s the only app. Turning on/off didn’t help.
```
</details>

## q098

**Question:** How much does Sony charge to repair a PS5 DualSense controller?

**Reference:** Not covered: the PS5 postdates the 2017 dataset. The assistant must not substitute PS4 repair information.

**System answer:**

The 2017 PlayStation support history does not say how much Sony charges to repair a PS5 DualSense controller. Agents never mentioned a DualSense or any repair price for one. When customers asked about PS4 controller warranty or repair options, agents only directed them to warranty or service links and did not quote a charge. What is missing is any agent statement about DualSense repair pricing.

<details><summary>cited conversation #212188</summary>

```
Customer: AskPlayStation hey what’s your warranty or repair options on a PS4 controller ? Had it about a year and one of the buttons is dead .
AskPlayStation: Hi Tiffany. Please check the requirements for in-warranty service here: [link]
```
</details>

<details><summary>cited conversation #31989</summary>

```
Customer: AskPlayStation how much does it cost to have Sony service a launch model PS4? My kid damaged my optical drive, it won't read discs
AskPlayStation: Sorry to hear that! For more info on service, click here: [link]
```
</details>

## q007

**Question:** How do I complain about a rude Uber Eats delivery person?

**Reference:** Uber_Support said to tap the 'Help' button in the app; if you've already done that, DM them your account email so they can follow up.

**System answer:**

In October–November 2017, Uber support’s consistent advice was to file the complaint in writing, not by phone.

For a rude Uber Eats delivery person specifically, agents told customers to send a note through their help link so the team could get in touch and look into it. That was the reply both when someone said their UberEATS driver was rude [#493496] and when someone said a delivery driver was rude and ruined their dinner [#144697]. The same “send a note via the help link” instruction was used for other Uber Eats driver problems, such as a missing part of an order [#390209].

They did not give a customer-care phone number for this. When someone asked where to complain about a rude driver and whether there was a phone line, the agent only pointed them to the help link [#233267]. In a related thread, an agent said they did not offer phone support for these issues and to use the link instead [#404062].

Agents also sometimes asked people to direct-message them, but the details differed:
- One agent asked for a DM with the email address and more details so they could connect [#370232].
- Another asked for a DM with the email and phone number linked to the account [#214381].
- When someone wanted to report a rude driver who was not their own, the agent asked for a DM with the email address so they could connect [#749717].

In the app, when the ride is over, you can rate the driver and also leave a comment [#404062]. Agents said that about a ride, not specifically about an Uber Eats delivery. If the rating option does not appear, they still told people to send the details through the help link [#199651].

On what happens after a report, the only statement in these threads was about a cab driver, not an Uber Eats courier: the agent said that under their privacy policy they could not share what action was taken against the driver, but that the team was reviewing the report and would address it [#679499].

The actual form URLs were not preserved in these transcripts (they show up only as “[link]”). This is from October–November 2017 and the process may have changed.

<details><summary>cited conversation #493496</summary>

```
Customer: My UberEATS driver this morning was rude as fuck 😂 then when I went to go get my food he act like he didn’t see don’t try it I’ll beat yo ass
Uber_Support: Here to help! Send us a note via [link] so our team can get in touch.
```
</details>

<details><summary>cited conversation #144697</summary>

```
Customer: Your delivery driver was rude and ruined my dinner.
Uber_Support: We'd be happy to further assist. Please share details here; [link] so we can take a look into this.
```
</details>

<details><summary>cited conversation #390209</summary>

```
Customer: I had to file a report against this uber eats driver cause he literally left half my order at the restaurant
Uber_Support: We apologize for what happen, kindly send a note here: [link] so our team will get in touch.
```
</details>

<details><summary>cited conversation #233267</summary>

```
Customer: if driver is rude where should we complain? Don't u guys have a customer care number at least for this kind of situation??
Uber_Support: We're sorry to hear this was your experience. Please send us a note here; [link] so our team can connect.
Customer: Uber_Support Thanks
```
</details>

<details><summary>cited conversation #404062</summary>

```
Customer: hello what is your contact info for customer service
Uber_Support: At this moment, we don't offer phone support for these issues. Visit this link [link] so our team can assist.
Customer: Uber_Support The app only lets me rate my driver I want to write a review how do I do that
Uber_Support: Happy to clarify. When the ride is over, you're able to to rate and also provide a comment about your driver.
```
</details>

<details><summary>cited conversation #370232</summary>

```
Customer: I raised one complaint yesterday, yet no action. Ur driver is rude, threaten me in mid journey and u do nothing...
Uber_Support: Sorry about the trouble! Please send us a DM with your email address and more details so we can connect.
Customer: Uber_Support , email - __email__
```
</details>

<details><summary>cited conversation #214381</summary>

```
Customer: just had the craziest rude as fuck experience but idk if i should report the driver cause they have my phone number wtf
Uber_Support: Let's take a further look into this. Please send us a DM with your email and phone number linked to your account.
```
</details>

<details><summary>cited conversation #749717</summary>

```
Customer: Uber_Support how do i report a driver that was not my driver? I just witnessed a driver who picked up a lday on a wheelchair from sfo and he was really hostile and rude to her. also a driver AskLyft
Uber_Support: We take this very seriously. Please send us a DM with your email address so we can connect ASAP.
```
</details>

<details><summary>cited conversation #199651</summary>

```
Customer: Uber_Support I've been trying to report about a driver. But no rating option is coming in the app. How do I go about it?
Uber_Support: Hey, please reach out with the details at [link] so we can help.
Customer: Uber_Support Thank you. Done.
```
</details>

<details><summary>cited conversation #679499</summary>

```
Customer: today cab driver was rude and did not return 10 rupees after paying him 288 and said its for chai and pani.. was so rude with my sister.. [link]
Uber_Support: Sorry to hear about that! Can you please contact us [link] so our team can connect?
Customer: Uber_Support Thanks for reply.ive filled the details and just to let you know the i gave 5 star rating without asking her experience and later i come to know about this. Plwae revert the 5star rating
Uber_Support: We're here to help! Send us a DM with your email address so we can follow up.
Customer: Uber_Support Dm has been sent..pls take some action as its not acceptable with any female passenger
Uber_Support: Hi there! We see your outreach and a member of our team will be following up via email as soon as possible. We appreciate your patience.
Customer: Uber_Support Guys..i m not looking out discounts( Received email for ₹50 discount coupon) i want you to take action against that rude driver.
Uber_Support: Thanks for reaching out. in accordance with our privacy policy, we are unable to provide you with information in regards to actions taken against the driver. However, our team is reviewing your report and will be sure to address it appropriately.
```
</details>

## q026

**Question:** Was the recent Comcast internet outage caused by Level 3?

**Reference:** comcastcares said there was a known issue with Level 3 earlier that caused problems and that it had been resolved.

**System answer:**

The 2017 Comcast support history does not show that the internet outage was caused by Level 3. On November 6, 2017, agents acknowledged a nationwide internet interruption and said they were working to fix it, and later that it had been resolved, but they never named a cause. When customers said it was a Level 3 (CenturyLink) peering or backbone issue, agents did not confirm or deny that. They replied with things like “I understand,” asked for account details, or repeated that there was a nationwide interruption. What is missing is any agent statement attributing the outage to Level 3. This is from 2017 tweets and may not reflect later events.

<details><summary>cited conversation #456404</summary>

```
Customer: is there an outage in Fort Lauderdale? Many offices showing tremendous latency.
comcastcares: There is a nationwide interruption causing connection issues. We are aware and working to get this resolved as quickly as possible. –SLM
```
</details>

<details><summary>cited conversation #456199</summary>

```
Customer: Can always count on my cell service for a hot spot. When will comcastcares start paying for data due to poor serv
comcastcares: I understand your frustrations. There is a nationwide interruption causing connection issues. We are aware &amp; working to fix. –SLM
```
</details>

<details><summary>cited conversation #457149</summary>

```
Customer: “Some” LOL [link]
comcastcares: We are aware of a current nationwide issue. We are working towards a resolution. You can follow comcastcares for updates. -CF
```
</details>

<details><summary>cited conversation #455202</summary>

```
Customer: Complained to earlier today about ongoing unhappiness I have with them. All of a sudden internet’s not working. So vindictive.
Customer: Not comcast. It's a North American Internet outage involving several backbone routers
comcastcares: I would be happy to look further into your service issues if you would provide your full address and account associated phone # in a DM. -JW
Customer: Ah interesting. Thank you. I’ve had long issue with them this summer, so it seemed specific and personal.
comcastcares: There was a nationwide issue for internet. The issue was recently resolved. Are you still having issues with your services? -JW
comcastcares: I just wanted to follow up with you and see if you are still having any issues with your services. -JW
Customer: comcastcares Working fine now. Thanks! Just need to downgrade services to internet only, but no time to do that today. :) Thanks for checking in
comcastcares: I'm glad this was resolved. We can help you downgrade the services, please DM when you get a chance. -DP
```
</details>

<details><summary>cited conversation #455104</summary>

```
Customer: Can't tell if this is just a packet loss issue or a larger peering issue. Someone fix the internet please! #packetloss #routing
comcastcares: I can look into your internet issue. Can you DM the phone number on your account? -VG
Customer: comcastcares Thanks, but it's not just me. Looks like a country-wide Level3 peering issue: [link]
comcastcares: I understand. Would you like for me to look into this for you? -VG
Customer: comcastcares Yes, but look into it for the hundreds of thousands of us who are affected, not just me: [link]
comcastcares: Thanks for your feedback. Feel free to reach out if you have any other questions or concerns. -VG
Customer: comcastcares Some detail on how you're fixing this for the hundreds of thousands of impacted customers would be nice
Customer: comcastcares If only we could get rid of Net Neutrality we could pay extra for our outages + template responses.
Customer: comcastcares Haha. It's fixed now. And to be fair, a country-wide outage between major peers is noticed immediately by their NOC.
```
</details>

<details><summary>cited conversation #456429</summary>

```
Customer: Map finally loaded [link]
Customer: it's an issue with Level3 which provides backbone and internet connectivity to many large ISPs
Customer: Well aware. We're monitoring it as best we can at work right now. All clients are freaking out.
Customer: But it's specifically Comcast to L3 (CenturyLink now) which is why all the hullabaloo about Comcast.
Customer: Finally got the Level 3 map to load. Notice how it matches Comcast. [link]
comcastcares: Hi, I would be happy to help look in to the services. Can you please send me a DM with your acct# or phone# so I can assist you? -CLR
Customer: comcastcares Service is restored, thank you. [link]
```
</details>

<details><summary>cited conversation #453993</summary>

```
Customer: CenturyLink completes acquisition of Level 3. #WelcomeToTheNewCenturyLink [link]
Customer: You tweet this and then your backbone takes a huge shit less than an hour later, majorly impacting Comcast's service. Really makes you 🤔
comcastcares: Hi, I would be happy to help look into the services. Can you please send me a DM with your acct# or phone# so I can assist you? -CLR
```
</details>

<details><summary>cited conversation #466943</summary>

```
Customer: internet went out again. Detroit. 5 minutes. Happening all day. If this is a CenturyLink issue, how do we hold them accountable?
comcastcares: Hello, I apologize about the interruption and I can further investigate. Please DM me if you are still experiencing issues. -ADW
```
</details>

<details><summary>cited conversation #532741</summary>

```
Customer: comcastcares Intermittent internet connectivity here. TV okay, but internet goes down randomly and reconnects after awhile. Is this still the effect of the Level 3 outages last week? Please don't make me call tech support - if I get asked if my power's out, I may lose it! :/
comcastcares: Let's see what's going on with that connection. Please DM your phone/account number so I can look into this for you. - KM
```
</details>

## q099

**Question:** Does Tesla include free Supercharging with the Model 3?

**Reference:** Not covered: Tesla isn't in the corpus.

**System answer:**

The 2017 Twitter support history does not include Tesla, and no company agent in those conversations discusses whether free Supercharging is included with the Model 3. Mentions of Tesla are unrelated (for example, ride-hail vehicle eligibility), so the history does not answer this question.

_(no conversations cited)_

## q037

**Question:** Why was British Airways flight BA2278 from Oakland cancelled on 18 November?

**Reference:** BA said it was cancelled because of a technical issue with the aircraft.

**System answer:**

British Airways told a passenger that flight BA2278 on 18 November was cancelled due to a technical issue with the aircraft. This is from their 2017 Twitter support replies and may not reflect any later official account.

<details><summary>cited conversation #618126</summary>

```
Customer: British_Airways no explanation! Hours on hold,sent to different departure airport,different arrival airport,late, need to be home for cats! [link]
British_Airways: Sorry for the disruption to your journey, Laura. I do hope you're on your way soon. Let us know if you'd like us to give you a call to discuss the issue. ^Lisa
Customer: British_Airways Please let me know why flight BA2278 from Oakland at 16.25 was cancelled with such short notice. Thank you
British_Airways: Hi Laura, BA2278 on 18 Nov was cancelled due to a technical issue with aircraft. I'm sorry for any inconvenience this caused you. If you need any help, please DM your full name, reference, contact number, passport number, passport expiry and date of birth, and we'll take a look.
```
</details>

## q006

**Question:** If I schedule an Uber ride in advance, am I guaranteed a driver?

**Reference:** No. Uber_Support said scheduling doesn't guarantee a driver; if none can be found you're notified at the end of your selected 15-minute window.

**System answer:**

No. Uber support agents said scheduling a ride in advance does not guarantee you’ll be connected with a driver.

They described the process as a request, not a reservation: a nearby driver is requested on your behalf at the start of the pickup window you selected, and only then do you see the driver’s information. If no driver can be found, they said you’d be notified at the end of that window, which agents consistently described as 15 minutes (one reply referred only to “the end of your selected time window”). They called a missed match rare, but still not guaranteed.

This is what agents told customers in October–December 2017 and may have changed since.

<details><summary>cited conversation #708738</summary>

```
Customer: prebooking a trip with you does not mean you get a ride. It’s a stupid system
Uber_Support: Here to help! Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver cannot be found, you'll be notified at the end of your selected time window of 15 minutes. For more information on this, visit; [link]
Customer: Uber_Support Problem is at that point it’s too late to schedule alternate transportation so my only choice is to not use uber and pay more to guarantee I have a ride when I need one. The town car people will guarantee me a ride for when I schedule it.
Uber_Support: We always appreciate feedback, please reach out directly so we can further connect; [link]
Customer: Uber_Support try UZURV, its legit
```
</details>

<details><summary>cited conversation #796333</summary>

```
Customer: if I’ve booked a trip will it defo happen?? Worried they won’t take me where I need to go !
Uber_Support: Hi there. Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver can't be found, you'll be notified at the end of your selected time window of 15 minutes. For more information on this, click here; [link]
```
</details>

<details><summary>cited conversation #658508</summary>

```
Customer: Uber_Support This is first time using UBER. I scheduled a ride and I now I see only "cancel Ride"- there is no "Edit Time" in [Your Trips] page of the App. Is that mean that it is a set, scheduled? I want to make sure that someone will definitely pick me up tomorrow morning.
Uber_Support: Here to help! For more info please visit; [link]
Customer: Uber_Support Yes, I saw this page a dozen time. It says "scheduling a ride in advance does not guarantee you'll be connected with a driver. " How do I know I surely have a driver?- do I get an information about car and a driver in [Your Trips] page of Uber App?- because I see no driver info.
Uber_Support: We can certainly understand your concern, Hyeonji. When you schedule a ride, a nearby driver-partner will be requested on your behalf at the beginning of the pickup window you selected. At that point, you will see your driver's information. Hope this clarifies.
Customer: Uber_Support Sorry for keep asking- I have no idea that there will be a set ride for tomorrow or not. If I do not see any information yet,it means that there are nobody responding to my request yet, right? As soon as a driver-parter nearby responds , then I see info?
Uber_Support: Happy to take a closer look! Send us a DM with your email address so we can follow up.
```
</details>

<details><summary>cited conversation #723375</summary>

```
Customer: Uber_Support how do I know for sure that my scheduled pickup time is truly confirmed?
Uber_Support: Hi! Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver cannot be found, you'll be notified at the end of your selected time window of 15 minutes. For more info, click here; [link]
```
</details>

<details><summary>cited conversation #500540</summary>

```
Customer: used the Uber schedule ride feature for the first time, booked a cab 2 days ago and guess what....Let me down
Uber_Support: Here to help! Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver cannot be found, you'll be notified at the end of your selected time window of 15 minutes. For more info on this, click here; [link]
Customer: Uber_Support Might be there first and last time I use this
```
</details>

<details><summary>cited conversation #648990</summary>

```
Customer: hey thanks for cancelling my scheduled ride ONE MINUTE before it was set to start &amp; making me scramble to get a ride — no wonder all my friends are switching to Lyft... guess i will be too :)
Uber_Support: Sorry to hear this, Tina. Please note, scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case a driver cannot be found, you'll be notified at the end of your selected time window. We apologize for any inconvenience caused.
```
</details>

<details><summary>cited conversation #737160</summary>

```
Customer: Why even bothering scheduling a pick-up on when they’re going to give you a 20 minute window that you then have to wait for a driver to accept #notcool #35minuteslater 🖕
Uber_Support: Hi! Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver cannot be found, you'll be notified at the end of your selected time window of 15 minutes. For more information on this, click here; [link] .
```
</details>

## q040

**Question:** I paid for Wi-Fi on a Virgin Trains train and it doesn't work. What should I do?

**Reference:** VirginTrains suggested forgetting the network in your device settings, reconnecting, and following their link.

**System answer:**

In 2017, Virgin Trains agents told passengers whose paid onboard Wi-Fi wasn’t working to try a few fixes, then contact Wi-Fi support or claim a refund.

Troubleshooting they suggested:
- One agent asked whether the passenger was connected to the network named virgintrainswifi and had [link] open in a browser/tab [#649348].
- Another told a passenger to forget the network in their settings, reconnect, and follow [link] [#574203]. When that didn’t work, that same agent suggested speaking to the onboard team to see if they could reset the system. Earlier in that conversation they had asked whether the issue was speed or connection [#574203]. Other agents also asked if the problem was speed or connection, but did not go on to suggest an onboard reset [#81479][#403201].

If those steps didn’t help, agents gave the Wi-Fi support number 0330 088 1271 (also written 03300881271). One agent said that team could try to reset the connection [#743901]. Another gave the number without saying what the team would do [#574203]. A third said the team should be able to assist further [#403201]. A fourth said you can speak with the Wi-Fi team on that number regarding refunds if the Wi-Fi didn’t work [#174853].

For a refund or compensation when paid Wi-Fi failed, agents repeatedly said to email them (the address is redacted in these transcripts as __email__) [#649348][#81479][#574203][#403201]. One agent described it as a claim for compensation [#81479]; another said to contact that email for a full refund [#403201].

These replies are from October–November 2017, so the phone number, email, and process may have changed since.

<details><summary>cited conversation #649348</summary>

```
Customer: £5 for wifi that doesn't even work on a £60 train journey. Bravo VirginTrains
VirginTrains: Are you connected to virgintrainswifi and have [link] open in a browser/tab? ^CB
Customer: VirginTrains Sorry couldn't reply as had no wifi. Currently using free Wi-fi on a £4.60 40 minute journey with a better train company. Cheers for ripping me off 👍🏻
VirginTrains: You can claim a refund via __email__ ^MM
```
</details>

<details><summary>cited conversation #81479</summary>

```
Customer: Hey VirginTrains I paid £5 for wifi on your train and it doesn't work so I'm having to tether. Anyway I can arrange a refund please?
VirginTrains: Hi there, sorry to hear you're having issues with the Wi-Fi. Is the problem with connection or speed? ^HP
Customer: VirginTrains The connection was almost non-Existent :( had some work to do so had to tether from my phone
VirginTrains: Really sorry about that, Codie :/ Please make a claim for compensation by contacting __email__ ^HP
```
</details>

<details><summary>cited conversation #743901</summary>

```
Customer: VirginTrains hello I’m on the 11.55 Manchester Piccadilly train to London Euston - have paid for a days wifi access. Access code is not working. Train manager has reset wifi. Still not working. Lease help or refund. Thank you.
VirginTrains: Sorry to hear that, might be worth speaking to the Wi-Fi support tam about this on 0330 088 1271 and they can try and reset this for you, Lisa ^MW
```
</details>

<details><summary>cited conversation #574203</summary>

```
Customer: Paid £5 for 24 hour access to VirginTrains WiFi which hasn’t worked for most of the journey. Very disappointing.
VirginTrains: Sorry to hear that, Kevin, is the issue with speed or connection? ^HP
Customer: VirginTrains Both. When it’s working, it’s slow. But keeps losing connection altogether for the most part. 9:35 from Chester to Euston
VirginTrains: Apologies Kevin, can you please try forgetting the network in your settings, reconnect &amp; follow [link] ^HP
Customer: VirginTrains Tried - no internet [link]
VirginTrains: Really sorry about that, Kevin, it may be worth speaking to the onboard team to see if they can reset the system for you ^HP
Customer: VirginTrains This train is packed - there is no way I’m risking losing my seat. This is not helpful
Customer: VirginTrains The WiFi only works when the train is static!
VirginTrains: Apologies for the inconvenience caused, Kevin. You can also contact our Wi-Fi support team on 03300881271 ^HP
Customer: VirginTrains Making a call on a train is like walking up a hill of sticky toffee sauce barefoot!
VirginTrains: Sorry about this issue, Kevin. You can apply for a refund for your pass by contacting __email__ ^HP
```
</details>

<details><summary>cited conversation #403201</summary>

```
Customer: OMG The WiFi on VirginTrains is diabolical and they have the cheek to charge for £5 for this "service".
VirginTrains: Hi Mark, sorry to hear you're having issues with the Wi-Fi. Is the problem with speed or connection? ^HP
Customer: VirginTrains Both! A very slow connection, 3 min to load twitter page. You block the sites I need to work. VPNs blocked. I can't work on your train.
VirginTrains: 1/2 Really sorry for the inconvenience caused to you, Mark. It may be worth contacting our Wi-Fi support team on 03300881271
VirginTrains: 2/2 as they should be able to assist further. Alternatively you can claim a refund by contacting __email__
Customer: VirginTrains I seriously doubt that. Last time they hung up on me when I asked about vpns
VirginTrains: So sorry for your experience Mark. Please do contact the above email to claim a full refund ^HP
Customer: VirginTrains may not entirely be VT's or their providers fault. 4G lineside coverage for wifi south of the midlands is typically appalling.
```
</details>

<details><summary>cited conversation #174853</summary>

```
Customer: VirginTrains wifi onboard is woeful Runcorn to London can't believe I have paid for it #freewifiplease #shoulddobetter
VirginTrains: Sorry to hear you're having Wi-Fi trouble, Rachael. Is it not connecting? ^LC
Customer: VirginTrains Poor wifi is inexcusable in 2017, but poor wifi when you have paid for it.....
VirginTrains: You can also speak with our WiFi team regarding refunds if your WiFi didn't work, on 03300881271 . ^BT
```
</details>

## q035

**Question:** Why does British Airways sell more tickets than there are seats on a flight?

**Reference:** BA said overselling is common airline practice that keeps fares low; when a flight is oversold they ask for volunteers to travel later and, if nobody volunteers, select passengers.

**System answer:**

British Airways agents in 2017 said they deliberately sell more tickets than there are seats because some passengers book and then don’t turn up, or change to a later flight. Overselling is meant to avoid flying with empty seats, which they said helps keep fares lower. They described it as common across the airline industry. One agent said it is only done on flights that have a history of passengers who fail to show, or who are likely to change their tickets to later flights. They also said they sometimes misjudge the numbers; when that happens, airport staff are expected to rebook affected passengers and offer compensation. This is what their support agents told customers in October–December 2017, so the practice or how they explain it may have changed since.

<details><summary>cited conversation #312234</summary>

```
Customer: British_Airways Unless the flight is overbooked likes yesterday. 7 passengers denied boarding GOT-LHR
British_Airways: Hi Ian, most airlines oversell flights in order to keep fares as low as possible, but I'm sorry to hear we misjudged the numbers on this 1/3
British_Airways: occasion. I hope our airport staff rebooked you and offered compensation? If not, please DM your reference, email and contact number 2/3
British_Airways: and we'll be happy to take a look. ^BS 3/3
Customer: British_Airways BA agents followed the rules, rebooked on a later flight and the BA compensation card. The point is overbooking is immoral...........
Customer: British_Airways .......selling seats you don’t have. Even Ryanair dong do it.
British_Airways: We appreciate your feedback, Ian. We do get customers who don't turn up for their flights. To keep our fares low and not to have 1/2
British_Airways: empty seats, we do oversell our flights. 2/2 ^Linda
Customer: British_Airways BA should have a good look at this overbooking policy. No employee of my company will ever fly BA again whilst on business.
British_Airways: We're sorry you feel this way, Ian. This is something most airlines do. We do hope to welcome you and your employees on board again soon. ^L
Customer: British_Airways Most airlines have a different approach. Usually asking at checkin or the gate if passengers would like to catch a later flight. Not BA thou
Customer: British_Airways In which case you’ve just lost a customer. Don’t try to sell me a good deal...only to tell me I might not actually get seat once at airport!
British_Airways: We appreciate your frustration, Ian. We can only offer our sincere apologies for any inconvenience caused. ^Cody
Customer: British_Airways Most airlines oversell flights because who cares about the passengers #FTFY
```
</details>

<details><summary>cited conversation #550872</summary>

```
Customer: How is it allowed for British_Airways to continue to sell WT+ tickets for todays BA106, while they are knowingly downgrading passengers at the airport!!!
British_Airways: Hi Sam. Tickets are automatically sold up to the time check-in closes. Any customers downgraded will receive compensation and a refund in the difference in fare based on the flown leg. ^N
Customer: British_Airways but that's not the point, you should not be allowed to sell tickets for a class you know is full! 1/2
British_Airways: We have an overbooking policy, as some passengers don't turn up for their flight, Sam. We're sorry for any disappointment this has caused. ^Leanne
```
</details>

<details><summary>cited conversation #718349</summary>

```
Customer: British_Airways ridiculous policy overbooking your flights, my husband left his family this afternoon to make his meeting tomorrow and you couldn't get him on his flight. He will now miss his meeting and us!
British_Airways: Hi Vicki. We're sorry to hear that your husband was denied boarding today. Overselling flights is common place in the airline industry and only done on flights that have a history of passengers who fail to show, or are likely to change their tickets to later flights. It's a 1/2
British_Airways: strategy which helps keep fares down as we avoid operating with empty seats. We're so sorry on this occasion our figures were clearly wrong. Our airport staff will have compensated your husband and arranged an alternative flight. 2/2 ^Natalie
Customer: British_Airways It must have cost you some money, there were 3 of them in the same hotel Sunday night!
British_Airways: Sometimes we get the numbers wrong, Vicki. We collect all data and use that to make decisions in the future. Thanks for your concern. ^Julie
```
</details>

<details><summary>cited conversation #559727</summary>

```
Customer: Really enjoy it when they overbook your flight and say 'we'll let you know if you can board this flight when boarding begins (enjoy the run through security).' Cheers British_Airways
British_Airways: We're sorry to hear your flight has been oversold, Dan. However, we do have an overbooking policy, as some passengers book and don't turn up for their flight. This helps us keep our fares down and avoids flying with empty seats. ^Leanne
```
</details>

<details><summary>cited conversation #788358</summary>

```
Customer: British_Airways I book and pay for a flight 6 months ago. I arrive at LHR for you to tell methe flight is full and we go on standby?!? What the actual F**K are you playing at!!
British_Airways: We're sorry this has happened, Carl. We do oversell flights to counteract customers not turning up, for example. This helps lower our fares. We hope you're able to be confirmed, and if not, our staff will rebook you and let you know about compensation. ^Cecilia
```
</details>

<details><summary>cited conversation #297536</summary>

```
Customer: So fed up to get to airport and discover that British_Airways has overbooked my flight and may not be able to get on it 😫😫😫😫
British_Airways: We're sorry to hear this, Victoria. Our airport staff will keep you updated with any additional info. We hope you don't have to 1/2
British_Airways: wait too long. 2/2 ^JR
Customer: British_Airways Why do you overbook flights?
British_Airways: Hi Victoria. It's commonplace in the airline industry to oversell flights to keep ticket prices down. 1/2
British_Airways: Is there anything we can assist with? 2/2 ^David S
Customer: British_Airways Yes with getting on the flight please
British_Airways: We're sorry we're unable assist from here, Victoria. Our colleagues at the airport will do all they can to assist. 1/2
British_Airways: Please accept out apologies for any inconvenience caused. 2/2 ^David S
Customer: British_Airways From what I am hearing it sounds like they can’t do anything unless other passenger don’t turn up
British_Airways: If you'd like us to check alternative flights, please DM us your full name, booking ref, email and contact number. 1/2
British_Airways: However, our colleagues at the airport are best placed to assist. 2/2 ^David S
Customer: British_Airways Well none of your staff are at the gate yet so there is no-one here to assist
Customer: British_Airways You don do this automatically when you take someone’s booking then decline to honour it. I have to make a request to get on any flight now?!
```
</details>

## q094

**Question:** How do I move my Instagram account to a new phone number?

**Reference:** Not covered: Instagram support isn't in the corpus.

**System answer:**

The 2017 Twitter support history doesn’t answer this. Instagram isn’t one of the companies in the logs, and no support agent explained how to move or reassign an Instagram account to a new phone number. Mentions of Instagram are about app issues (notifications, crashes, data use), not changing the phone number on an Instagram account.

_(no conversations cited)_

## q079

**Question:** My O2 Priority code for the Star Wars phone case isn't taking any money off at checkout. Why?

**Reference:** O2 said the codes ran out very quickly because the offer was so popular.

**System answer:**

In November 2017, O2 said the Priority Star Wars phone-case codes ran out very quickly because the offer was so popular. When a customer redeemed a code and the checkout price did not drop, agents told them they had missed out that time [#662904].

Agents gave related explanations depending on the day and the error:
- There were no more codes available for that day, and they suggested checking the Priority app again the next day [#663426].
- If checkout said the code did not exist, they said the cases were in high demand and to watch the app again from 9am the next day [#677703].
- On 21 November they said the offer had been paused and would go live again at 9am the next day [#647369].

This was a limited, high-demand 2017 offer, so those code-availability rules would not still apply now.

<details><summary>cited conversation #662904</summary>

```
Customer: O2 hi just redeemed a code from priority, I went to the website and it does not work?
O2: Hi Shiva 👋 Which code are you trying to redeem? What error message are you getting when you try to use it?
Customer: O2 Hi I am trying to redeem the Star Wars case and when I click redeem it just loads but the price does not go down
O2: Ah right, did you copy the code over and use it at the online checkout?
Customer: O2 Yes I did
O2: The codes ran out very quickly yesterday as the offer was so popular. We're sorry you missed out this time.
```
</details>

<details><summary>cited conversation #663426</summary>

```
Customer: O2 You're O2 priorities Star Wars phone case offer isn't working and no one is responding from support, can you help????
O2: 😞 There are no more codes available for today. Check the app tomorrow to try again.
```
</details>

<details><summary>cited conversation #677703</summary>

```
Customer: O2 Hi there, The code for the Star Wars phone case doesn't seem to work, it says it doesn't exist when entering it at the check out
O2: Sorry you missed out this time Emma, they are in high demand. However, keep your eye on the app again tomorrow from 9am, who knows! 😉
```
</details>

<details><summary>cited conversation #647369</summary>

```
Customer: O2 #priority errr... [link]
O2: 😔 We'd like to help Brian, is this when you're trying to redeem the Star Wars case offer? The offer has been paused now and will be live again at 9am tomorrow.
```
</details>

## q097

**Question:** What is the battery capacity of the iPhone 15?

**Reference:** Not covered: the iPhone 15 postdates the 2017 dataset. The assistant must not answer with older iPhone battery information.

**System answer:**

The support history does not include the battery capacity of the iPhone 15. These conversations are from October–December 2017, and Apple Support agents never discussed an iPhone 15 (that model was not available then). Mentions of “15” in Apple battery threads refer to charge percentage, minutes, or hold times, not the iPhone 15.

_(no conversations cited)_
