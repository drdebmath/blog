<div class="by-collab">

I built [Mobility Matters](https://drdebmath.github.io/mobility-matters/), a living survey of open problems on
autonomous agents, robots and particles. I built it to prepare for the results that AI models are about to
produce.

I had been thinking about building something like it for a while, and the recent OpenAI math results were a
wake-up call. If the future is about getting proofs for free, what makes them useful is putting them in
perspective.

</div>

<div class="by-ai">

Putting a proof in perspective means answering three questions about it: which setting it settles, which
other settings it carries over to, and what stays open after it. The atlas is built to answer all three.

</div>

## Why a map of open problems

<div class="by-collab">

Research is going to be democratic anyway. Anyone, anywhere, will eventually have access to a frontier model, or
to a model capable enough to contribute at the frontier of research. So why not start by enabling a random high
schooler to contribute to frontier research?

The problems that need attention should fall first. The compute is also a fixed budget, and it should not be
wasted: if $X$ tokens, or $X$ compute, are enough to solve a problem, then the cost should not grow to $100X$
because a hundred different people try the same thing.

So everything comes down to making research accessible. Mobility Matters is one way I am trying to do it. Anyone
can find the questions at the frontier by going through the assumptions and choosing their own branch. When they
succeed, they send a request to update the latest result for that problem under those assumptions.

</div>

<div class="by-collab">

The site also serves two other readers: undergraduates who are starting in the area, and researchers who are
returning to the field after a gap and need to catch up on the progress.

</div>

<div class="by-ai">

Each reader has an entry point. An undergraduate can start with *A first look* on a problem page and the
Perspectives essays, which explain why the models exist before they list bounds. A returning researcher can start
with the timeline, which dates every introductory result, current best and lower bound, and with
the progress map, which puts each lower bound next to the best upper bound and names the gap.

A map does two jobs here. It shows a newcomer where the open land is, and it shows everyone what has already been
claimed, so that nobody spends a month of compute proving a known bound again.

</div>

## What is on the map

<div class="by-ai">

The atlas covers four models: mobile agents on graphs, mobile robots in the plane, search in geometric domains
(linear search, evacuation, patrolling) and programmable matter. Inside them are six problem families and 51
problems, from exploration and dispersion to gathering, pattern formation, black hole search and leader election
among amoebots. The problems are split into 282 settings, 268 of them checked against the full text of their
papers, with 389 references. Eleven essays (*Perspectives*) connect the problems across models, and a ranked list
names the ten open questions whose answers would feed the most other problems.

For every setting the atlas records:

- the proven lower bounds, and what forces each one (its *bottleneck*, such as distance, symmetry breaking or
  indistinguishable Byzantine agents), with the assumptions its proof needs;
- the paper that introduced the setting, and the current best result;
- how far apart the two are: tight, near-optimal (a polylogarithmic gap), a polynomial gap, unknown, or
  impossible;
- the open questions, worded precisely.

</div>

## The assumption DAG

<div class="by-ai">

The central idea is that a problem is not one problem. Dispersion on a static graph with synchronous agents is
solved; dispersion on a temporal graph with asynchronous agents is a different question. So each model names its
**assumption axes**: graph dynamics, direction, timing, faults, communication, identifiers. Every axis is a scale.
Its lowest value assumes nothing (a temporal graph, asynchronous or silent agents, Byzantine faults), and each
higher value is a stronger assumption, which makes the problem easier.

</div>

<div class="by-collab">

The assumptions form a directed acyclic graph (DAG). Each end point of the DAG is a problem solved under the
assumptions that came before it as nodes.

</div>

<div class="by-ai">

The axes are independent, so a setting that assumes both a tree topology and a rooted start can be reached by
adding either assumption first: it has two parents. Each problem page draws its DAG, with every cited paper joined
to the settings where it gives a bound. A simpler tree view adds the axes in one fixed order, for browsing. Points
where the branches split but nobody has studied the setting are drawn dashed. These are honest gaps in the
literature, and anyone can open them.

Because the axes are ordered, results carry over without anyone writing them down. Thus an algorithm for a weaker
setting works in every stronger one, and a lower bound for a stronger setting holds in every weaker one. Every
setting's page lists the nearest settings in both directions.

*Choosing your own branch* is the [Explore](https://drdebmath.github.io/mobility-matters/#/explore) page: pick a model, a problem and a value per axis, and the atlas shows
the exact setting if it exists, the algorithms of the closest weaker settings and the lower bounds of the closest
stronger ones.

</div>

## A first look, for the high schooler

<div class="by-ai">

A map is no use if the reader cannot read the legend. So every problem opens with *A first look*, written for a
curious high-school student. Dispersion begins with $k$ electric cars arriving in a town where each charging point
serves one car and no car has a map. Then come two to four ideas, ordered by how useful they are to a newcomer: an
algorithm in a few numbered steps, or the situation an adversary builds for a lower bound, with a short counting
argument for why it works and how far it is from the best known result. Every technical word is defined.

</div>

## A website and a book

<div class="by-ai">

The atlas is a website and a book with the same content. The website is for finding things: a search box over
problems, settings, open questions, essays and references; the Explore page; a timeline that dates every
introductory result, current best and lower bound; and a progress map per problem that puts each lower bound next
to the best upper bound. It works on a phone. The book,
[mobility-matters.pdf](https://drdebmath.github.io/mobility-matters/mobility-matters.pdf), currently 535 pages, is
for reading and citing: models and their assumptions, the essays, every problem with its settings, all open
questions, an index of assumptions, the timeline and the bibliography.

Each model has one table of symbols, so a symbol means one thing inside a model, and a bound reads the same as in
the papers it cites. Every assumption has a precise definition and a short note on where it comes from.

</div>

## What makes it trustworthy

<div class="by-ai">

The atlas was compiled with Claude (Anthropic). A survey written with a model is only useful if a reader can trust
each line, so the rules are about evidence:

- **Read the full text.** A setting is marked *verified* only after its bounds are checked against the paper's
  model section and theorem statements, not the abstract. Abstracts have misstated settings: "asynchronous" for a
  semi-synchronous model, "common sense of direction" for a full compass. Unchecked entries are marked *draft* and
  say "as reported by".
- **Never invent** a reference, a venue or a bound, and cite only published papers and public preprints.
- **Ask, do not guess.** Questions of placement, naming and policy are decided by a person, not by the model.

Checking the full text pays off in small places. For example, the dispersion entry notes that several papers quote
a memory lower bound of $\Omega(\log(k + \Delta))$, but the $\log \Delta$ term has no published proof for
deterministic agents with identifiers.

One policy question was how to show results whose proofs are disputed. The answer:

</div>

<blockquote class="by-human">

Make disputed as another color. Don't show them as best.

</blockquote>

## The weekly update

<div class="by-ai">

A survey of a moving field is out of date the week after it is written. So the atlas updates itself once a week:

1. **Find new papers.** New papers on arXiv and OpenAlex are collected by keyword and by author (everyone cited
   at least twice in the atlas), together with Google Scholar alerts. Papers already in the atlas are dropped.
   This step uses no AI.
2. **Collect submitted results** from readers (see the next section).
3. **Read and place.** An AI agent triages the candidates, reads the relevant papers in full, and places each
   one: a better bound becomes the current best, a new set of assumptions becomes a new setting, a paper that does
   not fit yet goes under *Further reading*, and a new problem is proposed but not added.
4. **Check** that every citation resolves and every page and the book still build.
5. **Report.** Every change is listed as before and after, with the papers skipped and why, the papers behind a
   paywall, and the questions that need a decision.

Nothing goes online until a person has read the report. So the expensive step, reading a paper and checking its
theorems against a setting, happens once per paper, for every reader of the atlas.

</div>

## Submitting a result

<div class="by-ai">

Every problem page and every setting page ends with two links: **Suggest a result** and **Report an error**. Each
opens a [GitHub issue form](https://github.com/drdebmath/mobility-matters/issues/new/choose), with the problem and the setting already filled in. The result form asks for:

- the paper (title, authors, venue or arXiv id) and a link to the full text;
- the problem, and the setting, or the assumptions if the setting is new;
- the bound or impossibility, the theorem that states it, and the assumptions the paper makes;
- how the reporter wants to be acknowledged, and whether they are an author of the paper.

A third form suggests a new problem. Submitted results are read in the next weekly update, ahead of the papers it
finds itself, and each claim is checked against the linked paper, not against the text of the issue. Every issue
gets an answer: accepted, placed under *Further reading*, or declined, with the reason. Everyone whose result,
correction or suggested problem is accepted is listed on the atlas's [Acknowledgements](https://drdebmath.github.io/mobility-matters/#/acknowledgements) page, with the issue that
brought it in.

</div>

## Two other ways it could go

<div class="by-collab">

Mobility Matters is one way, and I think a promising one. Another way, less prominent but highly probable, is that
one of the big companies uses these problems as a test set for internal AI model development. Then they would
butcher the presentation of the results, and I would not be sure what exactly they are trying to show.

A third way is to verify all the research. Some of the results need to be formally verified, and some of the
assumptions in the community of mobile agents and robots are not encoded in a formal language. So perhaps the
second important project is to formalise these assumptions, so that anyone can build proofs on top of them.

</div>

<div class="by-ai">

The atlas already takes a first step. Every axis value carries a definition in the notation of its model, so
the assumptions are written down precisely, though in Markdown and LaTeX rather than in a proof assistant.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: the instruction to read the atlas's agent instructions and the files in the Research folder kept as the request, dictation errors fixed ("A research any is anyway" read as "Research is going to be democratic anyway", "Then nothing goes down to" as "Then everything comes down to", "send a request and get up to say what is the latest result" as "send a request to update the latest result"), capitalization and punctuation fixed.</p>

<div class="by-human">

Read the Mobility Matters agent instructions and check inside the Research folder for the details, and write a blog post about how the website is built. Later: write about how the weekly automatic update works and how people can submit their results as GitHub issues. The reason I wanted to build such a website is to prepare for the upcoming model-induced results.

I have been thinking about building something like this for a while, and the recent OpenAI math results are a wake-up call. If the future is about getting proofs for free anyway, what makes them useful is putting the proofs in perspective.

Research is going to be democratic anyway. Why not start by enabling the random high schooler to contribute to frontier research? If anyone anywhere is going to have access to a frontier model eventually, or a model capable enough to contribute at the frontier of research, then the problems that need attention should be falling first, and there is a fixed budget. We should not waste resources, in the sense that if $X$ amount of tokens is sufficient to solve a problem, or $X$ amount of compute is sufficient to solve it, then this $X$ amount of compute should not be overrun by a hundred different people trying to do the same thing.

Then everything comes down to how to make research accessible. One way I am trying to do it is by making this website, a survey called Mobility Matters, where anyone can get access to the questions on the frontier by going through the assumptions and choosing their own branch, and then, when they are successful, they can send a request to update the latest result in a particular problem under certain assumptions.

The idea is also to serve undergrads starting with the area, and to help researchers who are returning to the field after some gap, to keep them updated about the progress.

The assumptions are a DAG. Each end point of the DAG is a problem solved under the assumptions that came before it as nodes.

This is one way of doing it, and I think it is a promising way. The other, less prominent but highly probable way is using these problems as a test set for some internal AI model development by one of the big companies. Then they would butcher the presentation of the results, and I would not be sure what exactly they are trying to show.

Another way is to verify all the research. Some of the things need to be formally verified, and some of the assumptions that we have in this community of mobile agents and robots are not encoded in a formal form. So perhaps the second important project is to formalise these assumptions so that anyone can build proofs on top of them.

</div>
</details>
