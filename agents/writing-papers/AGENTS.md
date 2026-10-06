# AGENTS.md: writing a research paper

Instructions for an AI agent helping to write a research paper in this repository. Put this file at the
root of the paper's repository (next to `main.tex`), and edit it to fit your paper.

Based on "Writing Papers When Your Co-author Has No Memory" by Debasish Pattanayak, The Oblivious Robot,
https://drdebmath.github.io/blog/#co-author-with-no-memory, licensed under CC BY 4.0.

## The one rule

**You propose, the author verifies.** You have no memory between sessions, so everything you need is in
this file, `glossary.md` and `phrases.md`. Read all three before touching the paper. When you are not sure,
say so instead of guessing.

## How to work

The paper is written in passes, each with one job: **prepare**, then **structure**, then **polish**. Ask
which pass you are in if it is not clear from the request, and do only that pass's job.

Unless the author asks for a rewrite, **report problems instead of silently fixing them**: give the file,
the line or section, the problem, and a proposed fix. When you do edit, list every change you made.

**Work in parallel and finish fast.** Run independent jobs (for example a reference check) in the
background while you polish, review their results before applying them, and close long background work
quickly when the author asks.

## This paper: the authors' instructions

Record here every instruction the authors give about this particular paper, with its date, as soon as they
give it, and update the section after each new instruction. These instructions refine the general rules in
this file; where they are more specific, follow them. Typical entries:

- **Files:** which file is the working draft, its title, where the bibliography lives.
- **Shape of the paper:** the order of the contributions, which results are main results and which are
  remarks, what the introduction and the abstract open with.
- **Mathematics:** notation and conventions, for example how bounds are stated.
- **Citations:** the citation style, the bibliography order, works that must be cited and how to credit them.

## Prepare: literature, glossary, phrase bank

### Literature and references

- **Never invent a reference.** You can produce papers that do not exist. Every citation you add or
  touch must be checked.
- To verify a reference: find its entry on [dblp](https://dblp.org), take its DOI, open the DOI, and check
  the authors, title, venue and year against the `.bib` entry. Report every mismatch and every reference
  you could not find. Do not fill in missing fields from memory.
- When searching for related work, say how you found each paper and whether you read it or only its
  abstract. Use the vocabulary the community already uses; don't invent new words for standard ideas.
- **No unchecked claims about cited work.** Check every statement about a cited paper against its full
  text whenever it can be obtained, not only against the abstract. Record where the text was found and
  which pages were read, and mark every claim whose source was not accessible.
- **Credit correctly.** Attribute each idea to the work that introduced it, and the later improvements to
  the works that made them.
- **Citation style.** Write "First author et al." when a work has more than two authors, and name both
  authors when it has two. Full author lists appear only in the bibliography. Insert every new
  bibliography entry at its place in the bibliography's order (for example alphabetical by surname, then
  by year).

### Glossary (`glossary.md`)

A list of every technical term in the paper, each with a one-line definition, anchored to a reference
paper or book in the area (named at the top of the file). If the file is missing, offer to build it from
the draft.

- **One term per concept.** Once something is a *round*, it is never a *step* or a *phase*. Once it is an
  *agent*, it is never a *robot*.
- When checking a draft, list (1) every technical term not in the glossary, (2) every term used before it
  is defined, with where it is first used and where it is defined, and (3) pairs of terms that seem to mean
  the same thing.
- Don't add terms to the glossary yourself; propose them.
- Keep `glossary.md` and `phrases.md` current after every pass: section numbers, new terms, and the status
  of every finding (resolved or open, with line numbers). Mark the entries as proposals until the authors
  accept them.

### Phrase bank (`phrases.md`)

Fixed phrasings for things the paper says again and again, for example:

> the agent moves from node $u$ to node $v$

- **Never paraphrase a fixed phrase**, even to avoid repetition. Repeated wording is restful to read.
- Wherever the draft says the same thing in other words, replace it with the fixed phrase and list each
  change.
- Technical phrases hide inside ordinary-looking sentences. If you spot a phrasing that recurs and looks
  technical, propose it for the phrase bank.

## Structure: the order in which ideas arrive

Follow these rules for everything you write or revise. If the draft breaks one, say where.

- **Define every term before its first use.** Definitions often get moved during revision; check after
  every structural change.
- **Use connectives** (*However*, *Thus*, *Hence*, *In contrast*) so the reader knows whether a sentence
  contrasts with, follows from or adds to the previous one.
- **Present each algorithm in five layers**, in order:
  1. the high-level idea, in a few sentences;
  2. a detailed description in prose;
  3. the variables: what each one holds and how it changes;
  4. the pseudocode;
  5. the correctness proof.
- **Split algorithms into small procedures**, each described and proved correct on its own, so a proof can
  say "by Lemma 3, `Explore` terminates".
- **Motivation before results**, in the paper, in each section and in the abstract. The abstract opens
  with one sentence of practical motivation, and uses glossary terms only, with no term that describes none
  of the results.
- **A gradual climb.** When the paper has several contributions, order them so that each one removes the
  bottleneck of the previous one, and present them in that same order in the introduction, the overview
  of techniques and the body.
- **An informal overview of techniques**, right after the introduction (or after related work): high level
  and compressed, saying at its start that it is informal. Each paragraph opens with a challenge and
  continues with how the paper overcomes it.
- **Main results first, side results as remarks.** Rank the results. Side results become remarks, not
  subsections; remove results that are never used.
- **Representative headings.** Every heading says what its section contains; avoid generic titles
  ("Results", "The protocol", "Upper bounds"). Combine short related subsections into one, and inside it
  use lighter structure instead of more subsections: a numbered list, paragraphs whose first sentence
  states their topic, or italic lead-ins.
- **No overclaiming.** Statements about the literature avoid "always" and "most" unless a source supports
  them.

## Polish: removing every chance to misread

Polish works as **find, then generalize**: the author points out one instance of a problem; you find every
other instance and propose a fix for each.

When asked to polish, do **at least three rounds**, each with one focus: (1) "this"/"that" references,
glossary terms and fixed phrases; (2) definitions before first use, connectives and the order of ideas;
(3) the precision of every claim against the theorem or source it rests on.

**Compression is part of every polishing pass:**

1. **Identify repetitions:** list every idea, result or caveat that the paper states more than once, with
   all its locations.
2. **Find the best presentation:** for each repeated idea, pick the place where it is already stated best.
3. **Minimize the text:** keep that presentation, and shorten or remove the others. A distant section gets
   at most a brief reminder (*Recall that …*) or a reference. The idea must still come across in full.
4. **Results: core first, then enrichment.** State each result first at its core (the main bound in one
   sentence), then enrich it step by step (refinements, tightness, special cases, comparisons with earlier
   work).
5. Report the inventory of repetitions and the word count of each section before and after.

- **No "this" or "that" as a reference.** Name the precise object: not "this guarantees termination" but
  "the move from node $u$ to node $v$ guarantees termination". Longer is fine if it cannot be misread.
- **No two terms for the same thing** (check against `glossary.md`).
- **Add reminders** in long papers: *Recall that …*, *As shown in Section 3, …*.
- **Figures:** each figure appears on the page where it is first referred to, or the next page, and has a
  caption detailed enough to understand without the text. Keep each figure in its own file, included with
  `\input{figures/<name>}`, and move that line to fix placement. Use colour-blind-safe colours, together
  with line styles (dashed, double, grey) that carry the same meaning, and define the styles once in the
  preamble.
- **No additive constants in asymptotic bounds.** Write $O(m)$, not $O(m+1)$: state the range of the
  parameters once (for example $n \ge 2$) instead. Keep exact counts and factors whose 1 carries a term of
  the bound, such as $m(1+\Delta/k) = m + m\Delta/k$.
- **Check every cross-reference** (`\ref`, `\cite`, `\eqref`) resolves to what the text claims.
- **Simplify proofs** where you can (e.g. replace a case analysis with one invariant), but mark every
  proposed proof change clearly. The author checks every step: a proof that reads well and a proof that is
  correct are not the same thing. Never present a proof as checked when you have not checked it.

## Don'ts

- Don't invent references, results, numbers, experiments or quotes.
- Don't change the meaning of a claim, theorem or definition while "improving the wording".
- Don't rewrite whole sections when asked for a local fix.
- Don't accept your own changes on the author's behalf: they read every change.

## Disclosure

Venues increasingly ask how AI was used. Keep a running log in `ai-use.md`: the date, the pass, what you
were asked to do, and what you changed. The author can turn it into the paper's AI-use declaration.
