<aside class="checklist by-ai">
<p class="checklist-title">Build your own bridge</p>
<p class="pass">Ask</p>
<ul>
<li>State the goal, not the design</li>
<li>Answer the agent's questions on constraints</li>
<li>Say which features matter</li>
</ul>
<p class="pass">Run it</p>
<ul>
<li>Let the agent install the toolchain</li>
<li>Enable wireless debugging on the watch</li>
<li>Install, open, grant permissions</li>
<li>Paste back every error</li>
</ul>
<p class="pass">Live with it</p>
<ul>
<li>Complain about whatever feels wrong</li>
<li>Check the numbers it writes to Health</li>
<li>Ask what it sends, and how often</li>
</ul>
</aside>

<div class="by-collab">

I have struggled to use my Pixel Watch 2 because the battery in my Pixel 6a failed. Then I got an iPhone.

</div>

<div class="by-ai">

A Pixel Watch leans on its phone for setup, updates and notifications, so a failing phone meant a half-working
watch. The iPhone did not help on paper. Google's compatibility page says the Pixel Watch 2 needs Android 9 or
newer and states plainly: "iOS phones are not supported"
([Google Pixel Watch Help](https://support.google.com/googlepixelwatch/answer/12652073)). The companion app
that pairs and manages the watch exists only for Android.

</div>

<div class="by-collab">

None of this is an accident. The Pixel Watch was never planned to support iOS, just as the Apple Watch was
never planned to support Android. Each watch is built to keep you inside its own phone's ecosystem.

</div>

<div class="by-collab">

So I asked an AI coding agent to build an SDK that would let the watch work with the iPhone.

</div>

<div class="by-ai">

One evening later, the watch sends
heart rate and steps to Apple Health, shows my iPhone notifications and controls the music on the phone. Bedtime mode switches on at 22:00, and the first night of sleep stages
has come through. Workouts with GPS routes are built too, waiting for their first real run. The code lives in a folder on my laptop. Nobody else
runs it, and nobody else needs to.

This post records how the bridge was built, mostly by an AI coding agent (Claude Code, running Claude Opus 5.5),
and what it suggests about software in general.

</div>

<p style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap" class="by-ai">
<img src="img/personal-software/logo.png" alt="PixelBridge logo: an orange watch ring crossed by a white pulse line" width="150">
<img src="img/personal-software/tile.png" alt="The PixelBridge tile on the watch: iPhone connected, with Run, Music and Sleep buttons" width="190">
<img src="img/personal-software/watch-home.png" alt="The PixelBridge home screen on the watch, with Workout, Music, Route and Sleep" width="190">
</p>

## Thirty minutes to a first version

<div class="by-collab">

Claude built the MVP in 30 minutes: an iPhone SDK, a watch app, and the protocol between them.

</div>

<div class="by-ai">

The design came from the agent, after it listed what cannot be done. An iPhone cannot pretend to be an Android
phone, so the bridge does not try. Instead, the watch app opens its own Bluetooth Low Energy service, and an app
on the iPhone connects to it. Two Apple services do the rest without any iPhone app at all: the Apple
Notification Center Service (ANCS) gives the watch every iPhone notification, and the Apple Media Service (AMS)
lets it press play and skip.

| Feature | How |
|---|---|
| Heart rate, steps, energy, distance | Wear OS Health Services on the watch, HealthKit on the iPhone |
| Workouts with GPS route | Recorded on the watch, saved as an Apple Health workout with its route |
| Notifications, with answer and decline for calls | ANCS, straight from iOS |
| Music control, crown for volume | AMS, straight from iOS |
| Sleep stages | Raw heart rate and wrist motion overnight, staged on the iPhone |
| Bedtime mode at 22:00, off at 06:00 | The watch app flips the system setting itself |
| Settings from either device | A small `config` message over the same link |

</div>

## What was left to me

<div class="by-collab">

The slow part was everything around the code, and most of it fell to me. Downloading the SDKs took more time
than creating the app.

</div>

<div class="by-ai">

- **Toolchains.** The Mac had Xcode but no Java. A JDK, Gradle and the Android SDK (about a gigabyte) came
  through Homebrew, and Xcode then asked for its own components and platform downloads. The agent's sandbox let
  Java reach Google's servers but not GitHub, where Gradle's download redirects, so the agent fetched that file
  with `curl` and pointed the build at the local copy.
- **Wi-Fi debugging on the watch.** The watch charger carries no data, so every install goes over Wi-Fi. On the
  watch: tap the build number seven times to unlock Developer options, turn on ADB debugging and Wireless
  debugging, and pair with a six-digit code. The connection then uses a second port, which changes every time
  Wireless debugging restarts. So each session began with me reading a port number off the watch. Wireless
  debugging also keeps the radio on, and the watch ran out of battery once.
- **Xcode setup.** Sign in with an Apple ID (a free account works), let Xcode download its iOS components, and
  trust the developer certificate on the iPhone under Settings, General, VPN & Device Management. After that,
  the agent built, signed and installed the app from the command line, over Wi-Fi once the cable was gone.
- **Permissions and pairing.** On the watch: nearby devices, notifications, location, and body sensors with
  "allow all the time". On the iPhone: Bluetooth and Health.

None of these steps involve writing software. They are the toll for running software that no store distributes.

</div>

## Complaints as specifications

<div class="by-collab">

My prompts were not specifications. Most of them were complaints: the agent was planning instead of writing
code, the watch app looked poor and felt slow, the play button opened Apple Music instead of Spotify, I wanted
PixelBridge one swipe from the watch face, and the calorie count was too high.

</div>

<div class="by-ai">

Each complaint became a change in the code within minutes. The poor design became five screens and a tile.
The swipe became a Wear OS tile, the panel that appears when you swipe left from the watch face. The calorie
complaint was the most useful one, because the agent had the bug and I did not know the code. The
watch reports *total* energy, resting burn included, and the bridge had been writing all of it to Apple Health
as Active Energy. The fix has the watch learn my resting rate from its own quiet minutes, and split each minute
into Active Energy and Resting Energy.

</div>

## Where it broke

<div class="by-ai">

Nothing worked on the first try on real hardware, and every failure was specific:

- **The first crash** was a size limit. The iPhone negotiated large Bluetooth packets, and Android refuses any
  single notification longer than 512 bytes. The watch crashed on its first message, then again every time the
  iPhone reconnected.
- **The release build** crashed because the optimizer renamed fields that Health Services looks up by name.
- **The watch thought it was in Toronto.** It had kept the time zone of the Android phone it was set up with,
  so 22:00 would have meant 07:30 in India.

Some things could not be fixed. AMS controls whichever app iOS considers *Now Playing*, and cannot be pointed
at Spotify. Without Spotify Premium there is no other route, so the watch now refuses to send Play unless
Spotify is the current player, rather than waking Apple Music.

</div>

## The official story and the real one

<div class="by-collab">

The official instructions and what actually happened did not match. Google says the watch does not support
iOS, yet Google's own Health app on my iPhone was already showing the watch's data.

</div>

<div class="by-ai">

The watch explains the gap. Its Fitbit app (now called Google Health) uploads straight to Google's servers
over home Wi-Fi: the watch's network statistics show it sending about 120 to 180 KB every two hours with
no phone in the path. The Google Health app on the iPhone then reads that data back from the cloud. It never
talks to the watch. Since version 5.05, released in August 2026, it can also write steps, workouts, sleep and
some vital signs into Apple Health
([Khaleej Times](https://www.khaleejtimes.com/business/tech/how-to-sync-fitbit-and-pixel-watch-data-with-apple-health)).
That includes Fitbit's own sleep stages, which are better than anything the bridge can estimate from raw
sensors.

<figure style="text-align:center">
<img src="img/personal-software/iphone-dashboard.jpg" alt="The PixelBridge iPhone app: watch connected and synced, heart rate 70 bpm, 12,213 steps, no workouts yet, and a sleep card showing 6 h 3 m asleep from 11:48 PM to 5:51 AM, split into 2 h 24 m deep, 1 m core, 3 h 38 m REM and no time awake" width="300">
<figcaption>The iPhone app on 27 October. The sleep card is the bridge's own first estimate: one block of deep
sleep, then one of REM, and no time awake. Real nights cycle through the stages every hour and a half or so,
so this staging is wrong, which is one more reason to take sleep from Google Health.</figcaption>
</figure>

So "not supported" means something narrower than it sounds. The health data crosses over, through the cloud.
What does not cross is everything that needs the phone and watch to talk: notifications, calls, music,
settings, schedules. Those are exactly the parts the bridge provides, over Bluetooth, with Apple's own
notification and media services. Someone else built nearly the same bridge for a Pixel Watch 4
([drmhse.com](https://www.drmhse.com/posts/synchronizing-a-pixel-watch-with-an-iphone/)), with the same
conclusion about what can and cannot be reached.

The bridge now has a switch for this. With *Send health data* off, the watch stops recording heart rate,
steps, energy and sleep for the iPhone, and Google Health supplies them to Apple Health instead, without
duplicates. Workouts with GPS routes, notifications, music and the Bedtime schedule keep running through the
bridge.

</div>

## Asking what it costs

<div class="mixed">

<span class="by-collab">I asked how much data the watch sends the phone, whether all of it needs to go right away, and what could be stored and sent later.</span>
<span class="by-ai">The agent measured it from the iPhone's log: 461 readings in 18 minutes, about 27 per minute, or
2.7 MB a day, in a batch every one or two minutes. None of it needed to be live. The watch now holds readings,
rolls them into one value per minute, compresses them, and sends them once an hour, or when I open the iPhone
app. The estimate is about 50 KB a day and a few dozen radio wake-ups instead of over a thousand.</span>

</div>

## The era of personal software

<div class="by-collab">

PixelBridge is personal software. It was written for one person, one watch and one phone, and it will never be
published, because the value is entirely in the fit.

</div>

<div class="by-ai">

The economics used to forbid such software. A Bluetooth protocol, a Wear OS app, an iOS app, a sleep model and
a HealthKit integration add up to weeks of work for an experienced engineer, so only products with many users
could pay for them. A user with a rare combination of devices simply did without. Here the cost was one evening
of typing complaints, and the result does exactly what one person wants: Spotify and never Apple Music, sleep
from 22:00 to 06:00, health data once an hour.

</div>

<div class="by-collab">

The interface is no longer fixed either. It is generated, and regenerated, on demand.

</div>

<div class="by-ai">

The watch app started the evening as one plain list of buttons, and ended it as five screens and a tile.
Each version existed because a sentence asked for it. The settings appeared on the iPhone too, as soon as I
asked for them there. A generative interface, in this sense, is not a screen drawn
by a model at run time. It is an ordinary app whose design is cheap enough to throw away and ask for again.

Even the shelf life fits. An app signed with a free Apple ID stops opening after seven days, so PixelBridge has
to be rebuilt every week. For a product, the limit would be a disaster. For personal software, it is a
reminder of what the software is now: something made on the fly, for a purpose, and remade when the purpose
changes.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: capitalization and punctuation fixed, consecutive messages on the same topic joined, and only the prompts that shaped the bridge are kept (status updates, ports and confirmations removed). The post's facts come from the session itself: build and install logs, the iPhone app's sync log, and the code.</p>

<div class="by-human">

**Request for this post.** See the blog repo in Research and write a post about how I created this bridge between the Pixel Watch and the iPhone. The title is "The era of personal software". Then also allude to generative interfaces and software on the fly, or on demand.

**Background, added later.** Start with how I have struggled to use my Pixel Watch due to the failed battery in my Pixel 6a; then I got an iPhone.

**Correction, added later.** The Google Health app on the iPhone is already working with the Pixel Watch. Say that the official instructions were different from what happened. The Pixel Watch never planned to support iOS, and the Apple Watch never planned to support Android.

**Notes added later.** Claude did the MVP in 30 minutes. Write about what needed to be done by me, such as Wi-Fi debugging and the Xcode setup for creating the app. Downloading the SDKs took more time than creating the app.

**Prompts during the build.**

The objective here is to create an SDK such that I can use my Pixel Watch with my iPhone.

The final objective is to essentially create a bridge for me to sync the Pixel Watch with my iPhone. I will get data from the Pixel to my Apple Health. Plan accordingly. Do it fast.

You are not writing any code. You can write code while things download.

What can you do to find the sleep stage data? Can you export the entire data and then compute the sleep stage post facto on the iPhone?

Now it is a poorly designed watch app. Add options with multiple screens accessible from home to use the options. Add a logo in both the iOS app and the Pixel app.

Make a better looking iPhone app. The watch app is too slow.

Music on the watch still goes to Music on the iPhone. I want to have something such that the Spotify app on the watch can find the iPhone. Music commands are working but they go to the Apple Music app; I want a configuration to set Spotify.

Can you optimize the app and set bedtime on the Pixel Watch to 10 to 6? I want PixelBridge when I swipe from the home screen of the watch. I want these controls from the iPhone app.

How much data is the watch sending the phone every second/minute? Is that necessary? What can be stored and sent later? Yes. Can we do once an hour?

The calorie count is also counting inactive calories. Apple Health only takes active calories.

</div>
</details>
