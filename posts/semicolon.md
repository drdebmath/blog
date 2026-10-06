<aside class="checklist by-ai">
<p class="checklist-title">Pipeline</p>
<p class="pass">Song</p>
<ul>
<li>Lyrics that cover the syllabus</li>
<li>Suno inputs in several styles</li>
<li>Generate takes, pick one</li>
<li>Cut repeats on bar lines</li>
</ul>
<p class="pass">Picture</p>
<ul>
<li>Align lyrics, find the beat</li>
<li>Write a treatment</li>
<li>Make the cast on green</li>
<li>Write one brief for every scene</li>
<li>One file per scene</li>
<li>Check stills</li>
</ul>
<p class="pass">Ship</p>
<ul>
<li>Render in segments</li>
<li>Upload, link from the lecture</li>
</ul>
</aside>

<div class="mixed">

<span class="by-collab">During the midsem break of CS103 (Computer Programming, C++) in 2026, I made a music video for fun, after the midsem was over.</span> <span class="by-ai">It recaps Lectures 1 to 11: **Semicolon**, a three-minute Bollywood dance number about one missing character, now linked at the end of [Lecture 12](https://drdebmath.github.io/IITIJul2026CS103/).</span>

<span class="by-collab">The idea came from the viral p(doom) video. It took 11 hours in total. Once the pipeline was set up, the video part was mostly automatic. My time went into setting up the pipeline, choosing a catchy song among the candidates, and figuring out how to mix them.</span>

</div>

<div class="by-ai">

The template was [mexicat's take on the p(doom) video](https://x.com/_mexicat/status/2103108369569726802), posted
on X on 24 September 2026. I shared the result on X:

</div>

<blockquote class="by-human">

I used [@_mexicat](https://x.com/_mexicat) template to make a video for my programming course.
Overfitted bollywood in that.

Debasish Pattanayak ([@drdebmath](https://x.com/drdebmath)),
[5 October 2026](https://x.com/drdebmath/status/2106974006150873265)

</blockquote>

<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/7JqWeqbx_XQ" title="Semicolon: CS103 midsem recap" allowfullscreen></iframe></div>

<div class="by-ai">

The story is a masala film. The Compiler, a dacoit chief, rules a ravine of 203 errors. His bandolier of
semicolons has one empty slot, and no program in the land compiles. Semi, the lost semicolon, travels through
Bollywood set pieces with a gang of operators and variables. At the end Semi lands after `return 0`, the
program compiles, and the 203 errors go up as Diwali fireworks.

This post records the steps, so they can be repeated for the next course. The files named below (song inputs,
treatment, scene brief and scripts) live in the course's working folder.

</div>

## 1. Lyrics in four styles

<div class="by-collab">

I started by experimenting with different lyrics and different song styles, and only then mixed them.

</div>

<div class="by-ai">

The lyrics had one job: name the ideas of Lectures 1 to 11, one per line. They were written for
[Suno](https://suno.com) in *Custom* mode, where each song has four fields: title, style of music, styles to
exclude, and lyrics with section tags such as `[Verse 1]` and `[Spoken Word, deep villain voice]`. Four songs
were written, each in its own file:

| Song | Style | Language |
|---|---|---|
| Compile Kar Le | Bollywood comedy item song, dhol and shehnai | Hindi and English |
| Semicolon | Bollywood dance pop, built like "A.P.T.": one silly word as the hook | English |
| My P(Segfault) Is Rising | glossy synth pop, after the viral "I'm Upping My P(doom)" | English |
| One Brace, One Scope | anime ending theme, J-rock | English |

Two tricks made the vocals work:

- **Script decides pronunciation.** In the Hindi-English song, Hindi words are written in Devanagari and English
  words in Latin letters. Romanised Hindi gets English phonetics, so *the* would be sung as the English *the*.
- **Spell code the way it is sung.** `i++` becomes "i plus plus" and `cin` becomes "see-in". The on-screen text
  comes from a separate copy of the lyrics with real code in it.

</div>

## 2. Generate the song

<div class="by-ai">

Suno rarely gets a song right on the first take, and it often skips spoken-word tags. So each song was generated
several times.

</div>

<div class="by-collab">

Writing the Hindi words in Devanagari was not enough on its own. To make the Hindi vocals work, I had to submit
a voice recording to Suno.

Choosing among the candidates came down to which song was the catchiest: **Semicolon**. The other part that took
real thought was how to mix the songs together.

</div>

<div class="by-ai">

The final mix opens with the spoken intro of Compile Kar Le, a nod to *Sholay*: "कितने error थे?" "सरदार, दो
सौ तीन।" (How many errors were there? Two hundred and three, chief.) Then Semicolon starts.

Songs from the free plan are for non-commercial use only. A classroom video fits that; a monetised upload does
not.

</div>

## 3. Cut the repeats

<div class="by-ai">

Pop songs repeat their chorus more than a recap needs. A script (`edit_cuts.py`) removed three repeated blocks,
32 seconds in total, and brought the song down to about three minutes. Each cut works like a loop point in a
sampler:

1. Both ends of a cut lie on bar lines, a whole number of bars apart.
2. Among such pairs, pick the one where the 3 seconds around the start and around the end sound most alike
   (cosine similarity of log-mel spectra over the beat grid).
3. Align the join to the sample by cross-correlation, and blend it with a 0.12 s equal-power crossfade.

The point is that playback jumps between two moments that already sound the same, so the join is hard to hear.

</div>

## 4. Align the lyrics and find the beat

<div class="by-ai">

The video has to know when every word is sung. [Whisper](https://github.com/openai/whisper) transcribes the song
with word timestamps, but its transcript of a sung, half-Hindi song is not the lyrics. So `align.py` matches the
*written* lyrics to Whisper's words (a sequence diff) and takes the timestamps from the matches. The screen then
shows exactly the lyrics that were written, at the moment they are sung.

[librosa](https://librosa.org) supplies the rest: a beat grid at 136 BPM, the downbeat of every bar, the
sections, and loudness envelopes at 100 frames per second. Every cut, pose change and camera move in the video
lands on one of these.

</div>

## 5. Write a treatment

<div class="by-ai">

A treatment (`TREATMENT.md`) is the film on one page: the idea, the cast, the style rules, and one row per
scene with its time, lyric, what we see, the cast, the world and the beat moments. Its central rule is that the
lyrics are a **loose map, not a storyboard**. Each line names a C++ idea, and the scene shows a film situation
where that idea *happens* to the characters:

- The `int` box carries 3.7 across a river, and the `.7` falls overboard (truncation).
- A child variable `x` wanders out through brace-shaped fair gates and fades to a ghost (scope).
- A truck with no brakes rolls through every village on the road (`switch` without `break`).
- Two doubles try to marry, and the priest refuses: `0.1 + 0.2 != 0.3`.
- The `.at()` ticket inspector catches a passenger stepping off past the last coach (bounds checking).

The code on screen is correct C++.

</div>

## 6. Make the cast

<div class="by-ai">

The characters are drawn by ChatGPT as character sheets: several characters standing side by side on a pure
green (`#00FF00`) background. Two short scripts turn each sheet into sprites:

- `key_green.py` makes the green transparent. A pixel's alpha comes from how much greener it is than its other
  channels, and green spill on the edges is pulled back.
- `split_sheet.py` cuts the sheet at runs of fully transparent columns, so each character becomes one PNG.
  Parts of one glyph stacked vertically, like the two bars of `==`, stay together.

The cast: the Compiler and his henchman, Semi, a hero and a heroine with glowing laptops, the `++` twins, the
`==` sisters, the `&&` toll guard, the `<<` postman, the `>>` fisherman, and variables such as the `int` box,
the `const` statue and the `vector` train. Each has a few poses to swap on the beat.

</div>

## 7. One brief, one file per scene

<div class="by-ai">

The first engine was a lyric video in [three.js](https://threejs.org): one "station" per section, with the
camera flying between them. The final video instead uses a fork of pdoom-video, mexicat's
template from the post above (by Giacomo Magnanini, MIT license). Every background is a GLSL shader, and the
characters, props and lyrics are drawn on a canvas on top. There are no stock images.

Each scene is one TypeScript file, written by an AI coding agent from a shared brief,
`SCENES.md`. The brief says what a scene file looks like, which sprites exist, and the rules every scene
follows:

- Find lyric lines by their text, never by hard-coded times. The song can then be re-cut without breaking
  the scenes.
- Output depends on the song time only: seeded noise, never `Math.random()`. A frame can then be rendered on its
  own, in any order.
- Poses and hits land on beats or sung words, and the camera snaps on downbeats.
- Under 25 ms per frame.

A brief like `SCENES.md` is an `AGENTS.md` for one kind of file. The agent starts each scene with no memory, so
everything it needs is written down once, and the scenes come out consistent.

</div>

## 8. Look at the stills

<div class="by-ai">

The agent checked its own work by rendering stills: one frame per lyric line, plus the instrumental parts,
tiled into contact sheets. A contact sheet shows in one image whether the lyric covers a face, whether the
`;` lands on "line", and whether a cut is on the beat. The brief tells the agent to iterate until every frame looks like a
polished music video.

</div>

## 9. Render in segments

<div class="by-ai">

The renderer drives a headless browser frame by frame, with 4 sub-frames per frame for motion blur. A single run
over the whole song lost its page about 1,000 frames in. Since every frame depends only on the song time, the
fix was simple: render 30-second segments, each in a fresh browser (with one retry), join them losslessly, and
add the full song once at the end, so there are no audio seams.

The result is a 1080p, 60 fps master of 1.5 GB, and a 1080p, 30 fps web copy of 84 MB for YouTube.

</div>

## What carries over

<div class="by-ai">

None of the steps needed a studio, and most of them are a short script. The decisions that matter are the
lyrics, the choice of take, and the treatment's rule that each idea must *happen* on screen. Everything else
can be written down well enough for an agent with no memory to do it.

</div>

<div class="by-collab">

So the video part was mostly automatic. The 11 hours went into the pipeline and the song.

</div>

## What would have made it faster

<div class="by-collab">

The character sheets in ChatGPT and the song generations in Suno went through Codex computer use, which works
in one tab at a time. It does not use parallel tabs, and parallel tabs would have made the work much faster and
more hands-off. I said as much on X, on the
day I made the video:

</div>

<blockquote class="by-human">

i think computer use would go boom with multiple parallel cursor support with parallel tabs doing things. The
model can easily move a hundred cursors in different planes. For example a 100 apps, each with its own cursor.
Who is making this new OS?

Debasish Pattanayak ([@drdebmath](https://x.com/drdebmath)),
[3 October 2026](https://x.com/drdebmath/status/2106330823234572674)

</blockquote>

<div class="by-collab">

Reliability was the other problem. The subagents died several times, from internet errors, API errors and usage
limits, and each time a subagent's memory was lost with it:

</div>

<blockquote class="by-human">

API error is killing subagents and their memory is getting lost. Reliability has to go a long way for LLM
serving.

Debasish Pattanayak ([@drdebmath](https://x.com/drdebmath)),
[3 October 2026](https://x.com/drdebmath/status/2106363259381235766)

</blockquote>

<div class="by-ai">

A written brief makes such deaths cheaper. A new subagent can read `SCENES.md` and the treatment, and start the
scene again without anything from the old one. The same holds for the renderer: a segment that dies is rendered again,
and nothing else is lost.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: editing instructions about embedding posts from X removed (the post is quoted in the text instead), capitalization and punctuation fixed. The steps themselves come from the files in the course folder (song inputs, treatment, scene brief, scripts, logs and review stills).</p>

<div class="by-human">

See the video in the CS103 course folder for 2026 and write a blog post based on the steps taken there.

I made the video after the midsem. It was something fun I did during the midsem break. I spent 11 hours in total, while the video part was mostly automatic after setting up the pipeline, choosing a catchy song among the candidates and figuring out how to mix them. The idea came from the viral p(doom) video.

I also complained about the lack of parallel tabs in Codex computer use (for both the character sheets and the Suno generations), which I thought would have made my work much faster and more hands-off.

I initially experimented with different lyrics and different song styles. Then I mixed them. Then I had to submit a voice recording to Suno to make it work for the Hindi vocals.

The subagents died several times due to internet errors, API errors and usage limits.

</div>
</details>
