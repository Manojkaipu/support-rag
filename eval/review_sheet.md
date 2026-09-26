# Evaluation set review

For each question: check that the question is natural, the reference answer only says what the company said, and the gold conversations really answer it. Set `review` in questions.jsonl to `approved`, `edited` (after fixing it) or `rejected`.

## q001 · AmazonHelp · policy

**Q:** I forgot to cancel my Amazon Prime free trial and got charged. Can I get that money back?

**Reference:** AmazonHelp said that if you haven't used any Prime benefits since the charge you get a full refund; otherwise the refund is pro-rated. They linked the help page for cancelling the membership.

<details><summary>gold conversation 249833</summary>

```
Customer: forgot to cancel my free trial of amazon prime and it just charged me $100 ummm fuck
AmazonHelp: I'm sorry for the unexpected charge! Here's a link to our Help page on how to cancel the membership: [link]
Customer: AmazonHelp can u reverse the charge tho
AmazonHelp: If you haven't used the benefits since being charged, you'll receive a full refund. Otherwise, it will be pro-rated. ^AM
```
</details>

## q002 · AmazonHelp · howto

**Q:** Our Amazon merchant account was suspended. Who are sellers supposed to contact?

**Reference:** AmazonHelp directed merchants to the Seller Support team through a help link rather than the consumer support account.

<details><summary>gold conversation 100580</summary>

```
Customer: Our account was suspended for no logical reason. No response from you in days despite repeated requests for help.
AmazonHelp: Hey, sorry to hear about the trouble! W/o providing personal or acct specific info, can you tell us more? ^LB
Customer: AmazonHelp Thanks. Can you give me a human being to call to discuss? We are a merchant. Unbelievable that no number for merchants to call for help.
AmazonHelp: You can reach out to our Seller Support team here: [link] They'd be happy to help! ^ZW
Customer: AmazonHelp I've contacted them many times via our AmazonPay Account. Just get forwarded to another dept. No # for merchants in good standing to call?
Customer: AmazonHelp How can merchants trust you to process payments if you arbitrarily suspend long-term accounts in good standing &amp; then disappear?
AmazonHelp: What department are we stating we've forwarded your concern to? Have we provided a time frame for follow up? ^RA
Customer: AmazonHelp It's the team. Yes, they were supposed to respond by yesterday.
Customer: AmazonHelp What happens is that every support department refers us to someone else. Round and round it goes. do you care about merchants?
AmazonHelp: Please provide as much info as possible here: [link] so a member of our Social Media team can look into this.^ZW
Customer: AmazonHelp OK. Filled it out. Hopefully, a real human can now contact me to discuss. Hard to believe can't provide support for merchants.
AmazonHelp: Thank you for the update! I have confirmed that we have received the information you sent. Someone will be in touch soon! ^AL
```
</details>

## q003 · AmazonHelp · howto

**Q:** Quel est le numéro du service client d'Amazon en France ?

**Reference:** AmazonHelp confirmed 0 805 10 14 20 as the Amazon France customer service number.

<details><summary>gold conversation 162376</summary>

```
Customer: Bonjour un de mes colis n’est toujours pas arrivé (prévu le 6/10 puis 11/10), possible d’avoir une explication ? Merci AmazonHelp [link]
AmazonHelp: Bonjour, désolée d'apprendre cela. Quel est le transporteur en charge de la livraison? ^MD
Customer: AmazonHelp D’après votre site (et mon imp écran ^^) c’est La Poste. En me rendant sur leur site, le colis n’a pas bougé depuis le 01. [link]
AmazonHelp: Avez-vous contacté notre SAV dans ce sens ?^AR
Customer: AmazonHelp Le numéro est bien : 0 805 10 14 20 ?
AmazonHelp: C'est bien celui là.^FT
Customer: AmazonHelp C’est bon, j’ai eu un de vos conseillers. Commande annulée + remboursée \o/ Merci ;)
AmazonHelp: Parfait, je vous en prie.^FT
```
</details>

## q004 · AppleSupport · incident

**Q:** Since the latest iOS update my iPhone keeps replacing the letter 'i' with a strange symbol. Is Apple fixing this?

**Reference:** AppleSupport said it would be fixed in a future software update and shared a workaround article (a text replacement) to use until then. The customer said the workaround didn't help and AppleSupport moved to DM.

<details><summary>gold conversation 469466</summary>

```
Customer: better come out with a new software update soon....it’s kinda tough to communicate without the letter “i”
AppleSupport: Here’s what you can do to work around the issue until it’s fixed in a future software update: [link]
Customer: AppleSupport Thanks- I did the replacement text and it didn’t solve the issue
AppleSupport: Understood. Let's continue in DM. Send us a message and we'll follow up there. [link]
```
</details>

## q005 · AppleSupport · troubleshooting

**Q:** After updating to iOS 11 the Phone app on my iPhone only shows a blank screen. What should I try?

**Reference:** AppleSupport suggested force-closing the Phone app, restarting the iPhone and opening it again. When that didn't work they asked whether it started with the update and recommended making a current iCloud or iTunes backup before further steps.

<details><summary>gold conversation 767041</summary>

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

## q006 · Uber_Support · policy

**Q:** If I schedule an Uber ride in advance, am I guaranteed a driver?

**Reference:** No. Uber_Support said scheduling doesn't guarantee a driver; if none can be found you're notified at the end of your selected 15-minute window.

<details><summary>gold conversation 500540</summary>

```
Customer: used the Uber schedule ride feature for the first time, booked a cab 2 days ago and guess what....Let me down
Uber_Support: Here to help! Scheduling a ride in advance does not guarantee you'll be connected with a driver. In the rare case that a driver cannot be found, you'll be notified at the end of your selected time window of 15 minutes. For more info on this, click here; [link]
Customer: Uber_Support Might be there first and last time I use this
```
</details>

## q007 · Uber_Support · howto

**Q:** How do I complain about a rude Uber Eats delivery person?

**Reference:** Uber_Support said to tap the 'Help' button in the app; if you've already done that, DM them your account email so they can follow up.

<details><summary>gold conversation 526444</summary>

```
Customer: My UberEATS delivery guy was a total dick. 😡
Uber_Support: That's not what we like to hear. Please tap the "Help" button in the app and we can look into this.
Customer: Uber_Support I already did that.
Uber_Support: We can definitely take a look! Send us a DM with your email address so we can follow up.
```
</details>

## q008 · Uber_Support · incident

**Q:** Why couldn't I get the free Krispy Kreme dozen on Uber Eats?

**Reference:** Uber_Support said a technical issue caused by high demand was affecting orders, and later that demand was so high the free Original Glazed dozens ran out. They said to watch for future promotions.

<details><summary>gold conversation 561035</summary>

```
Customer: HOW COULD YOU DO THIS TO ME WHILE I'M ON MY PERIOD 😭😭😭😭😭 [link]
Uber_Support: We're sorry, and we're working hard to sort a technical issue caused by high demand. Please doughnut worry, there will still be plenty of time to order. If you're not immediately connected, do try again.
Customer: Uber_Support I don't think you understand how much I've been trying all this time.. My resolve is weak, and my menstrual flow is heavy, is denying me freebies from .. Mom's spaghetti #KrispyKreme #UberEats #AtTheMercyOfMyUterus
Customer: Uber_Support AND I BARELY EVEN USE TWITTER! 😫
Uber_Support: We're so sorry you didn’t get your FREE Original Glazed Dozen box. Demand was through the roof. Stay tuned for more fun promotions soon!
```
</details>

## q009 · Uber_Support · policy

**Q:** My friend left her phone in an Uber and can't log in to her account. Can I contact the driver for her?

**Reference:** Uber_Support said that due to its privacy policy it must speak directly to the account holder, who should contact Uber through the help link or DM the email address on the account.

<details><summary>gold conversation 727394</summary>

```
Customer: my mate has left her phone in one of your cabs but obvs can't get the drivers details and can't get the log in verification code! Please help! I have the drivers name ....
Uber_Support: Due to our privacy policy, we will have to speak directly to the account holder. Please have them contact us via [link]
Customer: Uber_Support Tried this no one calls!
Uber_Support: Here to assist, Shiarra! Please DM us the email address associated with the account holder to look further into this.
Customer: Uber_Support Have done thanks
Uber_Support: We've responded via DM!
Customer: Uber_Support Still nothing from you
Customer: Uber_Support Your service is really not good!
Uber_Support: We have followed up via DM.
```
</details>

## q010 · SpotifyCares · howto

**Q:** Spotify put an album by a different artist with the same name on my favourite band's page. How do I report it?

**Reference:** SpotifyCares asked for the album's Spotify URI (right-click the album > Share > URI) so they could correct the artist page.

<details><summary>gold conversation 8741</summary>

```
Customer: SpotifyCares you added an incorrect album to this artists page - this is Lydia (band, USA) and the album is from Lydia (singer, Japan) [link]
SpotifyCares: Hey, help's here! Can you send us the Spotify URI? Just right-click the album &gt; Share &gt; URI? Keep us posted /JS
Customer: SpotifyCares went to check and it's sorted itself out (Y)
SpotifyCares: Awesome, we're glad it's looking good! If you ever need anything else, just shout and we'll come running 🏃 /JX
```
</details>

## q011 · SpotifyCares · product

**Q:** On Spotify Free on my Android phone I can't pick a specific song, it just shuffles. Is that a bug?

**Reference:** No. SpotifyCares explained that on the Free tier you can't stream specific songs on demand on mobile; Free is ad-supported and shuffle-only on mobile devices.

<details><summary>gold conversation 137373</summary>

```
Customer: I wanted to play 's new song but Spotify app won't let me and I'm super annoyed lol
SpotifyCares: Hi Mara! What device, operating system, and Spotify version are you using? Are you getting any error messages? A screenshot can be handy /AU
Customer: SpotifyCares Hi, my device is HUAWEI and an android. Earlier it wouldn't let me play the song and shuffles albums from other artists instead and now (c)
Customer: SpotifyCares I get this message when I try to play anything at all. I screenshot the version and the mesaage: [link]
SpotifyCares: 1: Thanks. Looks like you're on Free. This means you can’t stream specific songs on demand. You also get ad-supported, shuffle-only... /AU
SpotifyCares: 2: access on mobile devices. For more info, click here: [link] /AU
Customer: SpotifyCares I don't mind the shuffle feature but not being able to play songs is a bit futile in terms of having the app. Thanks for the help tho!! 😊
SpotifyCares: We appreciate your feedback. Rest assured, we'll pass it on to the right folks. If there's anything else, just give us a shout 🙂 /AU
```
</details>

## q012 · SpotifyCares · troubleshooting

**Q:** The Spotify web player has been stuck playing one song silently for hours. How do I fix it?

**Reference:** SpotifyCares suggested clearing the browser's cache and cookies or trying an incognito window. The customer found refreshing the tab fixed it.

<details><summary>gold conversation 170615</summary>

```
Customer: Evidently, has been silently playing one 4 minute song for the past 6 hours. Lemme guess, it's not a bug it's a feature? [link]
SpotifyCares: Hi Renee! Can you try clearing your browser's cache/cookies? If that doesn't help, try using an incognito window /RH
Customer: SpotifyCares All I had to do was refresh the tab. Thanks though!
SpotifyCares: Awesome, thanks for letting us know. Enjoy the music! [link] 🙂 /BH
```
</details>

## q013 · SpotifyCares · howto

**Q:** How do I hide the Find Friends panel in the Spotify app on my Mac?

**Reference:** Click View and uncheck Right Sidebar.

<details><summary>gold conversation 369000</summary>

```
Customer: How do we hide this “Find Friends” window on the Mac app? I don’t use it and it’s a waste of space.
SpotifyCares: Hey Michael! You can hide that section by clicking View &gt; unchecking Right Sidebar. If there's anything else, just give us a shout /RH
Customer: SpotifyCares Thanks!
SpotifyCares: You're welcome! Stay awesome /KL
```
</details>

## q014 · SpotifyCares · product

**Q:** Songs I listen to every day suddenly disappeared from Spotify and my playlist. Why?

**Reference:** SpotifyCares said content is sometimes temporarily removed because of licensing changes and hopefully will be available again soon.

<details><summary>gold conversation 596210</summary>

```
Customer: SpotifyCares Howcome Swiss Army and Places are no longer on Spotify?
Customer: SpotifyCares oh and shade of poison trees is missing too. It was on yesterday, what's happened?
SpotifyCares: Hey! Sometimes content gets temporarily removed because of licensing changes. Hopefully we'll have it available again soon /DF
Customer: SpotifyCares Okay, thanks for getting back to me :)
SpotifyCares: No worries! If you need anything else, just shout and we'll come running /DF
```
</details>

<details><summary>gold conversation 673533</summary>

```
Customer: Yo! where did my netnobody tracks go? Why can't I listen to them and why was it deleted from my playlist? That's bot cool, I listen to those songs daily, and you just wanna ruin my day?
SpotifyCares: Hey there! Sometimes content gets temporarily removed because of licensing changes. Hopefully we'll have it available again soon /NQ
Customer: SpotifyCares Well I really wanted to show it to a friend but it was gone
SpotifyCares: We understand. Fingers crossed we'll be able to have it again soon, but there's info about Spotify content here: [link] For anything else, let us know /GU
```
</details>

## q015 · SpotifyCares · troubleshooting

**Q:** Spotify's Your Time Capsule keeps showing an error message even though I listen every day. What's wrong?

**Reference:** SpotifyCares said to keep listening to songs you love and make sure you're not in a Private Session, giving Spotify time to learn your taste.

<details><summary>gold conversation 723468</summary>

```
Customer: this is still an issue help SpotifyCares [link]
SpotifyCares: Hey! You can find Your Time Capsule at [link] We'd also suggest following it to keep it saved 🙂 /MG
Customer: SpotifyCares I use spotify every day and this is the message i’ve been getting every time i’ve clicked the link in the past two months [link]
SpotifyCares: Sorry to hear that. Carry on listening to the songs you love, making sure you’re not in a Private Session. This should give us a little time for us to get to know you. Let us know if you have other questions /MG
```
</details>

## q016 · Delta · policy

**Q:** Delta still hasn't found my delayed bag. Can I get reimbursed for things I buy in the meantime?

**Reference:** Yes. Delta said you can use the delayed-bag file you created to be reimbursed for purchases made while waiting for the bag.

<details><summary>gold conversation 246100</summary>

```
Customer: Delta "... due to extreme weather events, you can expect to receive substantive response from our office w/in 30 days." THIS DOESNT CUT IT
Delta: I'm sorry that your bag has been delayed for so long. So far, there's no new info on the bag, but we're working hard to find it &amp; get... 1/3
Delta: ...the bag's arrival. *HWG 3/3
Delta: ...it back to you quickly. In the meantime, you can use the file you created to be reimbursed for your purchases while waiting on... 2/3
```
</details>

## q017 · Delta · policy

**Q:** My Delta account got locked after too many failed login attempts. How do I get back in?

**Reference:** Delta said the account stays locked for 24 hours after the last failed attempt; after that you can try again, but more wrong attempts will lock it again.

<details><summary>gold conversation 317108</summary>

```
Customer: delta my delta acc has been disabled due exceed login attemp is there a way to re enabled my acc ? Thx
Delta: Unfortunately, the account will be locked for 24 hours after your last failed login attempt. *AJY
Customer: Delta Ok, so after that 24 hrs it will automatically unlock right?
Delta: Yes, you can try it again in 24 hours. Unfortunately, too many wrong attempts will lock you out. *TAY
```
</details>

## q018 · Delta · howto

**Q:** My suitcase came off a Delta flight ripped to shreds. How do I file a claim?

**Reference:** Delta sent a claim form (completing it gives you a file reference number). When the form wouldn't submit, they said to call Baggage Service at 1-800-325-8224, open 24/7, to file the claim.

<details><summary>gold conversation 328704</summary>

```
Customer: Delta my bag has tire marks all over it and was ripped to shreds. How do I get a new bag? [link]
Delta: So sorry to hear this. Please fill out the attached form to start a claim. [link] *AJY
Customer: Delta I don’t have a file reference number? Now what?
Delta: Hello, David. Once you complete the form, you will get a file reference number. *TAY
Customer: Delta It won’t let me hit next?? [link]
Delta: You can call Baggage service at 1800 325 8224 and file a claim with them they are open 24/7. They will be happy to assist you. *TAY
```
</details>

## q019 · Delta · howto

**Q:** Miles from one leg of my Delta trip vanished from my SkyMiles account. What can I do?

**Reference:** Delta agents resubmitted the flight for credit and sent a review request to the SkyMiles team, promising an update.

<details><summary>gold conversation 346777</summary>

```
Customer: delta Seems as though miles from a previous leg of my journey (LHR &gt; ATH) have disappeared from my account. Can you please advise?
Delta: Hi, Chris, it has been pending and should have posted by now. I have resubmitted it for credit for you. I apologize for the delay. *TRR
Customer: Delta Thank you. And apologies - it was JFK &gt; ATH. Miles were in there last week but no longer after yesterday's flight (delayed DL2 from LHR)
Delta: GM Chris. I will submit the request to our SkyMiles team for review. As soon as I have an update, I will provide it to you. *ALS
```
</details>

## q020 · Delta · howto

**Q:** How do I file a discrimination complaint with Delta about how a passenger was treated?

**Reference:** Delta said it does not condone discrimination and pointed to an online complaint form handled by its discrimination specialists.

<details><summary>gold conversation 404321</summary>

```
Customer: One of my dearest friends on a flight this morning! Never flying Delta cc: [link]
Delta: Hello! Thank you for the details. We will certainly look into this. Delta does not discriminate (cont...) *HKS
Delta: or condone discrimination of a person or group for any reason. As a global carrier with a diverse workforce, (cont...) *HKS
Delta: serving a diverse customer base, we are committed to treating all passengers equally. *HKS
Delta: Thank you for your patience. If you haven't already done so. (cont...) *HKS
Delta: ...investigate. *HKS 2/2 [link]
Delta: You can file a complaint online via the following link [link] and one of our discrimination specialist will... 1/2
```
</details>

## q021 · AmericanAir · policy

**Q:** I booked an American Airlines flight with miles and need to cancel. Why am I being charged a fee?

**Reference:** American charges a fee to reinstate miles into your account (the customer was charged $175).

<details><summary>gold conversation 65505</summary>

```
Customer: AmericanAir i used miles for a flight and now need to cancel yet I’m being charged $175. #WTH #poorcustomerservice
AmericanAir: There is a charge to reinstate mileage into your account. Our apologies for any frustration.
Customer: AmericanAir I don’t understand this policy... I shouldn’t be charged for miles I haven’t used. #IMHO
```
</details>

## q022 · AmericanAir · policy

**Q:** American rebooked me because I'll miss my connection at DFW. Will my checked bag follow me to the new flight?

**Reference:** American said the bag was loaded and should transfer with you, and that you can track its location through their bag-tracking link.

<details><summary>gold conversation 267407</summary>

```
Customer: AmericanAir going to miss my conn flight at DFW from FAR because we were sitting on the runway too long. Now have to refuel. Let's talk.
AmericanAir: We'll do our best to have you airborne soon, Marc. We've backed you up on flight 2216 just in case you miss it.
Customer: AmericanAir See that in the app now, thanks. Please confirm that checked baggage will also transfer.
AmericanAir: Your bag was loaded onto your flight and should transfer with you. You can keep track of it's location here: [link]
```
</details>

## q023 · AmericanAir · policy

**Q:** American Airlines moved me out of the Main Cabin Extra seat I paid for. Do I get a refund?

**Reference:** American said it sometimes has to make last-minute seat changes and would refund the Main Cabin Extra charge after travel is complete.

<details><summary>gold conversation 591816</summary>

```
Customer: Leave tonight for BCN wedding anniversary trip. Booked in August for Main Cabin Extra and notice today has been changed by AmericanAir without any notification - I noticed it on my app. Boarding pass yesterday has MCE. Today, no! #fixit #AAcustomerservicesucks #makeitright
AmericanAir: We do our best to keep your seats as booked, but we may have to make last minute changes. We'll refund you after travel is complete.
Customer: AmericanAir Nice! And next time we will fly Iberia, Air France or British Airways as we should have done, to begin with. What were we thinking? Plus, your refund doesn't give back the 6 inches I am losing that I paid for. I will also use others for my corporate travel as I have been.
```
</details>

## q024 · TMobileHelp · product

**Q:** Can T-Mobile alert me when I've used half of my monthly data?

**Reference:** TMobileHelp suggested tracking data usage in the T-Mobile app and offered help by DM. They did not mention a 50% alert; the customer only got alerts at 80% usage.

<details><summary>gold conversation 111463</summary>

```
Customer: it would be so great if I got a message saying that I’ve used half of my data . I never get those.
Customer: I only get a message when I use 8/10 of my gigs 🙄
TMobileHelp: You can stay up to date with your data usage using your T-Mobile App. Send us a DM for assistance on how to access this feature. *JasmineS
```
</details>

## q025 · comcastcares · howto

**Q:** My Comcast cable box died. Can I just swap it at an Xfinity store?

**Reference:** Yes. comcastcares said you can swap it out at the service center.

<details><summary>gold conversation 223814</summary>

```
Customer: comcastcares I think my cable box finally died. Can I go to my nearest Xfinity store and swap it for a new one?
comcastcares: You can totally swap it out at the service center. Do you need the address of the nearest one? -JN
Customer: comcastcares Nope, I know where it is... Thanks!
comcastcares: Not a problem. If you need anything else, don't hesitate to reach back out. -JN
```
</details>

## q026 · comcastcares · incident

**Q:** Was the recent Comcast internet outage caused by Level 3?

**Reference:** comcastcares said there was a known issue with Level 3 earlier that caused problems and that it had been resolved.

<details><summary>gold conversation 455872</summary>

```
Customer: Dear - why do we have to have daily service outrages? It is ridiculous, for what we pay... #comcastfail
comcastcares: Hello, I can look into you service issues. Please send me a DM with account details to get started. Thanks so much. -NC
Customer: comcastcares I sent a DM, any reply? or updates? Service is back, for the moment, but it is really ridiculous the frequency. Thanks.
comcastcares: I do not see a DM, is the issue just with internet? -NC
Customer: comcastcares Check again, I sent it a few hours ago in response to your request for a DM with account info to validate who I am. Yes, only internet.
comcastcares: Are you still having issues? We did have a known issue earlier with Level 3, which caused problems but it has been resolved now. -NC
```
</details>

## q027 · comcastcares · policy

**Q:** Why can't I watch the OSU vs Wisconsin game on my phone with Comcast?

**Reference:** comcastcares said that due to licensing agreements the game wasn't available on mobile devices.

<details><summary>gold conversation 815737</summary>

```
Customer: I worked my ass off to get Comcast live on my phone and you dick heads have the balls to tell me I can’t watch OSU-Wisconsin?
comcastcares: I can look into why you cant watch the OSU-Wisconsin game. Please DM me your account info so I can help. -GR
Customer: comcastcares This!!!! [link]
comcastcares: Due to licensing agreements, the game will not available on your mobile ​device. Apologize for the inconvenience. -ZC
```
</details>

## q028 · SouthwestAir · policy

**Q:** Southwest cancelled my flight and the website won't let me rebook. Will changing it cost me anything?

**Reference:** SouthwestAir said they could rebook the customer at no charge and asked for the confirmation number by DM.

<details><summary>gold conversation 98027</summary>

```
Customer: Hey SouthwestAir! You cancelled my flight from SFO to LAX. I'm trying to rebook but your website / app aren't allowing it.
Customer: SouthwestAir I've called your 800 number but it is saying 52 minutes. I'm trying to rebook faster than that for a flight out of OAK.
SouthwestAir: Our apologies for the difficulty, Jana! We can get you rebooked out of SFO at no charge. Please DM your flight confirmation number. ^JB
```
</details>

## q029 · SouthwestAir · incident

**Q:** My Southwest flight to Las Vegas is delayed but a later flight to the same city is boarding first. Why?

**Reference:** SouthwestAir said the delay was due to air traffic control (ATC) directives and that departure times are based on those directives.

<details><summary>gold conversation 327334</summary>

```
Customer: Ugh 3 hour #delay from #LAX to #LAS! No advanced notice until after boarding time! What’s up with that, SouthwestAir ?!
SouthwestAir: We know how frustrating last minute delays can be, Phoebe. Send us your flt number and city pairs so we can look further. ^MS
Customer: SouthwestAir 10/28 LAX to LAS flight #3292
SouthwestAir: It looks like Flt #3292 is delayed until 12:25 due to ATC directives. Rest assured we're working on getting you out soon. ^MS
Customer: SouthwestAir Thank you! But why is a later flight, LAX to LAS #5930 boarding before ours?
SouthwestAir: Apologies. Please know we're working hard to get you to Las Vegas, but departure times are still based on ATC directives. ^MS
```
</details>

## q030 · SouthwestAir · product

**Q:** Does Southwest notify you when fares drop on a route you're watching?

**Reference:** No. SouthwestAir said it has no fare-decrease notifications, but you can sign up for Click 'N Save emails for alerts on its best deals.

<details><summary>gold conversation 633633</summary>

```
Customer: SouthwestAir Does SWA have a notification program when flights go down in price. We are flying from GSP to New Orleans next Summer. If so is there a link to sign up. Thanks.
SouthwestAir: Hey Don - We don't have that type of notification system for decreases in fares, but be sure to sign up for Click 'N Save for alerts on our best deals: [link] ^KM
Customer: SouthwestAir Thanks, I will do that.
```
</details>

## q031 · Ask_Spectrum · policy

**Q:** Why doesn't the NBC Sports app work with my Spectrum account on Fire Stick?

**Reference:** Ask_Spectrum said this is due to distribution agreements between Spectrum and NBC Sports.

<details><summary>gold conversation 318789</summary>

```
Customer: Ask_Spectrum any particular reason the nbc sports app doesn’t work on multiple devices? Love seeing my rates go up for less content
Ask_Spectrum: We would be more than willing to take a closer look ito any streaming issues you're having, Brandon. What error m... [link]
Customer: Ask_Spectrum The failure would be that the app is unavailable to charter users on fire stick. Pretty sure there isn’t much you can do about that
Ask_Spectrum: This would be due to distribution agreements between us and nbc sports. Our apologies as your assumptions are cor... [link]
```
</details>

## q032 · Tesco · howto

**Q:** Tesco asked for the SC code on a product so they can refund me. What is it and where do I find it?

**Reference:** It's the supplier code. One agent said it begins 'SC' and is near the barcode; another described it as a 4-6 digit number next to Tesco's address.

<details><summary>gold conversation 188707</summary>

```
Customer: Oh that’s cheeky!!! eggs bought got home and one had been taken out from behind the label!!! #Thecheekofit Tesco [link]
Tesco: Oh no Sarah, I'm sorry for the inconvenience caused. Are you able to return for an exchange? If not, I can refund you from here.Thanks, Leah
Customer: Tesco Thank you for your reply. No unfortunately I needed them so couldn’t return I’m afraid
Tesco: Hi Sarah. No worries I'll refund you from here. Can you please DM me the following information please? 1/2
Tesco: The store you bought these from, the SC code, your full name, address and email. Would you like a refund via email or post? TY-Charlotte 2/2
Customer: Tesco Hi the were bought from Tesco extra Huddersfield road, Oldham
Customer: Tesco What is an sc code please ?
Tesco: Hi Sarah, it's the supplier code. It begins 'SC....' and is located near the barcode. Thanks - Lara.
```
</details>

<details><summary>gold conversation 401202</summary>

```
Customer: I'm really upset because I just went to have some orange juice with bits in and NO JUICY BITS TO BE SEEN ☹️ thanks Tesco
Tesco: Hi Hayley, Oh no! You can't have orange juice with out the best bit, I'm sorry about that I would have been devastated myself! 1/4
Tesco: Could I get your full name (with title), address, email address, barcode, supplier code, date code, price and store you bought it from? 3/4
Tesco: Could you please DM me with some details and I'd be more than happy to feed this back to our suppliers and also get you fully refunded? 2/4
Tesco: Are you ok with me passing your details on to our suppliers? Also would you prefer to be refunded via email or via post? Thanks, Calum 4/4
Customer: Tesco How would I find some of those details?
Tesco: Hi Hayley. The barcode is on the side of the carton. The Supplier code's a 4-6 digit number located next to Tescos address (e.g. SC1234) 1/2
Tesco: The date code should be on the lid or the neck of the carton. :) - Alisha 2/2
```
</details>

## q033 · Tesco · policy

**Q:** I bought a faulty product at Tesco but can't take it back to the store. Can I still get a refund?

**Reference:** Yes. Tesco can refund from Twitter: DM your name, address and email plus product details (barcode, supplier code, store), choose a refund by email or post, and they may pass your details to the supplier.

<details><summary>gold conversation 217123</summary>

```
Customer: Tesco What's happened to your bin bags,every one has ripped down the side,I've had to sellotape it.The grey tab comes out too when I tie it [link]
Customer: Tesco Is this just a bad batch? All the others have been good quality, but these bags are all attached together, but they didn't used to be.
Tesco: I'm so sorry the bags you have purchased from our store have split down the side. I'd be just as disappointed. 1/4
Tesco: I'd like to ensure that this is looked into by our suppliers &amp; also arrange a full refund for you. 2/4
Tesco: Could you DM us with your name, your full address &amp; email? Please can you also confirm if you'd like a refund via the post or email? 3/4
Tesco: Lastly, are you happy for your details to be passed to our suppliers? They may want to contact you. -Rocsi 4/4 [link]
```
</details>

<details><summary>gold conversation 280394</summary>

```
Customer: Tesco I bought cherry jam doughnuts and was very disappointed to find out they had no jam inside :( [link]
Tesco: I'm really sorry about this. I understand how disappointing this must have been for you. 1/3
Tesco: Could you DM me your name, address, store, barcode details, price, use by date and supplier code? 2/3
Tesco: I can then log this feedback on our system and refund you. Also can I pass your details onto the supplier? Thanks, Jessica 3/3
```
</details>

<details><summary>gold conversation 188707</summary>

```
Customer: Oh that’s cheeky!!! eggs bought got home and one had been taken out from behind the label!!! #Thecheekofit Tesco [link]
Tesco: Oh no Sarah, I'm sorry for the inconvenience caused. Are you able to return for an exchange? If not, I can refund you from here.Thanks, Leah
Customer: Tesco Thank you for your reply. No unfortunately I needed them so couldn’t return I’m afraid
Tesco: Hi Sarah. No worries I'll refund you from here. Can you please DM me the following information please? 1/2
Tesco: The store you bought these from, the SC code, your full name, address and email. Would you like a refund via email or post? TY-Charlotte 2/2
Customer: Tesco Hi the were bought from Tesco extra Huddersfield road, Oldham
Customer: Tesco What is an sc code please ?
Tesco: Hi Sarah, it's the supplier code. It begins 'SC....' and is located near the barcode. Thanks - Lara.
```
</details>

<details><summary>gold conversation 401202</summary>

```
Customer: I'm really upset because I just went to have some orange juice with bits in and NO JUICY BITS TO BE SEEN ☹️ thanks Tesco
Tesco: Hi Hayley, Oh no! You can't have orange juice with out the best bit, I'm sorry about that I would have been devastated myself! 1/4
Tesco: Could I get your full name (with title), address, email address, barcode, supplier code, date code, price and store you bought it from? 3/4
Tesco: Could you please DM me with some details and I'd be more than happy to feed this back to our suppliers and also get you fully refunded? 2/4
Tesco: Are you ok with me passing your details on to our suppliers? Also would you prefer to be refunded via email or via post? Thanks, Calum 4/4
Customer: Tesco How would I find some of those details?
Tesco: Hi Hayley. The barcode is on the side of the carton. The Supplier code's a 4-6 digit number located next to Tescos address (e.g. SC1234) 1/2
Tesco: The date code should be on the lid or the neck of the carton. :) - Alisha 2/2
```
</details>

## q034 · British_Airways · policy

**Q:** British Airways lost my suitcase on my flight to New York. Can I claim for essentials I have to buy?

**Reference:** Yes. BA said to check the delayed bag's status through its link and send receipts for essentials bought while without your bags so they can arrange reimbursement.

<details><summary>gold conversation 232743</summary>

```
Customer: British_Airways why haven’t you sent missing luggage from yesterday from LDN-JFK yet? What’s the wait ... you are ruining people’s holidays
British_Airways: We're doing all we can to reunite our passengers with their belongings, Georgia. You can check the status of your delayed baggage via 1/3
British_Airways: 2/3 the attached link. If you've purchased any essentials while you've been without your bags please send us your receipts so that we can
British_Airways: 3/3 arrange your reimbursement. ^Linds [link]
```
</details>

<details><summary>gold conversation 69818</summary>

```
Customer: British_Airways there was only a few people on my flight and you still lost my bag #nextflighthopefully #ba0638 to #Athens
British_Airways: Please accept our sincere apologies for the delay to your baggage. Our team are working hard to reunite you as soon as possible.1/2
British_Airways: When your baggage is delayed, you can find out what to do here: [link] 2/2 ^Liz
```
</details>

## q035 · British_Airways · policy

**Q:** Why does British Airways sell more tickets than there are seats on a flight?

**Reference:** BA said overselling is common airline practice that keeps fares low; when a flight is oversold they ask for volunteers to travel later and, if nobody volunteers, select passengers.

<details><summary>gold conversation 155995</summary>

```
Customer: British_Airways ruined my travel arrangements by overbooking flights to JFK. Selling tickets for non-existing seats is unethical.
British_Airways: It's common practice in the airline industry to oversell, as it allows us to keep our fares as low as possible, Gurur. 1/3
British_Airways: Occasionally we do it get it wrong and will ask for volunteers to travel later. If no one volunteers we will select people instead. 2/3
British_Airways: We hope you had a pleasant flight to NYC once you travelled. ^Steph 3/3
Customer: British_Airways In fact, you're not selling seats but a probability to get a seat; this should be banned + I doubt if's actually legal (see "gambling") 1/2
Customer: British_Airways ...like banks marketing papers without real backing but just a probability of profit, "occasionally" causing the whole economy to crash 2/2
British_Airways: Hi Gurur, we're so sorry about this. Did you manage to get rebooked or anything at the airport? ^Alex C
```
</details>

## q036 · British_Airways · policy

**Q:** I tried to check in for my British Airways flight too many times and now I'm blocked. What do I do?

**Reference:** BA said you can try again 24 hours after the block; it's a security measure so nobody else can access your booking.

<details><summary>gold conversation 302693</summary>

```
Customer: British_Airways Hi, I was trying to check in my reservation and for some reason I tried too many times and now I am blocked! Help!!!
British_Airways: Oh no! Don't worry you can try again 24 hours after it told you you were blocked, it's just for security. 1/2
British_Airways: To make sure no one can access your booking apart from you. 2/2 ^Ashleigh
Customer: British_Airways The problem is that I leave in 6 hrs. Thanks
British_Airways: I'm sorry for the delay in this response. I hope you managed to get checked in for your flight and enjoyed your trip with us! ^Marie
```
</details>

## q037 · British_Airways · incident

**Q:** Why was British Airways flight BA2278 from Oakland cancelled on 18 November?

**Reference:** BA said it was cancelled because of a technical issue with the aircraft.

<details><summary>gold conversation 618126</summary>

```
Customer: British_Airways no explanation! Hours on hold,sent to different departure airport,different arrival airport,late, need to be home for cats! [link]
British_Airways: Sorry for the disruption to your journey, Laura. I do hope you're on your way soon. Let us know if you'd like us to give you a call to discuss the issue. ^Lisa
Customer: British_Airways Please let me know why flight BA2278 from Oakland at 16.25 was cancelled with such short notice. Thank you
British_Airways: Hi Laura, BA2278 on 18 Nov was cancelled due to a technical issue with aircraft. I'm sorry for any inconvenience this caused you. If you need any help, please DM your full name, reference, contact number, passport number, passport expiry and date of birth, and we'll take a look.
```
</details>

## q038 · VirginTrains · policy

**Q:** My Virgin Trains service was late and I couldn't sit in my reserved seat. Can I claim compensation?

**Reference:** Yes. VirginTrains said you can claim compensation online through their link.

<details><summary>gold conversation 129121</summary>

```
Customer: Gonna be a long trip home tonight😡😡😡😡 VirginTrains
VirginTrains: Hi Paz, is there anything we can help with this evening? ^HP
Customer: VirginTrains Well my reserved seat on the train would been nice😡😡😡😡 shambles.......don't worry about the late train , I'll be claiming all the fare back!
VirginTrains: Really sorry to hear you haven't been able to get your seat, Paz, which service are you on please? ^HP
Customer: VirginTrains 19:07 Euston to Crewe!!!! £95 and having to sit on my suitcase.......and I'm not alone.....at list dick Turpin wore a mask😡😡😡
VirginTrains: Apologies for the inconvenience caused, Paz. You can claim compensation for this online here: [link] ^HP
Customer: VirginTrains Don't worry I will............
```
</details>

## q039 · VirginTrains · policy

**Q:** My phone with my Virgin Trains mobile tickets might be dead by the time I travel. What can I do?

**Reference:** VirginTrains said you must be able to display mobile tickets on your device, and suggested contacting the Aftersales team to see if they could be sent to another device.

<details><summary>gold conversation 219597</summary>

```
Customer: VirginTrains hi I've got mobile tickets but my phone is not charging.. is there anything i can do in case it doesn't turn on?! travel @ 7pm
VirginTrains: 1/2 Hi Danielle, sorry to hear this. I'm afraid you do need to be able to display these on your device when travelling.
VirginTrains: 2/2 Are you travelling with another passenger at all? ^HP
Customer: VirginTrains Hi there no I'm travelling alone. Its on charge now, but i wondered if theres anything I can do as it's still a few hours to go...
VirginTrains: Ah ok, we would have suggested contacting our Aftersales team to see if they could be sent to another device for you ^HP
Customer: VirginTrains thanks but that doesn't really help me! what can i do? i don't really want to be buying another ticket. will going to the station help?
VirginTrains: 1/2 Really sorry Danielle but if you can't display the ticket then you would need to purchase another I'm afraid, as we can't
VirginTrains: 2/2 change the delivery method once the ticket has been purchase ^HP
```
</details>

## q040 · VirginTrains · troubleshooting

**Q:** I paid for Wi-Fi on a Virgin Trains train and it doesn't work. What should I do?

**Reference:** VirginTrains suggested forgetting the network in your device settings, reconnecting, and following their link.

<details><summary>gold conversation 561716</summary>

```
Customer: VirginTrains I've just paid £5 for my wifi and it's still not working, give me feee stuff pls
VirginTrains: 1/2 Oh no, sorry to hear this Sam. Can you please try forgetting the network in your settings, reconnect and
VirginTrains: 2/2 follow this link: [link] Please let us know if this works for you ^HP
```
</details>

## q041 · UPSHelp · policy

**Q:** UPS says my package will arrive by 'end of day'. What time does that mean?

**Reference:** UPSHelp said end of day is 7 PM (delivery times run 9am to 7pm), though drivers can be out later in some areas.

<details><summary>gold conversation 364368</summary>

```
Customer: When UPSHelp Say the delivery estimate is end of day do they mean they have up until 11:59pm? To deliver it..... #ups
UPSHelp: End of day is 7 PM. However, in some areas we can be out later. ^BO
Customer: UPSHelp So because it’s past that time now will it be back out for delivery tomorrow?
UPSHelp: Let me check the status of your package. Please DM your tracking number for further assistance. ^BO [link]
```
</details>

<details><summary>gold conversation 450129</summary>

```
Customer: UPSHelp Your website is inscrutable. I have a login. Is there any way for me to tell WHEN during the day my package might arrive?
UPSHelp: End of day delivery times are from 9am to 7pm. ^AD
Customer: UPSHelp I understand that, but is there not a site where you can track the truck your item is on… Or is that the other guys?
UPSHelp: Through are UPS My Choice app certain areas have a feature called follow my package. ^AC [link]
```
</details>

## q042 · UPSHelp · product

**Q:** Is there a way to get a more precise UPS delivery time than just 'out for delivery'?

**Reference:** UPSHelp recommended a free UPS My Choice account: set preferences, get updates, choose a two- or four-hour delivery window, and in some areas use Follow My Package.

<details><summary>gold conversation 389347</summary>

```
Customer: . / UPSHelp, why can’t customers track where your delivery vans are and know a particular time frame for deliveries?...
UPSHelp: Have you looked into setting up a UPS My Choice account. It is free and allows you to set preferences &amp; receive updates. ^KM [link]
Customer: UPSHelp Updates are very generals. e.g - ‘out for delivery’ or ‘end of day’. I somehow missed a delivery even though I was at home and aware. 1/2
Customer: UPSHelp If there was a way to know the estimated hour, I would of went down to the ground floor to make sure I received my delivery. 2/2.
UPSHelp: My Choice you can select a two or four hour delivery window. Please DM the tracking number we can research. ^TV [link]
```
</details>

<details><summary>gold conversation 450129</summary>

```
Customer: UPSHelp Your website is inscrutable. I have a login. Is there any way for me to tell WHEN during the day my package might arrive?
UPSHelp: End of day delivery times are from 9am to 7pm. ^AD
Customer: UPSHelp I understand that, but is there not a site where you can track the truck your item is on… Or is that the other guys?
UPSHelp: Through are UPS My Choice app certain areas have a feature called follow my package. ^AC [link]
```
</details>

## q043 · UPSHelp · howto

**Q:** I need to reschedule my UPS new-hire orientation but the phone number on my paperwork doesn't work. What should I do?

**Reference:** UPSHelp said to sign in to the UPS jobs website and reschedule there, and if that doesn't work, go to the building and talk to HR directly.

<details><summary>gold conversation 519483</summary>

```
Customer: do you know the number to contact the HR department at the UPS facility located on Vero Road in Maryland
UPSHelp: We do not have that information available. If you are an employee, please speak with your local management team. ^TT
Customer: UPSHelp I was supposed to go to my new hire orientation today but needed to reschedule and the number given on the paperwork isn't valid. So I have no way of contacting them.
UPSHelp: You can go onto [link] and sign in and reschedule on there. I am sorry that the number doesn't work. If the website doesn't help I would drive to the building and talk to HR direct. ^KM [link]
```
</details>

## q044 · UPSHelp · policy

**Q:** UPS tracking says my package was transferred to the post office. When will it arrive?

**Reference:** UPSHelp said the post office will deliver it within 1-2 days.

<details><summary>gold conversation 615114</summary>

```
Customer: My mood when has had my package in town since 8 AM yesterday and it still isn’t out for delivery [link]
Customer: [link]
UPSHelp: Based on the screenshots provided, your package was transferred to the post office. This means they will be delivering the package to you within 1-2 days. ^E.W. [link]
```
</details>

## q045 · UPSHelp · policy

**Q:** My UPS shipment to Kuwait is stuck in customs. Can UPS do anything?

**Reference:** UPSHelp said customs clearance is out of UPS's control; the shipper had been contacted to provide documentation and you need to contact the shipper for updates.

<details><summary>gold conversation 708180</summary>

```
Customer: UPSHelp And counting [link]
UPSHelp: Per your screen print your package has not yet cleared customs. This is out of the control of UPS. Your shipper has been contacted to provide documentation to clear the package. You will need to contact them for an update. ^CH
Customer: UPSHelp No. at kuwait aren’t active like others courier. There is nothing lack and no one yet contact us. If i call no response. They are dead here. I ask my supplier several time not to use UPs but they did same mistake over and over thankfully Haulotte middle east doesnt use UPS
```
</details>

## q046 · hulu_support · troubleshooting

**Q:** Hulu Live TV keeps skipping on my Chromecast. How do I fix it?

**Reference:** hulu_support suggested rebooting the device and modem/router (power cycling the equipment), following their troubleshooting link, and checking that internet speeds meet Hulu's requirements.

<details><summary>gold conversation 261699</summary>

```
Customer: hulu_support any reason why my live TV skips so much? Are you still in Beta testing???
hulu_support: Oh no! Which device do you use? Noticing this w/a certain channel? For now, try a quick reboot of your device+modem/router.
Customer: hulu_support chromecast from Android.
hulu_support: Got it. Please try: [link] --particularly power cycling your equipment. Is there any improvement after?
Customer: hulu_support actually, yes there seems to be! Thanks!
hulu_support: We're glad to hear it! If we can ever help with anything else, we're just a tweet away!
Customer: hulu_support sadly, the improvement only lasted a moment. 🙁
hulu_support: Oh no! Are you noticing this w/a certain channel? Please double-check your speeds are meeting our reqs: [link]
```
</details>

## q047 · hulu_support · troubleshooting

**Q:** Hulu shows error runtime-2 on my PS4 after a few minutes of playback. What should I do?

**Reference:** hulu_support suggested restarting the device and following their troubleshooting link. The customer found the problem was limited to one season of a show.

<details><summary>gold conversation 698161</summary>

```
Customer: hulu_support I keep getting this error. Tried googling it, no troubleshooting comes up. Help? runtime-2-15e4530e
hulu_support: Is the error appearing on your PS4, or are you accessing our app from a different device now? When exactly does it pop up?
Customer: hulu_support Whoops, forgot to mention, it's my PS4. I have season 20 of South Park on, it plays for about 2-3 minutes, starts to buffer for a while, then the screen goes black with that error.
hulu_support: Gotcha! Try a quick restart of your device as well as: [link] Any improvement after that? Let us know!
Customer: hulu_support I restarted it prior to messaging you, as if it were something that silly, I didn't want to bother you with it. It seems like it's just that season, as I moved to another and haven't had an issue yet.
hulu_support: Interesting... 🤔 If you do happen to run into more trouble please snap a pic of the error and send it our way for reference.
```
</details>

## q048 · hulu_support · product

**Q:** Why does Hulu play so many commercials during some shows?

**Reference:** hulu_support said ad breaks typically happen in the same time slots as in the original broadcast.

<details><summary>gold conversation 802416</summary>

```
Customer: Omg what is the deal with suddenly having so many commercials?!? It’s more commercials than just watching cable. You’re ridiculous. At least give me different commercials every break or something. 🤬
hulu_support: We're wondering if maybe it's due to being a dinosaur. Our system isn't designed for dinosaurs (yet... 🦖). Can you let us know the shows, seasons, and episodes affected? What device were you using? The more details you provide, the better we can assist. 💚
Customer: hulu_support Watching “The Orville” on the Apple TV 4th generation. There are commercials every 5 minutes of an actual show. It’s hard to really get into a show because every time I really start getting into it, there is a commercial. And it’s the same commercials every break.
hulu_support: Gotcha. Ad breaks typically occur in the same time slots as they did during the original broadcast. For The Orville, that would be about 5 commercial breaks. Are you seeing more than this when streaming?
Customer: hulu_support I’m not sure. I’ll have to count next time I watch
```
</details>

## q049 · ChipotleTweets · product

**Q:** Why does Chipotle's queso taste so different from other queso?

**Reference:** Chipotle said it's made with real, unprocessed ingredients and that they're still working to perfect the recipe.

<details><summary>gold conversation 16725</summary>

```
Customer: ChipotleTweets gotta step up the queso game my friends. Still love everything else
ChipotleTweets: It's a bit different because it's made with real ingredients, but we're working to perfect it. -Tay
Customer: ChipotleTweets I'll be waiting #brandloyalty
```
</details>

<details><summary>gold conversation 652444</summary>

```
Customer: ChipotleTweets The Queso was not worth the wait! You guys should really try to make it taste good because it’s soooo below average.
ChipotleTweets: Sorry you're not a fan. It's different because we're using unprocessed ingredients, but we'll keep working on the recipe. -AC
Customer: ChipotleTweets Don’t get me wrong, I love Chipotle! I actually asked at my local Chipotle why the queso was so bland and they said the same thing about the ingredients. I think you can do better! Any chance of having quac without onions 🤞🏻?
ChipotleTweets: We'll keep striving for better. No chance of guac without onions at the moment. -AC
```
</details>

## q050 · ChipotleTweets · product

**Q:** Which Chipotle restaurants still have soft corn tortillas?

**Reference:** Chipotle said it is phasing out soft corn tortillas entirely.

<details><summary>gold conversation 88896</summary>

```
Customer: ChipotleTweets I moved to Portland and was disappointed at lack of corn tortillas :( which cities have them?
ChipotleTweets: We are phasing out the soft corn tortillas entirely, but you can check out [link] for other ideas. -Zach
Customer: ChipotleTweets Wow way to be the bearer of bad news Zach!
```
</details>

## q051 · ChipotleTweets · product

**Q:** Can I order Chipotle guacamole without onions?

**Reference:** No, not at the moment.

<details><summary>gold conversation 652444</summary>

```
Customer: ChipotleTweets The Queso was not worth the wait! You guys should really try to make it taste good because it’s soooo below average.
ChipotleTweets: Sorry you're not a fan. It's different because we're using unprocessed ingredients, but we'll keep working on the recipe. -AC
Customer: ChipotleTweets Don’t get me wrong, I love Chipotle! I actually asked at my local Chipotle why the queso was so bland and they said the same thing about the ingredients. I think you can do better! Any chance of having quac without onions 🤞🏻?
ChipotleTweets: We'll keep striving for better. No chance of guac without onions at the moment. -AC
```
</details>

## q052 · ChipotleTweets · troubleshooting

**Q:** My coworkers got a free chips and guac offer in the Chipotle app but I didn't. Why?

**Reference:** ChipotleTweets asked whether the app update had been downloaded and pointed to a contact form so they could check on the offer.

<details><summary>gold conversation 519337</summary>

```
Customer: Hey ChipotleTweets how come all my co-workers got a free chips and guac when they opened they're app up but not me? [link]
ChipotleTweets: Did you download the update yet? -Gabe
Customer: ChipotleTweets I did! New UI is as fresh as your guac 💲👌
ChipotleTweets: Yessir. That's the truth. You can write us at [link] so we can check into that chip deal. -Gabe
```
</details>

## q053 · sprintcare · policy

**Q:** I got Hulu through my Sprint Unlimited plan. Will I be charged when the trial ends?

**Reference:** No. sprintcare said Hulu comes with Sprint Unlimited plans at no extra charge; it isn't a free trial.

<details><summary>gold conversation 799334</summary>

```
Customer: sprintcare I signed up for Hulu with sprint but it still seems I’ll be charged after free trial. How do I continue Hulu for free w/ plan
sprintcare: Have any questions? I’ve got answers! You can verify additional information about this amazing service here: [link] . -AG
Customer: sprintcare Ok but it says on Hulu I’ll be charged in January. How will I not be charged ?
sprintcare: Hey there! Please note, that our service of Hulu with our Unlimited Plans is available to all customers at no additional charge. This is not a free trial, once you sign in with us, Hulu service is free. Just click here [link] for more information. - EH
```
</details>

## q054 · XboxSupport · troubleshooting

**Q:** Forza Motorsport 7 goes to a black screen after the driver selection cutscene on my Xbox. Is there a fix?

**Reference:** XboxSupport suggested closing and reopening the game, then removing and re-adding the profile, and finally said it was a known issue being investigated by the relevant teams.

<details><summary>gold conversation 23606</summary>

```
Customer: XboxSupport in Forza 7 I get a black screen as the pick your gender/racer cutscene ends is there a fix for this?
XboxSupport: Hey, did the screen appear multiple times? If the issue continues, try closing the game and re-opening it. ^RM
Customer: XboxSupport I have tried that about 10 times and get the black screen every time. All I here is music in the background
Customer: XboxSupport I have deleted save data, tried it while my xbox is offline and hard reset the console. Nothing is working.
XboxSupport: Okay, here is another step you can try. You can try removing and adding your profile [link] Let us know if that works. ^RM
Customer: XboxSupport Tried it but now there is the xbox live error not allowing me to launch the game. Tried it offline after that and still get a black screen
XboxSupport: Hi again! This issue is currently being looked into by the proper teams: [link] 1/2 ^JA
XboxSupport: We appreciate your patience and understanding. 2/2 ^JA
Customer: XboxSupport I can launch the game now but still getting the blacl screen
```
</details>

## q055 · XboxSupport · troubleshooting

**Q:** The Crunchyroll app on my Xbox One keeps closing by itself. What should I try?

**Reference:** Uninstall the app, power cycle the Xbox One and the router/modem, then reinstall. If it continues, XboxSupport asked for Detailed Network Statistics (Settings > Network > Network Settings > Detailed Network Statistics).

<details><summary>gold conversation 82817</summary>

```
Customer: XboxSupport you guys still haven't helped me out at all when I asked about my crunchyroll app. It keeps starting up and closing on its own
XboxSupport: Hi there, if your app is crashing, please try uninstalling the app, power cycling: 1 ^ZM
XboxSupport: [link] your Xbox One console &amp; router/modem , and reinstalling the app. Any change? 2 ^ZM
Customer: XboxSupport I did that and sign out of the app from my laptop. It still does the same thing.
XboxSupport: seen on your Xbox One console? Are you experiencing this with any other apps? 2 ^ZM
XboxSupport: Apologies, it appears our tweet got cut off there. Can you please 1 ^ZM
XboxSupport: send us your Detailed Network Stats (Settings&gt;Network&gt;Network Settings&gt;Detailed Network Statistics) ? 2 ^ZM
Customer: XboxSupport [link]
```
</details>

## q056 · XboxSupport · troubleshooting

**Q:** My FIFA 18 disc won't load on Xbox even though I have the full game. What do I do?

**Reference:** Delete FIFA 18, power cycle the console, then reinstall the game.

<details><summary>gold conversation 377295</summary>

```
Customer: XboxSupport im trying to load fifa 18 and its saying this even tho i have the full game on disk? [link]
Customer: XboxSupport None of my games on disc will load
XboxSupport: Hi there! Let's try deleting FIFA 18, power cycle the console, then reinstall the game again [link] ^TJ
```
</details>

## q057 · XboxSupport · incident

**Q:** I keep getting disconnected at the end of Call of Duty WWII matches on Xbox and lose my XP. Is it my connection?

**Reference:** XboxSupport said it appeared to be a known issue that Activision was investigating, and offered to help troubleshoot the network connection too.

<details><summary>gold conversation 522678</summary>

```
Customer: 2 domination matches lost because of server disconnection XboxSupport #2XP
Customer: XboxSupport Got to the end of match and took me to headquarters with no accrue
XboxSupport: Hi there! We're sorry to hear about that. It would appear that this is a known issue that Activision is investigating: [link] If you would like to continue troubleshooting your network connection, just let us know. ^JA
```
</details>

## q058 · XboxSupport · policy

**Q:** My Xbox One S makes a chirping noise while I play. Is that normal and can I get it repaired?

**Reference:** XboxSupport said the console makes some noise when the fan is running; if you're concerned, set it up for service online, and a service charge applies if it's out of warranty.

<details><summary>gold conversation 656167</summary>

```
Customer: XboxSupport Hi, my Xbox One S has a very weird clicking sound going one while playing. Makes it impossible to play and I sit 3 metres away from the xbox.Any way I can have it checked in Austria?
Customer: XboxSupport It is actually chirping sound. Exactly like here. [link]
XboxSupport: Hi, your Xbox One S console will make some noise when the console/fan is operating. However, if you are concerned, you can setup your console for service here: [link] . We're afraid a service charge would apply if the console is out of warranty. ^ZM
Customer: XboxSupport Hi, the console is under warranty.In the link you supplied, after selecting my console, the webpage just says "Retrieving your eligibility" without any change. Tried different browsers.
```
</details>

## q059 · AskPlayStation · troubleshooting

**Q:** My PS4 keeps showing a network error when I connect to PlayStation Network. What should I try first?

**Reference:** AskPlayStation suggested power cycling your network devices; if the error persists, start the PS4 in Safe Mode and choose Restore Default Settings.

<details><summary>gold conversation 59224</summary>

```
Customer: AskPlayStation [link]
AskPlayStation: Here to assist! Please power cycle your network devices and try again: [link]
Customer: AskPlayStation Already done that
AskPlayStation: Please start your system in safe mode and select restore default settings. Steps here: [link]
Customer: AskPlayStation Done that and the error still comes up
AskPlayStation: Oh no! We have sent you a direct message to assist!
```
</details>

<details><summary>gold conversation 666421</summary>

```
Customer: AskPlayStation I'm having problems with the activation servers is this a known issue at the moment [link]
AskPlayStation: Sorry to know that. Please power cycle your network devices and try again, steps here: [link]
Customer: AskPlayStation Got it that fixed it thank you
AskPlayStation: Glad to know is working. Please feel free to contact us if you have further concerns.
```
</details>

## q060 · AskPlayStation · troubleshooting

**Q:** A PS4 trophy I earned won't unlock even after reinstalling the game. What can I do?

**Reference:** AskPlayStation suggested using Restore Licenses to refresh your purchases.

<details><summary>gold conversation 112965</summary>

```
Customer: AskPlayStation One of my trophies are glitched and it won't give it to me? I have tried removing installing the game but it doesn't work???
AskPlayStation: That's not good. Please try Restore Licenses to refresh your purchases: [link]
Customer: AskPlayStation It didn't work... For some reason it is still not coming up? I am so confused...
AskPlayStation: Please check your DM's for more instructions.
```
</details>

## q061 · AskPlayStation · troubleshooting

**Q:** My internet is fast but my PS4 gets poor upload speeds even on a wired connection. Any fix?

**Reference:** After the general network tips, AskPlayStation suggested Safe Mode option 4 (Restore Default Settings) and then setting up the connection again.

<details><summary>gold conversation 501270</summary>

```
Customer: AskPlayStation please help me. I have a very good connection where I have download speed of 75mbps and upload of 30mbps but I do not get any of these speeds on my ps4. It's making online gaming a terrible experience.
AskPlayStation: Here to assist! Information to improve your network connection is available here: [link]
Customer: AskPlayStation I've tried all these suggestions unfortunately. Even with a wired connection I don't get good upload speeds
AskPlayStation: Please try safe mode option 4 Restore Default Settings, and set up the connection again: [link]
```
</details>

## q062 · AskPlayStation · troubleshooting

**Q:** After I signed in on a friend's PS4, my games show a content lock on my own console. How do I fix it?

**Reference:** AskPlayStation said the console has to be set as your primary PS4 to access the content, and to Restore Licenses and try again.

<details><summary>gold conversation 530992</summary>

```
Customer: AskPlayStation my games have a content lock because I logged on on my mates ps4 the only way I can play is if I activate it as my primary
AskPlayStation: Hi there! To access content the console needs to be set up as primary. Restore licenses &amp; try again: [link]
Customer: AskPlayStation I have already tried that 😐
AskPlayStation: Thanks for trying that. Please make sure you are following us, so we can assist you better via a Direct Message.
Customer: AskPlayStation I am
AskPlayStation: We have sent you a Direct Message via Twitter with further instructions.
```
</details>

## q063 · ATVIAssist · policy

**Q:** I spent a prestige token on the wrong weapon in Call of Duty WWII. Can Activision refund it?

**Reference:** No. ATVIAssist said prestige tokens can't be refunded.

<details><summary>gold conversation 432791</summary>

```
Customer: ATVIAssist You probably won't believe this but I used my Prestige token on the Lee Enfield by accident. Is this possible to be reverted?
ATVIAssist: Hey there! Unfortunately, I cannot refund prestige tokens. I apologize for any frustration this may cause. ^MB
Customer: ATVIAssist That's alright, I'm already able to prestige my soldier, however I won't be doing that until the bugs when prestiging (no orders, attachments etc) are fixed. Thanks for the reply.
ATVIAssist: I sincerely apologize for the frustration. Stay tuned to Sledgehammer's twitter for all WW2 updates. ^MB
```
</details>

## q064 · ATVIAssist · troubleshooting

**Q:** Call of Duty keeps saying 'game restarted for a new update' and won't start. Any ideas?

**Reference:** ATVIAssist suggested power cycling the console and resetting the router for 5 minutes. The customer fixed it by deleting and reinstalling the game.

<details><summary>gold conversation 703940</summary>

```
Customer: my game isn’t working keeps saying game restarted for a new update ! Any ideas ?
ATVIAssist: Hello there. I apologize for the delay and inconvenience. Are you still experiencing this issue? Please let me know. ^RN
Customer: ATVIAssist Yes still having these issues
ATVIAssist: Go ahead and power cycle your console and reset your router for 5 minutes. Let us know if this helps. Thank you. ^RN
Customer: ATVIAssist Deleted and re installed and it worked thanks for help !
```
</details>

## q065 · AskTarget · policy

**Q:** When will my Target pre-order ship?

**Reference:** AskTarget said pre-orders ship on or near the release date, as stated on the item page, and to watch your email for updates.

<details><summary>gold conversation 549581</summary>

```
Customer: Hey, . When can I expect my preorder bundle? I still haven’t received it. 😰😰
AskTarget: We apologize for the disappointment. When you place a pre-order, by the add to cart button on the item detail page, it states: "Ships on or near the release date". You can review this information on [link] here: [link] Keep an eye on your email.
Customer: AskTarget Oh, I’m not mad or anything. I’m just anxious. Haha.
```
</details>

## q066 · GWRHelp · howto

**Q:** How do I get the passenger charter discount when renewing my GWR season ticket?

**Reference:** GWRHelp said that if the season ticket was bought at a station you renew at the same ticket office; if it was bought online you renew online and then email them to claim the discount.

<details><summary>gold conversation 286943</summary>

```
Customer: GWRHelp Is it poss to renew annual season ticket online and get the passenger charter discount? I get thru to payment, no discount offered.
GWRHelp: Hello Tim. To claim renewal, you will need to return to the point of purchase. A renewal discount can be sent to __email__ online.
Customer: GWRHelp Are you saying it can only be done at a station? I don't understand what you meant about sending a renewal discount to your email address.
GWRHelp: Yes, if your current Season Ticket was purchased at the station you will need to return to the same Ticket Office (1/2)
GWRHelp: If you purchased your Season Ticket online, you'll need to email upon online renewal to claim the discount. - Jordan (2/2)
Customer: GWRHelp To be clear, I haven't renewed the ticket yet. I just want to make sure that I get the discount when I do. (1/2)
Customer: GWRHelp If I can only renew online if I bought last year's ticket online then the website and customer centre don't make that at all clear. (2/2)
GWRHelp: That is correct, you can only claim renewal discount online if you purchased online. - Jordan
Customer: GWRHelp Ok thanks for the clarification Jordan. Please could you pass on this feedback to the web team and call centre? Cheers, Tim
GWRHelp: I shall feedback to the departments. - Jordan
```
</details>

## q067 · GWRHelp · product

**Q:** Does GWR offer information or announcements in Welsh?

**Reference:** GWRHelp said Welsh literature is available on request and some staff may make announcements in Welsh.

<details><summary>gold conversation 310156</summary>

```
Customer: Terrible, illogical decision by GWRHelp - Welsh passengers have a right to services in their language of choice. System should adapt. [link]
GWRHelp: Hi. Welsh literature is available upon request and some staff may make announcements in Welsh. Lewis
Customer: GWRHelp Thanks Lewis, but I think Welsh deserves equal treatment with English, not tokenism. Please pass this on to management. R.
```
</details>

## q068 · GWRHelp · policy

**Q:** My GWR train was cancelled because of a crew shortage. Can I get compensation?

**Reference:** GWRHelp said compensation may be due depending on the delay, claimed through their link.

<details><summary>gold conversation 339052</summary>

```
Customer: GWRHelp how comes so many trains today have been cancelled with no information?
GWRHelp: The 1821 was cancelled because of a shortage of train crew - Apologies for this. Phil.
Customer: GWRHelp Just frustrated, as onward journeys were also cancelled, I know you have no control, just wanted to get home though!
GWRHelp: I can appreciate the frustration Sarah, apologies for this. Depending on the delay compensation may be due, from [link] P
```
</details>

## q069 · GWRHelp · incident

**Q:** No GWR trains from Kemble to Paddington show up for 2 December. Will anything be running?

**Reference:** GWRHelp said an amended timetable for upgrade work wasn't finalised yet (expected within a couple of weeks); there would be a train service but possibly longer journey times or replacement buses for part of the journey.

<details><summary>gold conversation 451559</summary>

```
Customer: gwrhelp I'm trying to book a train from Kemble to Paddington on 2nd December but there are no trains and no information, can you advise?
GWRHelp: Hi Alice, there will be an amended timetable because of upgrade work but this hasn't been fully finalised yet. -Andy
Customer: GWRHelp Thanks Andy, do you know when that might be? I urgently need to re-arrange an event if we can't get to London quickly on Sat 2nd, thanks.
GWRHelp: We are hopeful it will be in the next couple of weeks. -Andy
Customer: GWRHelp Does an amended timetable mean there will be some trains running or none at all? Need to know if there will be some kind of train service ta
GWRHelp: There will be a train service but there may be extended journey times or replacement buses for part of the journey. -Andy
```
</details>

## q070 · sainsburys · policy

**Q:** I bought a product at Sainsbury's that turned out to be bad. How do I get a refund?

**Reference:** Sainsbury's either asks you to take it back to the store with your receipt for an exchange or refund, or asks which store it was from (and sometimes for a barcode photo) and then for your Nectar card number by DM so they can add the refund, sometimes with extra, as points.

<details><summary>gold conversation 407721</summary>

```
Customer: Hi sainsburys, this brocoli had a bit more protein in it than I generally like... [link]
sainsburys: Hi there, sorry about this Jon. We'd definitely expect more from our products. Which store did you buy this from? Robbie
Customer: sainsburys Thanks for getting back to me. East Village, Stratford, London
sainsburys: Thank you, if you DM me your Nectar card number via this link I can get a refund added for you plus extra and get this fed back too. Robbie [link]
```
</details>

<details><summary>gold conversation 781335</summary>

```
Customer: sainsburys are you now repairing eggs before selling? 🤔 Too much hassle to return this [link]
sainsburys: Hi there, I'm very sorry about this. We'd definitely expect more from our products. Can you send me a pic of the barcode please? Which store did you buy these from? Robbie
Customer: sainsburys Lordshill, Southampton. Thanks. [link]
sainsburys: Thank you, if you DM me your Nectar card number via this link I can get a refund added for you and make sure this is fed back to our buyers. Robbie [link]
```
</details>

<details><summary>gold conversation 812148</summary>

```
Customer: sainsburys Haywards Heath: You've put your pizza counter pizzas up by £1.20, this doesn't mean I wanted both BBQ &amp; tomato sauce on it at the same time to compensate?!? #whatwereyouthinking #pizzafail #messeduppizza
sainsburys: Sorry about that Jemma, doesn't sound like the most pleasant combination. Could you DM us on the below link with a picture of the barcode from the pizza please? Thanks. Gordon. [link]
Customer: sainsburys Oh sorry Gordon. That’s long gone in the bin I’m afraid 😬
sainsburys: No worries Jemma, Could you DM us over your Nectar card number? I'd be happy to feed this back to the store manager and add some extra points as a refund. Gordon.
```
</details>

<details><summary>gold conversation 236417</summary>

```
Customer: sainsburys gorseinon!! Bought this and it's watered down! Basically water!! [link]
sainsburys: Hi there, sorry about this! Which store did you buy this from? Robbie
Customer: sainsburys Gorseinon!! My friend bought it she's fuming
sainsburys: Thanks, I'm really sorry this has happened. Can you or your friend please take this back to store along with you receipt...1/2
sainsburys: ...and they'll be able to exchange/refund this for you. Aisha 2/2
```
</details>

## q071 · sainsburys · policy

**Q:** My Sainsbury's online order came with a poor substitute. What are my options?

**Reference:** sainsburys said the store sends the closest available match to what you ordered and you can send it back if you're unhappy with it.

<details><summary>gold conversation 401593</summary>

```
Customer: sainsburys hardly a reasonable substitute, got half what I ordered 😢 [link]
sainsburys: Really sorry Antony! The store will send out the closest match to what you've ordered. You can send it back if you're unhappy with it. Faiza
Customer: sainsburys It’s not the closest match! It’s 1/2 my order, so now have to go to Tesco to get the rest! Should’ve been 4 bags as sub!!
Customer: sainsburys Don’t want to send it back, I want the qty that I ordered
sainsburys: This what would have been available in the store, unfortunately you'll need to return these back to store. Mariya
```
</details>

## q072 · sainsburys · howto

**Q:** Sainsbury's stopped selling a product I really like. Can I ask them to bring it back?

**Reference:** They confirmed the product is no longer stocked and said you can log a product request through their link.

<details><summary>gold conversation 687999</summary>

```
Customer: sainsburys where have the wonderful Belizean prawns gone? Haven't seen them for months and missing them greatly... [link]
sainsburys: Hi there, sorry Stuart! Which store do you usually shop in? We'll have a check for you. Robbie
Customer: sainsburys East Dulwich (Dog Kennel Hill)
sainsburys: I'm afraid that we no longer stock this product in our stores Stuart. You can log a product request for this here though: [link] I'll keep my fingers and toes crossed for you! Take care, Gabby
Customer: sainsburys I'll log that! Thanks for finding out. It's a great pity...
```
</details>

## q073 · AskLyft · howto

**Q:** How do I report a Lyft driver who was driving dangerously?

**Reference:** AskLyft pointed to its Critical Response Line (click 'Call Me' and enter your number on their page) and said you can also report it through the Help Center.

<details><summary>gold conversation 1288</summary>

```
Customer: AskLyft What's the appropriate response when a driver speeds at 95 MPH with your wife and baby in the backseat? Not exaggerating.
Customer: AskLyft Just realized I never asked you to call me. FWIW, I would have definitely reported this if I could just send an email, with photo evidence.
AskLyft: You can do that as well through our Help Center at [link]
```
</details>

<details><summary>gold conversation 257361</summary>

```
Customer: I understand why my lyft driver has a cross in his car. We are going 50 down this street, we need all the blessings we can get not to hit someone.
AskLyft: To be immediately connected with our Critical Response Line, click the "Call Me" button and enter your number at [link]
AskLyft: Please report any unsafe driving behavior to our team at your earliest convenience.
```
</details>

<details><summary>gold conversation 46834</summary>

```
Customer: Felt lame to be arriving so early, until my lyft line almost got into an accident and missed 3 turns making me fashionably late 😎
AskLyft: To be immediately connected with our Critical Response Line, click the "Call Me" button and enter your number at [link]
Customer: AskLyft Whoops.
```
</details>

## q074 · AskLyft · howto

**Q:** How much will a Lyft from Phoenix airport cost, and what if I have a lot of luggage?

**Reference:** AskLyft said prices vary by area and to use the price estimator on your city's page; they suggested requesting a Lyft Plus for extra luggage room.

<details><summary>gold conversation 480393</summary>

```
Customer: Via Lyft: What are the charges from the Phoenx airport to Surprise, Az. on Mt. View Blvd. I will need help with my luggage to carry them to my condo, [link]
AskLyft: Prices vary in each coverage area. You can use the price estimator on your city's page to determine ride cost at [link]
AskLyft: We also suggest requesting a Lyft Plus so you can be sure there is enough room for luggage. :)
AskLyft: Let us know if you have any other questions or concerns! We're always happy to help.
```
</details>

## q075 · AskLyft · policy

**Q:** What does Lyft do about riders who are racist?

**Reference:** AskLyft said it has a very strict anti-discrimination policy, takes these reports seriously, and asked for details by DM to investigate.

<details><summary>gold conversation 490856</summary>

```
Customer: So is really just gonna let racist riders use their service ??
AskLyft: Please know that we have a very strict anti-discrimination policy on our platform and we take these reports very seriously.
AskLyft: Please send us a DM with more information so that we can get investigate this further immediately. [link]
```
</details>

## q076 · O2 · troubleshooting

**Q:** I've already used most of my O2 data a week into the month. How can I work out why?

**Reference:** O2 suggested checking your remaining balance on My O2, whether Wi-Fi Assist is turned on, and which apps use the most data.

<details><summary>gold conversation 140361</summary>

```
Customer: When you've used 80% of your data &amp; you only got it last week. How?!? O2 help me out here! [link]
O2: Have you looked at your remaining balance on My O2? [link] Have you got Wi-Fi assist turned on in the background?
Customer: O2 I have indeed. For what I pay I get minimal data
O2: Have you checked your settings to see what apps are using data up the most? Do you run out of data often? Please DM us more info. [link]
```
</details>

## q077 · O2 · policy

**Q:** I upgraded my O2 contract and should get extra loyalty data, but it isn't showing in My O2. Why?

**Reference:** O2 said it is added automatically once the 14-day cooling-off period has passed.

<details><summary>gold conversation 468236</summary>

```
Customer: O2 when I upgraded my contract I took 30gb data, and I believe I should get 10gb from you for staying with o2, yet I don’t see that on myo2
O2: It will automatically be added to your account once the 14 day cooling off period has passed 👍
Customer: O2 Alright! Thanks
```
</details>

## q078 · O2 · policy

**Q:** Can O2 add a family discount to my existing contracts?

**Reference:** O2 said the family plan discount can only be added at renewal.

<details><summary>gold conversation 507315</summary>

```
Customer: O2 thanks so much for the discounts. Ive asked for cheaper deals every time i renew a contract and I get lies. 4 contracts running(at once) for 10 years and no LOYALTY discount whatsoever. Time to move on. [link]
O2: Hi John, we're sorry to hear this, have all 4 account been taken out within the last 28 days and all in your name? Have we discussed the plan with you? We'd be sad to lose you.
Customer: O2 Hi, all 4 accounts have been running for years now. I update them when the 24 mnths are up. I never get offered discounts, ive consistantly requested a family discount/package and never get it. 1 account is due to end start of December.
O2: 🤔 Family plan discount can only be added at renewal. You'll find more info here: [link]
Customer: O2 I asked when i renewed in June. I was told there is no family deal or discount. Goodbye o2.
O2: The plan only started in mid June so it's likely it wasn't available at the time you renewed. We'll be sorry to see you leave.
```
</details>

## q079 · O2 · incident

**Q:** My O2 Priority code for the Star Wars phone case isn't taking any money off at checkout. Why?

**Reference:** O2 said the codes ran out very quickly because the offer was so popular.

<details><summary>gold conversation 662904</summary>

```
Customer: O2 hi just redeemed a code from priority, I went to the website and it does not work?
O2: Hi Shiva 👋 Which code are you trying to redeem? What error message are you getting when you try to use it?
Customer: O2 Hi I am trying to redeem the Star Wars case and when I click redeem it just loads but the price does not go down
O2: Ah right, did you copy the code over and use it at the online checkout?
Customer: O2 Yes I did
O2: The codes ran out very quickly yesterday as the offer was so popular. We're sorry you missed out this time.
```
</details>

## q080 · AskPayPal · howto

**Q:** I received a phishing email pretending to be from PayPal. Where should I send it?

**Reference:** AskPayPal asked for the email to be forwarded to its phishing-report address (redacted in the dataset as __email__) and asked the customer to delete the screenshot they had posted.

<details><summary>gold conversation 166768</summary>

```
Customer: AskPayPal hey, check this awful spam I got 'pretending' to be you! #deleted #notfallingforit [link]
AskPayPal: Thanks for letting us know! Please forward the email to __email__. Kindly delete the screenshot as it cont... [link]
Customer: AskPayPal Thank you! I will do
AskPayPal: You're welcome! Have a wonderful day. :) ^JMG
Customer: AskPayPal You too! Thanks for acting so promptly and for providing the email address. I've forwarded on the two emails - I've had another! 🤔
```
</details>

<details><summary>gold conversation 435502</summary>

```
Customer: AskPayPal hi I have had a fake PayPal email in my inbox.would you like me to forward it to you too look at?if so where should I send it?thx
AskPayPal: Hey there! Thanks for bringing this to our attention. Please forward the email to __email__ and our teams ... [link]
Customer: AskPayPal Just sent it now.thanks
AskPayPal: Thanks for helping to make PayPal a safer place for all our users! Have a nice day! ^SB
Customer: AskPayPal Not a problem. And you too 😆
```
</details>

## q081 · AskPayPal · policy

**Q:** PayPal took money from my bank account instead of the payment method I chose. Why?

**Reference:** AskPayPal said the funds may not have been available in your preferred payment method to complete the payment.

<details><summary>gold conversation 608488</summary>

```
Customer: AskPayPal Thanks to your site using the wrong payment method, and ignoring a method I had chosen, my checking account is now overdrawn, and I can't pay bills. Really appreciate that.
AskPayPal: Hello. Thank you for reaching out to us, and sorry for the delayed response. If you can send us a DM with some clarification about the situation, as well as your PayPal email address, we would be happy to assist you with this. ^RR [link]
Customer: AskPayPal I resolved the issue myself by working overtime to make up the money taken from my checking account, though I am confused as to why the payment methods I selected were ignored
AskPayPal: Our apologies for the confusion! There is a chance that the funds weren't available in the preferred payment method to complete the payment. For further questions, feel free to send us a DM! :) ^RR [link]
Customer: AskPayPal I checked and made sure that the card I used had the funds, and it had double the amount available. Instead, it ignored that source and used my bank account
AskPayPal: There is also a chance that our security system may have prevented you from using this card when completing the payment. If you would like speak with us about this further, please send us a DM. ^RR [link]
```
</details>

## q082 · Safaricom_Care · howto

**Q:** How can I get an old M-Pesa statement?

**Reference:** Statements for the last 12 months are available via *234#; for older periods visit a Safaricom shop with your original ID for a printout at KSh 25 per page. Another agent said statements can't be sent to your phone and that the last 6 months are available by registering or logging in online.

<details><summary>gold conversation 205790</summary>

```
Customer: Safaricom_Care ,,can i get my Mpesa statement for August 2015, from date 7th to 11th same month?
Safaricom_Care: You can only get M-pesa statements for the last 12 months via *234#. For periods more than that...(Contd)
Safaricom_Care: ..you need to visit a Safaricom shop with your original for print out at kshs.25 per page.^WO
```
</details>

<details><summary>gold conversation 759610</summary>

```
Safaricom_Care: ...You can also get a print out from any Safaricom shop at Kshs. 25 per page. ^LA
Customer: Safaricom_Care My friend in Qatar we don't have safaricom shops, please.cant you send it to my phone number coz the mini statement shows today's transactions?.
Safaricom_Care: Hello, sorry the statement cannot be sent to your phone. Register/login here [link] to get your ...
Safaricom_Care: (cont)statement for the past 6 months as advised earlier.^DE
```
</details>

## q083 · Safaricom_Care · howto

**Q:** How do I stop Safaricom promotional text messages?

**Reference:** Dial *100# or *200#, choose Products and Services, then option 98 'Stop Safaricom Promotion SMS', and follow the prompts.

<details><summary>gold conversation 530118</summary>

```
Customer: I'll need Safaricom_Care to stop texting me almost every day about their offers.
Safaricom_Care: Hi, dial *100#OK or *200#OK, select Products and Services, Option 98&gt;Stop Safaricom Promotion SMS and follow prompts to Stop.^DA
Customer: Safaricom_Care I followed your instructions but I'm still receiving the texts 😑
Safaricom_Care: Kindly confirm via DM [link] if 0701***279 is the affected number. ^ST
```
</details>

## q084 · Safaricom_Care · howto

**Q:** How do I change the Wi-Fi name and password on my Safaricom fibre router?

**Reference:** Safaricom_Care said to log in at 192.168.100.1 (user root, password admin) and change it under settings. The customer got in using the password printed on the router.

<details><summary>gold conversation 573148</summary>

```
Customer: Safaricom_Care How do I change my wifi username and password for safaricom fibre
Safaricom_Care: Hi, once you login, select option for settings to change,Use url:192.168.100.1� user/acc:root� pass:admin .^CH
Customer: Safaricom_Care Thank you
Customer: Safaricom_Care Am getting "Incorrect account/password combination. Please try again."
Safaricom_Care: Share with us your account via DM [link] ^ED
Customer: Safaricom_Care I've been able to access it using the password on router
Customer: Safaricom_Care Thank you though
Safaricom_Care: That's great.^DN
Safaricom_Care: You are welcome. Good evening. ^IZ
```
</details>

## q085 · Safaricom_Care · policy

**Q:** Someone called saying they're from Safaricom and asked about my M-Pesa. How can I tell if it's really them?

**Reference:** Safaricom only contacts customers from 0722000000 (or 0729333333 during promotions). Don't share personal details with other numbers; report fraud by SMS to 333, free of charge.

<details><summary>gold conversation 602024</summary>

```
Customer: Good morning Safaricom_Care please flag this number 0701597056 for MPESA FRAUD. Thank you. [link]
Safaricom_Care: Hi, thanks for sharing with us the information. Safaricom contacts you from the number 0722000000 or 0729333333 (during ....
Safaricom_Care: promotions). If contacted by any other number, do not share your personal information with anyone or perform any task ......
Safaricom_Care: that might be requested of you. Instead, share with us the information via the fraud sms number 333 (free of charge) ^NG
Customer: Safaricom_Care Thank you. Have a nice day.
Safaricom_Care: Much appreciated Cheers! ^MU
```
</details>

## q086 · VerizonSupport · troubleshooting

**Q:** My Verizon Fios internet is down and the router still shows a red light after a reboot. What next?

**Reference:** VerizonSupport said to reboot the battery backup unit (BBU) by holding the Alarm Silence or Reset button for 15 seconds; it may beep and take a few minutes to reinitialize, so check the router after about 3 minutes.

<details><summary>gold conversation 106935</summary>

```
Customer: VerizonSupport internet just went out and router still on. Great fucking timing
VerizonSupport: We want you connected. Do you get a red internet light after rebooting the router? ^JRA
Customer: VerizonSupport Yes
VerizonSupport: Do you know where your BBU is located for a reboot so the data port get reinitialized? ^JRA [link]
Customer: VerizonSupport Yes
VerizonSupport: Let's reboot that unit, by holding down the Alarm Silence or Reset button for 15 seconds. ^TXA
Customer: VerizonSupport Should it only take a few seconds for it to come back online? With the green light next to system status?
VerizonSupport: The unit may beep and will be a few minutes for the ports to be reinitialized. Check your router after about 3 minutes. ^JRA
```
</details>

## q087 · VerizonSupport · troubleshooting

**Q:** My Verizon Wi-Fi keeps dropping during online games. What can I do?

**Reference:** VerizonSupport said it may be wireless interference and suggested rebooting the router so it moves to another channel, then testing again.

<details><summary>gold conversation 271121</summary>

```
Customer: The is not all as advertised. I drop connections and consequently lose matches daily. #stuckincontract
VerizonSupport: We hate to hear this. Are these connections over a wireless network? ^BCW
Customer: VerizonSupport Yes. and tech has been over multiple times, this time they sold me on a better plan but with contract, but this is even worse connectivity
VerizonSupport: It may be wireless interference. Does the internet light ever go red when you lose connectivity? ^JRA
Customer: VerizonSupport I don't know.. I'll look.. I'm paying 160 a month for the worst cable selection and bad internet. This is criminal
VerizonSupport: Thank you, if it is wireless interference try to reboot the router to put it on another channel then test your connection again. ^JRA
```
</details>

## q088 · McDonalds · product

**Q:** Is McDonald's bringing back Szechuan sauce?

**Reference:** McDonald's said it isn't coming back for good, but would return for a third round in more US locations that winter; participating restaurants were listed through their link.

<details><summary>gold conversation 67527</summary>

```
Customer: So... If you could make some you could make more, yes? #szechuansauce #RickandMorty [link]
McDonalds: Szechuan Sauce isn’t coming back for good, but it’ll be back for round 3. You can expect it in more US locations this winter. 😉
Customer: McDonalds Would it be bad form to start camping out now?
```
</details>

<details><summary>gold conversation 8529</summary>

```
Customer: I need this now!! [link]
McDonalds: You can get Obsauced with Szechuan Sauce at participating McDonald’s. Find the list here: [link]
Customer: McDonalds ....Micky my boy, I use the same link as the one you gave me. [link]
```
</details>

## q089 · marksandspencer · product

**Q:** Are Marks & Spencer's pumpkin Percy Pigs vegan?

**Reference:** No. M&S said they're suitable for vegetarians but not vegans (the customer pointed to beeswax).

<details><summary>gold conversation 100151</summary>

```
Customer: marksandspencer are tour pumpkin Percy pigs accidentally vegan?
Customer: marksandspencer They're not vegan 😨 please remove the beeswax!
marksandspencer: They're suitable for vegetarians but not vegans - we'll still have other treats you can enjoy in store!
Customer: marksandspencer 💔💔💔💔
```
</details>

## q090 · marksandspencer · policy

**Q:** The item I want is only in stock at another Marks & Spencer store. Can they send it to my local store or post it?

**Reference:** No. M&S said they can't transfer stock between stores or post from other branches; you'd have to go to that store (calling ahead to have it put aside), or order online for delivery to a store if it's in stock online.

<details><summary>gold conversation 528328</summary>

```
Customer: Hey marksandspencer, do you know where I can source one of these? There’s none left on your website. It’s my 9 month olds favourite and we just need a back up in case this one disappears. Thanks 🤞🏼 [link]
marksandspencer: Hi Zoe, according to our system the only store with any of these left now is our Trafford Centre branch. You would need to go to the store, or have someone go on your behalf as we can't transfer stock between stores 1/2
marksandspencer: Give them a call beforehand if you do wish to go, so they can pop one aside for you. That way you'll know it'll still be there if you decide to go :) 2/2
Customer: marksandspencer Hi thank you very much. I’ve just rang the Trafford centre and they said they have none left. Do you know the product number? Thanks.
```
</details>

<details><summary>gold conversation 590955</summary>

```
Customer: marksandspencer can I order an item of clothing over the phone from a non local store as it’s the only one that has said item in stock?!
marksandspencer: Hi Hannah, you can order from our website and have it delivered to the store of your choice. Hope this helps.
Customer: marksandspencer It’s out of stock online and none of my local stores have it
marksandspencer: We're not able to stock transfer or post out from other branches, Hannah. What is the item?
Customer: marksandspencer A wool coat [link]
marksandspencer: Thanks, Hannah. What size and colour are you looking for and whereabouts are you?
Customer: marksandspencer Camel, size 10 and I’m in Chichester
marksandspencer: Sorry Hannah the coat isn't available in stores either! Looks like its sold out quicker than expected. Hope you find another one you love soon. Apologies again! Thanks
```
</details>

## q091 · no company · unanswerable

**Q:** How do I reset my Netflix password if I can't access my email anymore?

**Reference:** Not covered: Netflix support isn't in the corpus. The assistant should say it has no Netflix support history.

Top BM25 hits (confirm none of them answers the question):

- 28.8 [SpotifyCares] conv 196620: Customer: SpotifyCares need some assistance - need to reset password but do not have access to the email anymore. / SpotifyCares: Hey there! Can you DM us your account's email address? We'll take a look /RB [link]
- 26.6 [AskPlayStation] conv 343864: Customer: AskPlayStation hi. So I have forgotten my PSNetwork password but no longer have access to log-in email account / AskPlayStation: Hi there. Let's look into that. Please check your DM's for further instructions.
- 25.7 [AskPlayStation] conv 691457: Customer: AskPlayStation I forgot the password to my psn acc, I have access to the email but I can't reset the pass beca / AskPlayStation: Hi there! We have sent you a DM with more details
- 25.6 [AskeBay] conv 373916: Customer: if you lose access to email account used for ebay and cannot remember password to change email address what ca / AskeBay: If you are unable to access the details for your old account, then you’re welcome to register for a new account
- 25.2 [AmazonHelp] conv 567430: Customer: Why do mysterious items keep appearing in my cart ? / AmazonHelp: That's strange! Does anyone else have access to your account? ^VF

## q092 · no company · unanswerable

**Q:** Will FedEx leave my package with a neighbour if I'm not home?

**Reference:** Not covered: FedEx isn't in the corpus. The assistant must not substitute UPS's delivery policies.

Top BM25 hits (confirm none of them answers the question):

- 22.1 [AmazonHelp] conv 50989: Customer: Just got an email from Amazon saying they delivered my package to a neighbour. I'm 15 feet away from the door. / AmazonHelp: I'm sorry they didn't knock. You can leave feedback here: [link] Were you able to get your package? ^AF
- 21.7 [ArgosHelpers] conv 635693: Customer: ArgosHelpers hi I bought a tv online last night and chose my delivery to be tomorrow🙈 but I just realised nobo / ArgosHelpers: Hi George. Could you DM me with your details and I will see what we can do. Thanks - Kate
- 20.7 [AmazonHelp] conv 102168: Customer: AmazonHelp I've come home to a 'we missed you' card saying my parcel is in the 'shed.' It was left out in my g / Customer: AmazonHelp Snail and a slug attached to it and it's wet through!!!!! Surely they should leave it with a neighb
- 20.4 [AmazonHelp] conv 791226: Customer: “logistics” delivery is dreadful. Received text “handed to resident” - I wasn’t in (my account says leave with / AmazonHelp: I am very sorry to hear this Simon. Can I ask, have you selected a safe place instruction for this order ple
- 18.9 [AmazonHelp] conv 653044: Customer: returned home today to find parcel left on doorstep in full view of street. No attempt to leave with neighbour / AmazonHelp: I am so sorry about your package! We would like to look into this with you in real-time. Please contact us v

## q093 · no company · unanswerable

**Q:** Does Starbucks give me a free drink on my birthday through the rewards app?

**Reference:** Not covered: Starbucks isn't in the corpus.

Top BM25 hits (confirm none of them answers the question):

- 27.9 [GreggsOfficial] conv 614850: Customer: GreggsOfficial Can I take a screenshot of my free hot drink voucher on the rewards app to use at the airport o / GreggsOfficial: Unfortunately Melika your account will have to be live to redeem any reward.
- 26.6 [GreggsOfficial] conv 710398: Customer: GreggsOfficial Can you use free drink codes from the rewards app at airports? Thanks :) / GreggsOfficial: Yes, they accept Greggs Rewards.
- 26.3 [SouthwestAir] conv 351811: Customer: What about a free birthday drink? My birthday is tomorrow! [link] / SouthwestAir: Hey, Jamie. We give Passengers over 21 years old a free drink on Halloween. So you're golden. Happy birthd
- 25.9 [SouthwestAir] conv 20843: Customer: SouthwestAir did yinz stop sending free birthday drink vouchers for rr members or do I just need to fly more 😂 / SouthwestAir: As long as your Rapid Rewards account # is in your reservation, drink coupons are sent after completing 10
- 25.8 [GreggsOfficial] conv 772414: Customer: GreggsOfficial give you a free breakfast on the app and then the app no longer works. My free coffee i earned  / GreggsOfficial: Sorry Carrie - we're working on getting the app and website back up and running, as soon as it does your

## q094 · no company · unanswerable

**Q:** How do I move my Instagram account to a new phone number?

**Reference:** Not covered: Instagram support isn't in the corpus.

Top BM25 hits (confirm none of them answers the question):

- 20.2 [ATT] conv 209359: Customer: Someone from New York ordered new iPhones from our AT&amp;T account. This better not have anything to do with  / ATT: Hi Regina, we don't like to hear that. Please send us a DM with your account number and contact info so we can look
- 19.4 [Ask_WellsFargo] conv 469190: Customer: #WellsFargo Thx for the to-do activity today: finding a new bank. Don’t ❤️ you charging $12.50 to move my $ fr / Ask_WellsFargo: Let me review your charge concern, Dawn. Please DM us with your full name, phone number, and address (no
- 18.6 [MicrosoftHelps] conv 35552: Customer: MicrosoftHelps Hi my email was deleted and now I can't access my Instagram account! Help? / MicrosoftHelps: Hi, Niall! Glad to assist you. When was the last time you were able to log in? What message comes up whe
- 17.9 [AskLyft] conv 135643: Customer: AskLyft how long to change phone #? locked out of account-lyft made me a 2nd account now-makes no sense / AskLyft: Please do not create a new account and follow the instructions at [link] to see how to change your phone number
- 17.6 [AskLyft] conv 820351: Customer: AskLyft I recently switched cell phone numbers, how Can I switch it on my account? / AskLyft: Hi! In order to update your phone number, please email our Support Team at [link] Be sure to do so from the ema

## q095 · no company · unanswerable

**Q:** Can I take my small dog in the cabin on a Ryanair flight?

**Reference:** Not covered: Ryanair isn't in the corpus. The assistant must not substitute other airlines' pet policies.

Top BM25 hits (confirm none of them answers the question):

- 23.7 [British_Airways] conv 347995: Customer: British_Airways can I bring a small dog from Paris to London in the cabin? and how much is it? thank you / British_Airways: Hi Daniele, I'm afraid you can't bring your dog on board, sorry. Please click on the following link for
- 22.7 [Delta] conv 672566: Customer: Delta Please give me advice about exporting dog. How can I make flight reservation and bring my dog to the cab / Delta: Hi there. Please see the Pet In Cabin restrictions via the following link. [link] *ALA
- 21.3 [AmericanAir] conv 375950: Customer: AmericanAir what would i need to do to travel with my small dog on the cabin? / AmericanAir: A reservation will need to be added for you pup, we can help with that. Here's link with more info about do
- 19.9 [SouthwestAir] conv 450326: Customer: A screaming toddler, a woman with a small dog and a guy who "loud sneezes". This SouthwestAir flight might be  / SouthwestAir: Woosah, Brian. Woosah. ^SH
- 19.6 [VirginTrains] conv 116881: Customer: VirginTrains hi Can I take my small dog in first class on the 1843 to Euston next Friday ? / VirginTrains: Of course you can, just keep them off the seat and on a lead 😀 ^PA

## q096 · no company · unanswerable

**Q:** How do I cancel my Disney+ subscription?

**Reference:** Not covered: Disney+ launched in 2019, after this 2017 dataset.

Top BM25 hits (confirm none of them answers the question):

- 21.7 [AskPlayStation] conv 688873: Customer: AskPlayStation how do i cancel my ps now subscription? Thank you / AskPlayStation: Glad to help. Follow the steps in the next link for instructions about how to cancel the subscription: [
- 20.7 [Postmates_Help] conv 709112: Customer: I want to cancel my subscription. I can't find how to do it in the app. / Postmates_Help: Hi there! You can cancel this under Settings. Scroll down to the Postmates Unlimited category and tap on
- 20.3 [AskPlayStation] conv 732767: Customer: AskPlayStation I need to cancel my PS Plus subscription but the website is in maintenance. Do you know another / AskPlayStation: Hi! Check out the next article for more info on how to cancel Auto Renewal for Subscription Services: [l
- 20.2 [AppleSupport] conv 774594: Customer: AppleSupport how do I cancel my Apple music trial there is no option to? / AppleSupport: Check out this article, it will provide the steps to cancel a subscription: [link]
- 20.1 [AmazonHelp] conv 754602: Customer: AmazonHelp how do I cancel my kindle unlimited and why is it so hard to find / AmazonHelp: I'm sorry you are having trouble canceling your Kindle Unlimited subscription! You can find how to manage yo

## q097 · AppleSupport · unanswerable

**Q:** What is the battery capacity of the iPhone 15?

**Reference:** Not covered: the iPhone 15 postdates the 2017 dataset. The assistant must not answer with older iPhone battery information.

Top BM25 hits (confirm none of them answers the question):

- 23.7 [AppleSupport] conv 511684: Customer: How can I check the battery capacity on my iphone? AppleSupport / AppleSupport: Hey there. Are you having trouble with the battery-life on your iPhone? Please provide some details, we'd 
- 19.5 [AppleSupport] conv 318792: Customer: AppleSupport Hi, may I check the battery health of my iPhone 6s? / AppleSupport: We'll be happy to help with the iPhone battery. Can you tell us what seems to be happening?
- 18.9 [AppleSupport] conv 763057: Customer: AppleSupport How can I check the overall battery health of my iPhone 6s Plus? / AppleSupport: Great question. iPhone monitors battery health and alerts you when your battery may need to be serviced. T
- 18.5 [AppleSupport] conv 660374: Customer: applesupport Can you help me check my iPhone 7’s battery capacity? It is running down in as little as 3 hours  / AppleSupport: We can definitely help you with your battery issue. DM us your iPhone model and iOS version so we can get 
- 18.2 [AppleSupport] conv 645359: Customer: AppleSupport guys how is it possible that #iOS11 has eaten ~12% of my batt capacity and the phone lasts 50% of / AppleSupport: We're happy to look into this with you. To get started, let's be sure your iPhone's battery isn't in need 

## q098 · AskPlayStation · unanswerable

**Q:** How much does Sony charge to repair a PS5 DualSense controller?

**Reference:** Not covered: the PS5 postdates the 2017 dataset. The assistant must not substitute PS4 repair information.

Top BM25 hits (confirm none of them answers the question):

- 24.1 [XboxSupport] conv 211213: Customer: Does the left thumbstick on anyone else's Xbox One Elite Controller seem a little loose? Had my controller for / Customer: And even if it does become faulty, not much I can do about it... XboxSupport [link]
- 20.5 [XboxSupport] conv 240973: Customer: XboxSupport my controller is showing it's in charge all the time on Xbox dashboard how can I fix this as I do  / XboxSupport: Gotcha. Just so we're on the same page, are you only seeing the icon that shows that your 1/2 ^TJ
- 20.2 [XboxSupport] conv 88047: Customer: XboxSupport Hi, I have an issue with my controller. Live chat isn't working, can you help? / XboxSupport: Hi there, to clarify, does this happen with all controllers or just with one specific controller? ^JS
- 19.9 [XboxSupport] conv 63947: Customer: XboxSupport doing some bs controller update, it failed and now my only working controller is bricked. WTF [lin / XboxSupport: Hi there. If you unplug the controller and remove the battery for 10 mins does it turn on again? ^JL
- 19.8 [AskPlayStation] conv 544959: Customer: AskPlayStation does Sony have a program that can repair my ps vita? The home button doesnt work but it still t / AskPlayStation: Hello Manuel. Let's look into that. Please check your DM's for further instructions.

## q099 · no company · unanswerable

**Q:** Does Tesla include free Supercharging with the Model 3?

**Reference:** Not covered: Tesla isn't in the corpus.

Top BM25 hits (confirm none of them answers the question):

- 22.9 [Uber_Support] conv 108938: Customer: Uber_Support will the Tesla Model 3 be eligible for UberSELECT or UberBLACK? / Uber_Support: Here to help, Lance! For detailed information on vehicle requirements check out this page here; [link]
- 22.4 [AskLyft] conv 120434: Customer: My lyft driver today is a Tesla Model S, I can get used to this / AskLyft: [link]
- 18.1 [AmazonHelp] conv 393616: Customer: Hey Does your Amazon Visa comes with prime free shipping? / AmazonHelp: The Amazon Rewards Visa does not include free Prime shipping. Benefit details can be found here: [link] ^MB
- 15.9 [Postmates_Help] conv 143661: Customer: My delivery driver just pulled up in a #Tesla? 🤔 / Postmates_Help: Clutch.
- 15.3 [AmazonHelp] conv 702581: Customer: does prime include video and kindle unlimited? / AmazonHelp: It does include Prime Video and Kindle Owners' Lending Library amongst many benefits. Please see this link f

## q100 · no company · unanswerable

**Q:** What is the time limit on free Zoom meetings?

**Reference:** Not covered: Zoom isn't in the corpus.

Top BM25 hits (confirm none of them answers the question):

- 15.7 [AppleSupport] conv 419414: Customer: AppleSupport can you not zoom the apps on the home screen on iPhone X? / AppleSupport: We'd love to help. To clarify, are you asking about the Display Zoom, or the Zoom accessibility feature?
- 15.5 [AppleSupport] conv 711644: Customer: AppleSupport what is this zoom button, where did it come from and how do I get it to go away???! [link] / AppleSupport: We can certainly take a look at this with you. If you go to Settings &gt; Accessibility &gt; Zoom, do you 
- 15.4 [marksandspencer] conv 467520: Customer: marksandspencer I presume this isn't supposed to have a time clock running on it at 51 seconds? Ooops. / marksandspencer: This is a zoom in on the child recording what they think is Santa on their phone. Sorry if it caused so
- 15.1 [SpotifyCares] conv 76490: Customer: . SpotifyCares why is there a limit on downloaded songs? Have 15hr flight- limit is making me anxious. What if / SpotifyCares: Hi there! At this time there is a limit of 3,333 offline songs per device. We have some more info for you 
- 15.1 [AppleSupport] conv 47522: Customer: there’s an issue with the accessibility zoom in IOS 11.0.2. / AppleSupport: What kind of issues are you having with the zoom feature? We'd love to help.
