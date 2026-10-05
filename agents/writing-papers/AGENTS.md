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

## Prepare: literature, glossary, phrase bank

### Literature and references

- **Never invent a reference.** You can produce papers that do not exist. Every citation you add or
  touch must be checked.
- To verify a reference: find its entry on [dblp](https://dblp.org), take its DOI, open the DOI, and check
  the authors, title, venue and year against the `.bib` entry. Report every mismatch and every reference
  you could not find. Do not fill in missing fields from memory.
- When searching for related work, say how you found each paper and whether you read it or only its
  abstract. Use the vocabulary the community already uses; don't invent new words for standard ideas.

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
- **Motivation before results**, in the paper, in each section and in the abstract.

## Polish: removing every chance to misread

Polish works as **find, then generalize**: the author points out one instance of a problem; you find every
other instance and propose a fix for each.

- **No "this" or "that" as a reference.** Name the precise object: not "this guarantees termination" but
  "the move from node $u$ to node $v$ guarantees termination". Longer is fine if it cannot be misread.
- **No two terms for the same thing** (check against `glossary.md`).
- **Add reminders** in long papers: *Recall that …*, *As shown in Section 3, …*.
- **Figures:** each figure appears on the page where it is first referred to, or the next page, and has a
  caption detailed enough to understand without the text. Keep each figure in its own file, included with
  `\input{figures/<name>}`, and move that line to fix placement.
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
