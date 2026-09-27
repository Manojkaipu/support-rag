# Hand grading

For each answer, judge only from the cited conversations (and the reference answer):
- **grounded**: every factual claim is said (or fairly paraphrased) by a company agent in a cited conversation
- **correct**: it conveys the reference answer's main point (for unanswerable questions: it declined)
- **abstained**: it says the history doesn't answer the question

Record true/false for each in eval/human_grades.jsonl (the item with the same id), plus notes.

## q017

**Question:** My Delta account got locked after too many failed login attempts. How do I get back in?

**Reference:** Delta said the account stays locked for 24 hours after the last failed attempt; after that you can try again, but more wrong attempts will lock it again.

**System answer:**

In late 2017, Delta agents said a SkyMiles account locked after too many failed logins unlocks itself after 24 hours, and Twitter agents generally cannot unlock it sooner.

Wait 24 hours from the last failed attempt (one agent said “exactly 24 hours after the initial security lock”), then use Forgot Password and follow the reset-email link. More wrong attempts will lock you out again. Agents said they cannot set a temporary password, and most said they have no way to speed up the unlock. [#461842] [#317108] [#412506] [#336794] [#339225] [#548132] [#523166] [#630401]

Some agents also gave a phone option: Online Support at 888-750-3284. The agent in [#91099] stressed that this is Online Support, not regular customer service. Another agent called it the Online Customer Support Desk at the same number and still said the account unlocks itself after 24 hours. [#168402]

Other replies varied. One agent sent a password-reset email and said password-procedure changes might require contacting SkyMiles Support with a copy of ID. [#512827] A few asked for the SkyMiles number by DM; one said locked accounts are not unlockable by an agent but offered to send a reset email, and another said they might be able to unlock it via DM. [#548132] [#512862] In one case a customer later reported that tech support had unlocked the account and sent a reset link without a 24-hour wait; the agent only said they were glad it was unlocked and did not confirm that as the process. [#630401] If you need to travel before the lock lifts, an agent said you can still book and then add your SkyMiles number to the reservation for credit. [#523166]

This is from October–November 2017 and may have changed.

<details><summary>cited conversation #461842</summary>

```
Customer: Delta can you please unlock my account? It says it was locked due to many login attempts
Delta: Unfortunately, you would need to wait 24 hours for the account to unlock itself. Thank you. *TMB
```
</details>

<details><summary>cited conversation #317108</summary>

```
Customer: delta my delta acc has been disabled due exceed login attemp is there a way to re enabled my acc ? Thx
Delta: Unfortunately, the account will be locked for 24 hours after your last failed login attempt. *AJY
Customer: Delta Ok, so after that 24 hrs it will automatically unlock right?
Delta: Yes, you can try it again in 24 hours. Unfortunately, too many wrong attempts will lock you out. *TAY
```
</details>

<details><summary>cited conversation #412506</summary>

```
Customer: Delta Can't get into account; asked 4 times for link to reset, now locked out. # for asst is 2 hr hold. Can you help?
Delta: Sharon, we are unable to unlock the account. It will automatically unlock exactly 24 hours after the initial security lock. *ACJ
```
</details>

<details><summary>cited conversation #336794</summary>

```
Customer: Delta locked out of SkyMiles acct.. waited 1hr for a call back told there is NO way to reset account? Have to wait 24 hrs?
Delta: I apologize for this. For security, please allow 24 hours to go by then select "Forgot Password" to gain access. Thanks. *ATJ
```
</details>

<details><summary>cited conversation #339225</summary>

```
Customer: Delta I’ve now tried yet again to get account unlocked. I have been on hold multiple times 4 several hours over months. Why anyone help?
Delta: Sir, we are currently showing that your account is not locked. Your account is showing no conflicts. *TMA
Delta: You just need to set up a password, and you can access your account. *TMA
Customer: Delta When I click on the link and go to set up the password I am being told that the account is locked. Am I doing something wrong?
Delta: It would be our pleasure to help you find out, so you can resolve your issue. Please DM a contact phone #, for assistance. Thanks. *TMA
Customer: Delta I already have multiple times
Customer: Delta This is the same path I have already been down
Customer: Delta Can you please set up a temporary password for me so I can login and change it?
Delta: If you have been sent an email to reset your password, and then it tells you the account is locked, nothing can be done for 24 hours. *TMT
Delta: Please follow the email link in 24 hours to reset your password. We cannot set up a temporary password. *TMT
Customer: Delta You guys have told me this 4c,s in the last several weeks. It does not work. Please come up with a workaround. This is beyond frustrating
```
</details>

<details><summary>cited conversation #548132</summary>

```
Customer: Hey Delta - a hold time of between 65 and 115 minutes is UNACCEPTABLE. You need to do better. Password trouble isn't worth that time. Nothing is.
Delta: I apologize for the increased hold times. We are working furiously to reduce the wait, despite heavily increased call volume. In the meantime, please feel free to reach out to us right here for assistance. Are you still in need of password assistance? *ASK
Customer: Delta Yes. Password assistance. Locked. Can you unlock?
Delta: Locked SkyMiles accounts are not unlockable by agent. However, if you wait 24 hours from the time of the last attempted login, you can perform a password reset. If you wouldnt't mind sharing your SkyMiles account number via DM, I can get a password reset email out to you. *ASK
Delta: You can use the following link to share your SkyMiles number via DM. *ASK [link]
```
</details>

<details><summary>cited conversation #523166</summary>

```
Customer: Delta 2 hour wait when I need my account unlocked? That's ridiculous.
Delta: Hi Melanie, when your SkyMiles account is locked, it will automatically unlock 24 hours later. We don't have a way to hasten the process; you'll still be able to book flights and then add your SkyMiles account to the reservation to get credited for your trip. *TJP
Customer: Delta Ok thank you for the update. I'm flying out Monday so I want to make sure I can use my app.
Delta: You're welcome, take care! *TMB
```
</details>

<details><summary>cited conversation #630401</summary>

```
Customer: can someone help me unlock my online account? very long hold time to customer service
Delta: Hi Shawn, we can send you a forgot password but once a SkyMiles account is locked you have to wait 24 hours and it will automatically unlock itself. Thank you. *TMB
Customer: Delta FYI - got to tech support. Unlocked acct. Sent me link to reset password. I accessed acct. shld prob update ur procedures. 24 hour wait not req'd.
Delta: Glad to hear you were able to unlock your account, have a great night! *TMB
```
</details>

<details><summary>cited conversation #91099</summary>

```
Customer: Delta my account is locked, why.
Delta: Good evening. This typically occurs after too many failed log-in attempts. *ABN
Delta: Please contact our Online Support Team at 888-750-3284. Enjoy your evening! *ABN
Customer: Delta The wait for customer service is 2 hours long. Any other way to get it unlocked
Delta: I've given you the # for Online Support, not Customer Service. Please contact Online Support. *ABN
```
</details>

<details><summary>cited conversation #168402</summary>

```
Customer: Delta what’s your # to call if I locked my sky miles account
Delta: Hello, Lisa! I am sorry that you are locked out of your account. The account will unlock itself after 24hrs. You can call Online... 1/2
Delta: ...Customer Support Desk 888 750 3284. *TCC 2/2
Customer: Delta Thanks !
Delta: You're very welcome! *ABN
```
</details>

<details><summary>cited conversation #512827</summary>

```
Customer: Delta trying to log into account. 9074837189. but I think it is locked from too many login attempts. can you unlock
Delta: I just sent a reset email to the address on the account. However, due to changes in password procedures, it may be necessary to contact SkyMiles Support through [link] with a copy of your ID to get it reset. *HWG
```
</details>

<details><summary>cited conversation #512862</summary>

```
Customer: You locked me out of my app and my flight is tomorrow and i contacted you via your website at 6am this morning and it is not fixed delta
Customer: Delta And it is a two hour wait right now to be on hold Delta
Delta: Hey, can you DM your SkyMiles account to the link provided? I maybe able to unlock it for you. *TBT [link]
```
</details>

## q019

**Question:** Miles from one leg of my Delta trip vanished from my SkyMiles account. What can I do?

**Reference:** Delta agents resubmitted the flight for credit and sent a review request to the SkyMiles team, promising an update.

**System answer:**

In a 2017 case almost like yours, a customer said miles from a previous leg had disappeared from the SkyMiles account. The first agent said the credit had been pending and should already have posted, and that they had resubmitted it. After the customer clarified which leg it was, a second agent said they would submit the request to the SkyMiles team for review and would update the customer once they had news [#346777]. Another customer whose status miles were deleted was asked to DM their SkyMiles number so an agent could look [#337933].

Agents also described these other steps, and they did not all say the same thing:

1. **Wait for posting.** One agent said Delta-operated flights can take up to 24 hours after travel is complete, and partner-operated flights up to 7 business days [#263286]. Another said mileage can take 7–10 days, and offered to double-check if the customer shared a SkyMiles number and/or confirmation number by DM [#204075]. For partner flights, other agents said about 30 business days [#241281] or up to six weeks [#44947].

2. **Request the credit yourself.** One agent said you can retroactively add mileage credit once logged into your SkyMiles account, and that you need the ticket numbers of the previous flights, which begin with “006” [#769274]. When that customer saw zeros after entering the ticket number, the agent said that once you request credit the zeros populate, and eligible miles are posted within 7 business days [#769274]. When a customer got credit for only one of two segments, an agent pointed them to a link to file a request for the missing credit [#629121]. When a recent trip showed 0 miles, an agent said to request miles from a past-dated flight by filling out an online form [#793681].

3. **Have an agent look it up.** Agents asked for a SkyMiles number and ticket number via a link so they could assist [#561046], or a SkyMiles number and/or confirmation number by DM so they could double-check [#204075]. They did not say they would resubmit in those two threads. Resubmission is what the first agent said they had already done in the disappeared-leg case [#346777], and what an agent did when part of a ticket showed “activity not eligible for mileage credit”: that agent resubmitted the ticket to SkyMiles for retro credit and said to allow 7 days [#824157]. After a customer sent a SkyMiles number and a ticket number starting with 006, another agent said to allow 7–10 business days for all eligible SkyMiles to post [#97200].

4. **If a leg shows “not eligible.”** In one thread an agent looked at the account and said they were able to fix it so the customer would get proper credit for that leg [#513726]. In a different thread, where the app said the activity was not eligible, the agent called it Delta’s error and said the miles would post within 48 hours [#138716]. The customer later reported the same error on the return leg; the reply in that thread did not say it had been corrected [#138716].

5. **Fax, from one agent only.** That agent said SkyMiles is a self-monitored program, so discrepancies should be faxed and explained to the SkyMiles support desk at (404) 773-1945 [#312133]. Other agents in these threads used a DM, a ticket lookup, or an online request instead.

6. **If the missing leg was on a partner airline.** An agent said SkyMiles should be added to the reservation before departure when traveling with partner airlines [#82669]. In another thread the customer said they had already filled out a request form for Korean Air flights and then posted their SkyMiles number in the thread after being asked to share it via a link. The agent then queued the Korean Air ticket, said to allow 7 days for the SkyMiles to appear, and noted that with partner-airline travel it can take a few extra weeks for the miles to be credited [#699062].

All of this is from Delta’s Twitter support in late 2017, so the form, fax number, and posting times may have changed.

<details><summary>cited conversation #346777</summary>

```
Customer: delta Seems as though miles from a previous leg of my journey (LHR &gt; ATH) have disappeared from my account. Can you please advise?
Delta: Hi, Chris, it has been pending and should have posted by now. I have resubmitted it for credit for you. I apologize for the delay. *TRR
Customer: Delta Thank you. And apologies - it was JFK &gt; ATH. Miles were in there last week but no longer after yesterday's flight (delayed DL2 from LHR)
Delta: GM Chris. I will submit the request to our SkyMiles team for review. As soon as I have an update, I will provide it to you. *ALS
```
</details>

<details><summary>cited conversation #337933</summary>

```
Customer: Delta any reason my 12status miles were deleted from my account?
Delta: Hi Jon, pls DM your SkyMiles # and I'd be happy to take a look for you. *TJW
```
</details>

<details><summary>cited conversation #263286</summary>

```
Customer: Delta how long does it take for miles to be posted to sky miles account?
Delta: Hello, Darrin. I'll be happy to check on this for you. Can you please share your SkyMiles account number? *AOS
Delta: If your flights are flown by Delta, it can take up to 24 hours after you have completed your travel for the miles to post to your... 1/2
Delta: ...account. If your flights are operated by one of our partner's airlines, it can take up to 7 business days. *AOS 2/2
Customer: Delta 9118594408, I flew to Asheville, NC on the 10th of October.
Delta: Is it okay if I share some information through the following link? Please reply with the link. *AOS [link]
Customer: Delta What is it u need me to do?
```
</details>

<details><summary>cited conversation #204075</summary>

```
Customer: Delta I am missing my sky miles and MQM’s from 2 flights I took this past weekend. How can I fix this?
Delta: Good morning, Christopher. Mileage can take between 7 and 10 days to post to your account. However, I can double check for you. *ASK
Delta: Please share your SkyMiles account number and/or your flight confirmation # via DM at the below link. *ASK [link]
```
</details>

<details><summary>cited conversation #241281</summary>

```
Customer: Hi Delta, my DL ticketed CI flight still hasn't shown up for miles, MQMs or MQDs. How long does this usually take?
Delta: Hi, Luke. It generally takes about 30 business days for partner airline miles to post. They should appear soon! *HJB
```
</details>

<details><summary>cited conversation #44947</summary>

```
Customer: . Delta flew on a partner flight on Monday and miles aren't reflecting on account. MU 9816 HND-SHA. When will I see them? Please help!
Customer: Delta Can someone please help Kevin cc:
Delta: It could take up to six weeks before partner miles are posted. *AFM
```
</details>

<details><summary>cited conversation #769274</summary>

```
Customer: Delta how do I add my oldmiles to my SkyMiles Accnt?
Delta: You can retroactively add mileage credit via [link] once you are logged into your SkyMiles account. You will need the ticket numbers of your previous flights, beginning in "006." *AJC
Customer: Delta I did that and when I put in the ticket number, the miles came up as Zeros all over the [link] do I turn those Zeros into those Flights' Miles?
Delta: Once you request credit, the zeros populate, then eligible miles are posted within 7 business days. *TLT
```
</details>

<details><summary>cited conversation #629121</summary>

```
Customer: Delta I bought mileage booster on 2 segments of my flight and only got credit for one
Delta: Hi MJ, so sorry for this inconvenience. Please follow this link [link] and file a request for the missing the missing credit. Thanks. *TLT
```
</details>

<details><summary>cited conversation #793681</summary>

```
Customer: Delta I have sky miles with you and recent trip shows 0 miles and NO response from customer service.
Delta: Hi Jane. You can request your miles from a past-dated flight by filling out this info [link] *ALS
```
</details>

<details><summary>cited conversation #561046</summary>

```
Customer: Delta how do I add missing miles to my SkyMiles account?
Delta: Hi, Robert, I'd be happy to assist you. Can you provide your SkyMiles number and the ticket number via this link? *TRR [link]
```
</details>

<details><summary>cited conversation #824157</summary>

```
Customer: Delta can you help with my husband’s points from a recent trip?? Have not been processed yet.
Delta: Hi Jennifer, can you please DM me your husbands SkyMiles and ticket number and I'll be happy to look into your request. Thank you. *TMB
Customer: Delta Sky miles 2367362726 ticket #0068677812716 said “activity not eligible for mileage credit” but should have been.
Customer: Delta Received seat upgrade credit but not regular portion ticket upgrade
Delta: Thank you, please allow me a few moments to look into your request. *TMB
Customer: Delta [link]
Customer: Delta [link]
Delta: Thank you. *TMB
Delta: Hi Jennifer, I'm still looking into your request. Thank you for your patience. *TMB
Delta: Jennifer, I've resubmitted the ticket to our SkyMiles department for retro credit. Please allow 7 days for the mileage credit to be added to your husband's account. Thank you. *TMB
Customer: Delta You are the best!!! We love Delta!!
```
</details>

<details><summary>cited conversation #97200</summary>

```
Customer: DELTA how do I get the miles from a flight in March 2017?
Delta: Hello, Eloisa. Pls follow/DM your SkyMiles # and ticket # concerning this flight. *ARD
Customer: Delta 9374597640 Tkt 0067987410771
Delta: Thank you, please allow 7-10 business days for all eligible SkyMiles to post. *HRS
Customer: Delta My 12 year old daughter flew with me on the same flight. Does she need to have her own SkyMiles account or her miles can be posted on mine.
Delta: A separate account would be required, the name on the ticket must match the SkyMiles account. *HRS
```
</details>

<details><summary>cited conversation #513726</summary>

```
Customer: Delta why no skymiles credit for DL9318 on 4 November? #Diamondmedallion 2015401876? Not eligible???
Delta: ...scheduled trip on Nov 10 &amp; 11. *TJN 2/2
Delta: Hi, Richard! Thanks, for reaching out! I have your SkyMiles Account details pulled up. I was able to locate the trip that occurred from Nov 3- Nov 4 and it appears those miles have already posted towards your account. The remaining miles will post once you complete your... 1/2
Customer: Delta DL 9318 from AMS to EBB is showing no credit and " not eligible." Compare to miles posted for same flight in September. Thanks.
Delta: Hi there, lets take a look. One moment please. *HVI
Delta: I was able to fix it for you. You will get the proper credit for the leg. *HVI
Customer: Delta Thanks! #deltaone
Delta: You are welcome! *HVI
```
</details>

<details><summary>cited conversation #138716</summary>

```
Customer: Delta just spent $802 to fly cross-country &amp; my app is telling me “activity not eligible for [SkyMiles] mileage credit”. How can that be?
Delta: Hi, Victor. There was an error on our part. Your miles will be posted within 48 hours, I'm sorry for the inconvenience. *TJH
Customer: Delta Roger that. No worries. Thanks for the quick response!
Delta: You're welcome, take care! *TMB
Customer: Delta Same error on the return leg TUS-ATL. Please correct ASAP. Thanks.
Delta: Hi Victor. I regret the frustration we’ve caused you. Our goal is to do better than that. We certainly appreciate your patience. *TKR
```
</details>

<details><summary>cited conversation #312133</summary>

```
Customer: Delta I think I’m missing miles on my account for 2017. Please see pic below. [link]
Delta: The SkyMiles frequent flyer program is a self-monitored program. *AST
Delta: Therefore; any discrepancies found should be faxed and explained to our SkyMiles support desk at (404)773-1945. *AST
```
</details>

<details><summary>cited conversation #82669</summary>

```
Customer: Delta How can I add miles to my Skymiles acct on a past trip with a partner airline?
Delta: Hi Gabriel. SkyMiles should be added to the reservation prior to flight departure when traveling with our Partner airlines. *ALS
```
</details>

<details><summary>cited conversation #699062</summary>

```
Customer: Delta is there a faster way to receive my missing mileage credit from a partner airline? I've sent in requests but have not heard back. thank you!
Delta: Hi Emily. I'd be happy to look into this for you. Please share your SkyMiles number via this link to better assist. *TKR [link]
Customer: Delta Hi! My number is 9070686515. I have two korean air flights I used my skymiles number for, but didnt get credit. I was told I could get the miles for it and I had to fill out a request form. Filled the forms but haven’t heard back yet. Any assistance is greatly appreciated!
Delta: Hi Emily, I've queued your Korean Air ticket in our system. Please allow 7 days for the SkyMiles to appear in your account. With partner airline travel it can take a few extra weeks for the miles to be credited. Thank you. *TMB
Customer: Delta Thank you so much!!
Delta: You're welcome, take care. *TMB
```
</details>

## q080

**Question:** I received a phishing email pretending to be from PayPal. Where should I send it?

**Reference:** AskPayPal asked for the email to be forwarded to its phishing-report address (redacted in the dataset as __email__) and asked the customer to delete the screenshot they had posted.

**System answer:**

In 2017, PayPal support agents told people who received a phishing email pretending to be from PayPal to forward that email to PayPal’s reporting address so the team could look into it. In these transcripts the address itself is redacted (shown only as a placeholder), so the exact inbox cannot be recovered from this history.

What agents said:
- Forward the fake or phishing email to that reporting address; they would then review it, take action, or archive it [#778256] [#234241] [#515646] [#643580] [#2049] [#785275].
- After forwarding, delete the email from your inbox [#759752] [#203418].
- One agent distinguished two addresses (both redacted here): one to use for verification, and another if you are sure it is a phishing email [#632766].
- In one thread, after a report had already been sent, an agent said PayPal’s spoof/phishing team would look it over from there [#647228].
- In another case, an agent asked the customer to DM their PayPal email address along with a screenshot of the email [#549659].

This is from 2017 Twitter support replies, and the reporting address or process may have changed since.

<details><summary>cited conversation #778256</summary>

```
Customer: AskPayPal received a phishing email pretending to be PayPal today! [link]
AskPayPal: Thank you for bringing this to our attention! If you'd like, you can report this email by forwarding it to __email__. From there, we'll be happy to take action! ^JGP
```
</details>

<details><summary>cited conversation #234241</summary>

```
Customer: AskPayPal got a very fishy email claiming to be from paypal, quite likely a phishing attempt, let me know where to forward that note
AskPayPal: Thank you for letting us know about this! Please forward that fake email to __email__. ^IVS
```
</details>

<details><summary>cited conversation #515646</summary>

```
Customer: I recieve at least 3 fake/phishing emails a week from “PayPal” where can I send them so they can be investigated and stopped?
AskPayPal: Hi there! Please forward those emails to __email__ so that we can take a look at them. We really appreciate it! :) ^KK
```
</details>

<details><summary>cited conversation #643580</summary>

```
Customer: Heads up pretty convincing *first glance* phishing / scam email being sent out. I hope people don’t fall for this scam. #paypal #scam #phishing AskPayPal [link]
AskPayPal: Good catch! Please forward it to __email__ so that we can archive it. Thank you so much! :) ^RA
Customer: AskPayPal I deleted it. I provided the information in the pictures. I’m sure if you send the tweet to your spoof people they can handle it. I’ve done my part.
AskPayPal: Alright! Have a great rest of your day. ^BC
```
</details>

<details><summary>cited conversation #2049</summary>

```
Customer: askpaypal It was really seems to sent from Paypal. #phishing [link]
AskPayPal: Hi, this is a fake email. Please forward it to __email__ and our team can look into it. Thank you for reaching out! ^ES
Customer: AskPayPal Hello, for your review. #phishing [link]
```
</details>

<details><summary>cited conversation #785275</summary>

```
Customer: AskPayPal phishing email received today. [link]
AskPayPal: Thank you for letting us know! That is definitely not from PayPal. Please forward this over to __email__ so that we can look into this further. ^AK
```
</details>

<details><summary>cited conversation #759752</summary>

```
Customer: Almost fell for this scam. , this link sent me to another phishing website where it tried to get all of my personal details using Google form manager. [link]
AskPayPal: Hi there! That definitely isn't a PayPal email. You can go ahead and forward the email to __email__ and then delete the email from your inbox. For more information on how to spot fake emails, please follow this link: [link] Thanks for reaching out! ^JMR
```
</details>

<details><summary>cited conversation #203418</summary>

```
Customer: received a strange email this morning, can you confirm that this is a phishing scam? [link]
Customer: Hi , please tweet AskPayPal and a member of our team will be able to help you with the email you've received.
AskPayPal: That's definitely a fake PayPal email. Please forward it to __email__ and then delete it. [link] ^DD
```
</details>

<details><summary>cited conversation #632766</summary>

```
Customer: Just received this very real looking phishing email from . Folks — beware the phishing emails! Don’t click on anything that seems suspicious! (I don’t have a UK account and there’s nothing on my actual PayPal account showing I made this “purchase”). [link]
Customer: When you check the address for “__email__,” you get this email address. [link]
AskPayPal: Hi Kristina, thank you for reporting this email. If you could please forward it to __email__ for verification or __email__ if you are sure it is a phishing email. You will find more information on phishing emails here [link] Thanks
AskPayPal: Sorry, I sent you the wrong link previously, it should be [link] Thanks
```
</details>

<details><summary>cited conversation #647228</summary>

```
Customer: Just received a scam email, with an email that looked legitimate. Thankfully my phone tells me ‘other’ emails. Do not click links in an email if it looks off. PayPal would never email you saying ‘Dear Client’, they’ll refer to you by name. [link]
Customer: Forward it to __email__ - no need to write anything - and it will help them to work out where these scams originate from
Customer: Already done
AskPayPal: Hey guys! Our spoof/phishing team will look it over from here. Thanks for bringing this to our attention and have a great day! ^DP
```
</details>

<details><summary>cited conversation #549659</summary>

```
Customer: AskPayPal Keep getting an email asking to verify my information, keep sending it to the spoof report but I dont know if its fake or not?
Customer: AskPayPal Had the same email 3 times today
AskPayPal: Hello! Could you please DM us your PayPal email address along with a screenshot of the email? We'd be happy to he... [link]
```
</details>

## q092

**Question:** Will FedEx leave my package with a neighbour if I'm not home?

**Reference:** Not covered: FedEx isn't in the corpus. The assistant must not substitute UPS's delivery policies.

**System answer:**

The support history doesn't answer this. FedEx isn't one of the companies in these Twitter conversations, and no FedEx agent said whether a driver will leave a package with a neighbour if you're not home. Mentions of FedEx are only from customers comparing other carriers; those aren't FedEx's own policy. I can't use UPS or Amazon's answers in place of FedEx.

_(no conversations cited)_

## q096

**Question:** How do I cancel my Disney+ subscription?

**Reference:** Not covered: Disney+ launched in 2019, after this 2017 dataset.

**System answer:**

The 2017 Twitter support history does not include Disney+ or any company agents explaining how to cancel a Disney+ subscription. Disney+ is not one of the companies in this archive, and searches only turn up cancellation steps for unrelated services (PlayStation, Adobe, Google Play Music, and others). Those policies cannot be used in place of Disney+ instructions.

_(no conversations cited)_

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

## q047

**Question:** Hulu shows error runtime-2 on my PS4 after a few minutes of playback. What should I do?

**Reference:** hulu_support suggested restarting the device and following their troubleshooting link. The customer found the problem was limited to one season of a show.

**System answer:**

In the 2017 conversation that matches this PS4 runtime-2 playback error, the Hulu agent told the customer to do a quick restart of the device and also open a linked page. The thread doesn’t include what that page said, so those extra steps aren’t known from the history. If the error kept happening, the agent asked them to send a photo of the error for reference [#698161]. This is from November 2017 and may have changed since.

<details><summary>cited conversation #698161</summary>

```
Customer: hulu_support I keep getting this error. Tried googling it, no troubleshooting comes up. Help? runtime-2-15e4530e
hulu_support: Is the error appearing on your PS4, or are you accessing our app from a different device now? When exactly does it pop up?
Customer: hulu_support Whoops, forgot to mention, it's my PS4. I have season 20 of South Park on, it plays for about 2-3 minutes, starts to buffer for a while, then the screen goes black with that error.
hulu_support: Gotcha! Try a quick restart of your device as well as: [link] Any improvement after that? Let us know!
Customer: hulu_support I restarted it prior to messaging you, as if it were something that silly, I didn't want to bother you with it. It seems like it's just that season, as I moved to another and haven't had an issue yet.
hulu_support: Interesting... 🤔 If you do happen to run into more trouble please snap a pic of the error and send it our way for reference.
```
</details>

## q100

**Question:** What is the time limit on free Zoom meetings?

**Reference:** Not covered: Zoom isn't in the corpus.

**System answer:**

The customer-support history does not answer this. Zoom is not one of the companies in the 2017 Twitter support archive, and searches for free Zoom meeting time limits only turned up unrelated mentions of display zoom, hold times, and other companies’ policies. Nothing in the agent replies states a time limit for free Zoom meetings.

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

## q012

**Question:** The Spotify web player has been stuck playing one song silently for hours. How do I fix it?

**Reference:** SpotifyCares suggested clearing the browser's cache and cookies or trying an incognito window. The customer found refreshing the tab fixed it.

**System answer:**

In 2017, Spotify support’s advice for a web player stuck silently on one song was to clear the browser’s cache and cookies, and if that doesn’t help, try an incognito window [#170615].

For similar cases where the web player was stuck on a song that wouldn’t play, or the play button did nothing, agents also suggested logging out and back in [#108372], opening the web player in an incognito or private window [#108372][#166748][#244649][#797101], trying a different browser [#244649], restarting the router [#108372], and restarting the computer [#108372]. In one web-player case where a track kept going with no sound, an agent suggested uninstalling and reinstalling the app; after the customer said the app was working, the agent replied that if it’s working on the app, that’s fine [#779356].

This is what Spotify agents said in 2017 and may not match current behavior.

<details><summary>cited conversation #170615</summary>

```
Customer: Evidently, has been silently playing one 4 minute song for the past 6 hours. Lemme guess, it's not a bug it's a feature? [link]
SpotifyCares: Hi Renee! Can you try clearing your browser's cache/cookies? If that doesn't help, try using an incognito window /RH
Customer: SpotifyCares All I had to do was refresh the tab. Thanks though!
SpotifyCares: Awesome, thanks for letting us know. Enjoy the music! [link] 🙂 /BH
```
</details>

<details><summary>cited conversation #108372</summary>

```
Customer: Hey SpotifyCares as of yesterday I can't play music on any computer or browser. It's stuck on one song (that doesn't play). Please help :(
Customer: SpotifyCares I'm using the web player and have tried Chrome and Firefox on Windows 7 and Chrome on Mac OSX
SpotifyCares: Hey Elizabeth! Does logging out and back in help? If you're getting an error message, a screenshot of it would be great /CX
Customer: SpotifyCares No. No error message either. This is my screen. Whatever I click the play bar is stuck on that song. [link]
Customer: SpotifyCares Have also tried clearing all my cookies but it made no difference.
SpotifyCares: Could you try restarting your router? Using the web player on Chrome's incognito window is also worth checking /CX
Customer: SpotifyCares I've tried incognito to no avail. I can't restart the router as I'm on a shared network in a university. Had the same problems at...
Customer: SpotifyCares ...home last night so I'm not sure if it's a network problem. Could try later this evening though.
SpotifyCares: Sounds like a plan. In the meantime, you can try restarting your computer to see if it'll make it work /CX
```
</details>

<details><summary>cited conversation #166748</summary>

```
Customer: My Spotify web player isn't working and it's stuck on this add it lets me click songs and everything but it won't play it.SpotifyCares
SpotifyCares: Hi Kae! That doesn't sound good. Can you try opening the web player in an incognito/private window? Let us know how it goes /RK
```
</details>

<details><summary>cited conversation #244649</summary>

```
Customer: #bug (web player) this happens pretty often. Play button does nothing. Reloading fixes it. [link]
SpotifyCares: Hey Matteo! Can you let us know what device, operating system, and Spotify version you're using? We'll see what we can suggest /CH
Customer: SpotifyCares web player, Google Chrome on Linux (OS irrelevant).
SpotifyCares: 1: Thanks for the info. Just a heads up, we don't officially support Linux but we'll try our best to help you get this fixed. Have...
SpotifyCares: 2: you tried using a different browser or an incognito window? Let us know how it goes /ME
Customer: SpotifyCares The OS is irrelevant, this is on a browser. Happens systematically when opening web player after several hours since last time.
Customer: SpotifyCares I think it has to do with "remembering" the song that was playing last time
SpotifyCares: Got it, but we might have limited troubleshooting with your OS. By the way, have you tried using a different device? Does this help? /ME
Customer: SpotifyCares Haven't tried. It takes time, need to log in, play something, close browser window, wait a few hours, open web player again.
Customer: SpotifyCares and I usually use only my PC. Try and let me know if you cannot reproduce on Windows or Mac, I'm pretty sure it's not OS-dependent.
SpotifyCares: Looks like everything is clear from our end using Windows, so let's try to cover all bases. Can you DM us your account's email address? /ME [link]
Customer: SpotifyCares Did you follow all steps to test, including waiting several hours without logging out?
Customer: SpotifyCares I mean closing the browser tab but without logging out (nor clearing cookies)
```
</details>

<details><summary>cited conversation #797101</summary>

```
Customer: Hey any actual true and honest solution on the web player getting stuck with a non playing ad? Been trying for hours. 😐
Customer: SpotifyCares
SpotifyCares: Hey there, that doesn't sound right. Can you try giving the web player another go in an incognito or a private browsing window? Let us know how it goes /SY
```
</details>

<details><summary>cited conversation #779356</summary>

```
Customer: SpotifyCares hey there, so i'm playing a playlist and then denzel curry - ultimate comes on and plays, but the song keeps "playing" after the song is over. the song was supposed to be over at 3:09 but it's now at 25:15 with no sound or anything and i can't pause or skip. pls hlp
SpotifyCares: Hey there! Could you let us know what device/OS you're using? We'll see what we can suggest /DF
Customer: SpotifyCares i'm using the web player on the website on windows 7 64 bit. i also tried logging out and back in and that did nothing.
SpotifyCares: Hmm. That's odd. Could you try uninstalling and reinstalling the app? Let us know how it goes /DF
Customer: SpotifyCares i wasn't using the app, i was using the web player. but i will try the app and see what's up there and see if it's still not working on there.
Customer: SpotifyCares the app works. so i'll just use that. that is weird though, that glitch i had never happened before. anyways, thanks for your help! have a good day!
SpotifyCares: Thanks for letting us know. If it's working on the app, then that's cool. But if it ever comes up again, or if you could try it again and send over a screenshot, that'd be cool. In any case, you know where to find us if you ever need help with anything else /QI
```
</details>
