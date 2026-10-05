<p class="footnote">* <span class="by-collab">The co-author with no memory is the AI agent (simply "the AI" below), or your oblivious supervisor.</span> <span class="by-ai">Either way, every session starts from scratch, so the glossary, the phrase bank and the structural rules below have to be handed over each time.</span></p>

<p class="footnote by-collab">† I was talking about this with my students, and wrote it down here so they can find it again and refer back to it.</p>

<aside class="checklist by-collab">
<p class="checklist-title">Checklist</p>
<p class="pass">Prepare</p>
<ul>
<li>Search the literature</li>
<li>Verify every reference (dblp → DOI)</li>
<li>Build a glossary, anchored to a reference text</li>
<li>Build a phrase bank</li>
</ul>
<p class="pass">Structure</p>
<ul>
<li>Define terms before using them</li>
<li>Use connectives: <em>However</em>, <em>Thus</em></li>
<li>Algorithms: idea → description → variables → pseudocode → proof</li>
<li>Split into small procedures</li>
<li>Motivation before results</li>
</ul>
<p class="pass">Polish</p>
<ul>
<li>No "this" or "that" references</li>
<li>One term per concept</li>
<li>Add reminders</li>
<li>Figures on the same or next page, with detailed captions</li>
<li>Simplify proofs</li>
</ul>
</aside>

<div class="by-ai">

Most advice about writing papers is about sentences. Most problems in papers are about something else: a term used three pages before it is defined, an algorithm shown as pseudocode with no idea behind it, a proof that says "this implies that" without saying what *this* is. None of these are problems of talent. They are problems of process, and process can be learned.

The process below works in passes. Each pass has one job: first prepare, then structure, then polish. AI is now good enough to help with every pass, but only if you know what the pass is for. So this post first describes the passes, then where AI fits into each one.

</div>

## Prepare: literature, glossary, phrase bank

<div class="by-collab">

Start by **searching the literature**. This is not only about citing related work. Knowing what has been done tells you what your contribution actually is, and it shows you the vocabulary your community already uses. A paper that invents its own words for standard ideas makes readers translate before they can understand. Tools that show papers as a network of citations help here: [Connected Papers](https://www.connectedpapers.com/) and [Research Rabbit](https://www.researchrabbit.ai/) show which papers cite which, and [Elicit](https://elicit.com/) finds and summarizes papers that answer a research question.

Next, **build a glossary**: a running list of every technical term in the paper, each with a one-line definition. The glossary forces a decision: one term for each concept. Once you have called something a *round*, it is never a *step* or a *phase* two sections later.

</div>

<details class="example">
<summary>Example: a glossary for <em>Asynchronous Dispersion with Optimal Time Complexity</em></summary>

<div class="by-collab">

Condensed from [the paper](https://arxiv.org/abs/2507.01298) (Pattanayak, Kshemkalyani, Kumar, Molla and Sharma, ICPP 2026).

| Term | Meaning |
|---|---|
| Graph | $G = (V, E)$ is simple, undirected and connected, with $n$ nodes, $m$ edges and maximum degree $\Delta$. |
| Anonymous graph | Nodes have no unique identifiers. |
| Port-labeled graph | At each node $v$, the incident edges carry distinct local labels (ports) $1, \dots, \delta_v$. The port at $u$ of edge $\{u, v\}$ is $p_{uv}$, and in general $p_{uv} \neq p_{vu}$. |
| Agent | One of $k \le n$ mobile agents $a_1, \dots, a_k$, each with a unique ID in $[1, k^{O(1)}]$. |
| Dispersion | The agents relocate until no node hosts more than one agent. |
| Rooted / general configuration | Initially, all agents are on one node / on at least two nodes. |
| Local model | An agent communicates only with agents at the same node. |
| CCM cycle | Communicate–Compute–Move: read the memory of co-located agents, compute, then write memory and exit through a port. |
| $\mathcal{SYNC}$ / $\mathcal{ASYNC}$ | Agents activate in common rounds / at arbitrary times, with every agent active infinitely often and every cycle finishing in finite time. |
| Epoch | A minimal interval in which every agent completes at least one CCM cycle. *Time* means rounds in $\mathcal{SYNC}$ and epochs in $\mathcal{ASYNC}$. |
| Memory complexity | The number of bits an agent stores from one CCM cycle to the next. |
| Settled agent, $\psi(x)$ | The agent that stays at node $x$. Its ID stands in for the ID of the node. |
| Edge type | t11, tp1, t1q or tpq: whether the edge has port 1 at both ends, only the far end, only the near end, or neither. |
| Port-one tree (P1Tree) | A tree in which every vertex has an incident tree edge of type t11, tp1 or t1q. |
| DFShead | The group of agents leading the depth-first search. |
| Vacated node | A visited node whose settled agent (a *settled scout*) travels with the DFShead, and returns in the retrace phase. |
| Parallel probing | Neighborhood search in which the agents at the DFShead probe the ports of the current node in parallel. |

</div>
</details>

<div class="by-collab">

Then **build a phrase bank**, a small set of fixed phrasings for the things you say again and again. In a paper about mobile agents on graphs, that might be:

> the agent moves from node $u$ to node $v$

Use that exact phrase every time, never "the agent goes to the neighbor" in one place and "node $v$ is reached" in another. Repeated wording can feel dull to write, but it is restful to read: the reader stops parsing sentences and starts following the argument.

</div>

## Structure: the order in which ideas arrive

<div class="by-collab">

A reader meets ideas one at a time, in the order you chose. Structure is about choosing that order well.

**Define terminology before using it.** This sounds obvious and is violated constantly, usually because a definition got moved during revision. The glossary helps here: for each term, check that its first use comes after its definition.

**Use connectives.** Words like *However* and *Thus* are the joints of an argument. They tell the reader whether the next sentence contrasts with, follows from or merely adds to the previous one. Without them, the reader has to guess the logic.

**Present each algorithm in layers**, from the outside in:

1. the high-level idea, in a few sentences;
2. a detailed description in prose;
3. the variables: what each one holds and how it changes;
4. the pseudocode;
5. the correctness proof.

A reader who stops after the first layer still leaves with something. A reader who goes all the way reaches the pseudocode already knowing what it is meant to do.

**Split the algorithm into small functions or procedures.** Each piece can then be described, and proved correct, on its own. A proof that says "by Lemma 3, `Explore` terminates" is much easier to check than one that reasons about a single hundred-line procedure.

**Put motivation before results.** Tell the reader why a problem matters before telling them what you achieved. The same rule shapes a good abstract, so follow an abstract-writing guide when you write yours. A good one is Neel Nanda's [Highly Opinionated Advice on How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers). Its annotated abstract shows the job of each sentence.

</div>

## Polish: removing every chance to misread

<div class="by-collab">

The last pass is about ambiguity: every place where a careful reader could take a sentence two ways.

**No "this" or "that" as a reference.** Name the object precisely. Compare:

> *Before:* It then moves there, and this guarantees termination.
>
> *After:* The agent then moves from node $u$ to node $v$. The move from node $u$ to node $v$ guarantees termination.

The second version is longer and cannot be misread.

**No two terms for the same thing.** If the reader sees *robot* in one paragraph and *agent* in the next, they will reasonably wonder whether these are different entities.

**Add reminders.** In a long paper, readers forget. Short signposts, like *Recall that …* or *As shown in Section 3, …*, cost a few words and save the reader from flipping back.

**Check figures and references.** A figure should appear on the same page where it is first referred to, or on the next page. Give each figure a detailed caption, so it can be understood without hunting through the text for an explanation. A LaTeX trick for placement: put each figure in its own file and include it with `\input{figures/p1tree}`. That one line decides where the figure lands, so move it up or down in the source until the figure sits on the right page.

**Simplify proofs wherever you can.** A shorter proof is easier to check, easier to trust and harder to get wrong. If a case analysis can be replaced by one invariant, replace it.

</div>

## Where AI fits

<div class="by-ai">

The rule for every pass is the same: **AI proposes, you verify.**

</div>

<div class="mixed">

- <span class="by-collab">**Literature search.**</span> <span class="by-ai">AI can produce references to papers that do not exist, so every citation needs checking.</span> <span class="by-collab">One way to verify a whole bibliography: ask the AI to take each reference from [dblp](https://dblp.org), then use the DOI to find the actual paper and check the metadata (authors, title, venue, year) against your entry. Do this for all your references.</span>
- <span class="by-collab">**Glossary.** A glossary can be built up across several projects rather than from scratch for each paper. For consistency, anchor it to a reference paper or book in your area and follow its terms.</span> <span class="by-ai">The AI can then check a draft against it: ask it to list every technical term, where it is first used and where it is defined, and to flag pairs of terms that seem to mean the same thing.</span>
- <span class="by-collab">**Phrase bank.** The phrase bank is a meta thing: technical phrases hide inside ordinary-looking sentences, so read the draft line by line to identify them. Then give the AI reference phrases, so that it knows moving from $a$ to $b$ is a technical phrase with a fixed form, not wording to paraphrase.</span> <span class="by-ai">Read its changes; don't accept them wholesale.</span>
- <span class="by-collab">**Structure.** Specify structural requirements at the beginning, before the AI drafts or revises anything: terms defined before use, the five layers for each algorithm, motivation before results.</span> <span class="by-ai">Afterwards, check with concrete questions, such as *Which terms are used before they are defined?* The AI is a dependable reviewer when the question is this specific.</span>
- <span class="by-collab">**Polish.** Polishing works as find-then-generalize: find one instance of a problem yourself, such as an unclear "this" or two terms for the same thing, then ask the AI to find all such instances and disambiguate each one.</span> <span class="by-ai">For proofs, the AI can suggest a simpler argument, but you must check every step yourself. A proof that reads well and a proof that is correct are not the same thing.</span>

</div>

### Prompts to copy

<div class="by-ai">

Replace the parts in square brackets.

**Verify references**

```text
For each reference in the bibliography below, find its dblp entry and its DOI. Open the DOI and check that the authors, title, venue and year match my entry. List every mismatch and every reference you could not find. Do not guess.

[paste the .bib file]
```

**Check terms against the glossary**

```text
Here is my glossary, then my draft. List (1) every technical term in the draft that is not in the glossary, (2) every term used before it is defined, with where it is first used and where it is defined, and (3) pairs of terms that seem to mean the same thing. Do not rewrite anything.

Glossary: [paste]
Draft: [paste]
```

**Keep fixed phrases fixed**

```text
These are fixed technical phrases in my paper. Never paraphrase them. Wherever the draft says the same thing in other words, replace it with the fixed phrase, and list each change.

Phrases: [paste]
Draft: [paste]
```

**Set the structure first**

```text
Follow these rules for everything you write or revise: define every term before its first use; present each algorithm as high-level idea, detailed description, variables, pseudocode, correctness proof; state the motivation before each result. If the draft breaks a rule, tell me where instead of silently rewriting it.
```

**Find all instances of one problem**

```text
Here is one problem in my draft: "[quote the sentence]". The problem is [for example: "this" does not name what it refers to]. Find every other instance of the same problem in the draft, and for each one propose a rewrite that names the precise object.

Draft: [paste]
```

</div>

### An AGENTS.md for your paper

<div class="by-ai">

Pasting prompts works for one task. For a whole paper, write the rules down once where the AI will find them. Many coding agents, such as Codex and Cursor, read a file called `AGENTS.md` at the start of every session; Claude Code reads `CLAUDE.md`, which can contain just the line `@AGENTS.md`. Either way, the file works as the memory the co-author lacks.

<a href="agents/writing-papers/AGENTS.md" download="AGENTS.md">Download AGENTS.md for writing papers</a>: this checklist and the advice above, written as instructions for an AI agent. Put it at the root of your paper's repository, next to `main.tex`, and keep `glossary.md` and `phrases.md` beside it. It tells the agent to verify every reference, follow the glossary and the phrase bank, report problems instead of silently fixing them, and keep a log of AI use for the disclosure. Edit it to fit your paper.

</div>

<div class="by-ai">

**Disclosure.** Venues increasingly ask how AI was used. A declaration like the one at the top of this post, kept as you work, makes that easy.

</div>

<div class="by-ai">

None of this replaces thinking about the problem. What AI can take over is the mechanical part of careful writing: consistency checks, reference hunting and first drafts of prose. That leaves more time for the part only you can do.

</div>

## More reading

<div class="by-ai">

- Neel Nanda, [Highly Opinionated Advice on How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers) (2025): paper structure, and an annotated abstract that shows the job of each sentence.
- Leslie Lamport, [How to Write a 21st Century Proof](https://lamport.azurewebsites.net/pubs/proof.pdf) (2012): hierarchically structured proofs, a method that makes it harder to prove things that are not true.
- Leslie Lamport, [How to Write a Proof](https://lamport.azurewebsites.net/pubs/lamport-how-to-write.pdf) (1993): the original case for structured proofs.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: editing instructions removed, the author's own later corrections applied, and capitalization and punctuation fixed.</p>

<p class="note">Checklist:</p>

<div class="by-human">

- Search literature
- Build glossary
- Build phrasing
    - agent move from node $u$ to node $v$
- Structure
    - define terminology before using
    - Connectives
        - However, Thus,
    - Algorithms
        - High level idea
        - Detailed description
        - Variable details
        - Pseudocode
        - Correctness proof
    - Split the algorithm into small functions/procedures
    - motivation follows before result
        - follow the abstract writing guide
- Polish
    - remove ambiguity
        - no this or that type of reference (use precise reference to an object, e.g., node $u$ )
        - no two terms meaning the same thing
    - add reminders
        - e.g., recall that, ...; in the section &lt;no&gt;;
    - ensure that figures and references are correct
        - Figures appear in the same page or the next page they are referred to
        - write detailed captions for the figures
    - Simplify proofs wherever you can

</div>

<p class="note">Notes on using AI at each step:</p>

<div class="by-human">

1. Lit search can be verified by asking AI to take the references from dblp; then use DOI references to actually find the paper and verify the metadata for all your references.
2. Glossary can be built throughout several projects, but use a reference paper or a book for consistency.
3. Phrase bank is a meta thing. Read line by line to identify these. Give the models some reference phrases so that they know "moving from a to b" is a technical phrase.
4. Structural changes can be specified in the beginning.
5. Polish is finding something and asking AI to find all such things and disambiguate.

</div>

<p class="note">On why this post exists, and its title:</p>

<div class="by-human">

This post is something I was talking about with my students. I just wrote it so that they can find it again and again and refer to it.

The co-author is the AI agent, or your oblivious supervisor.

</div>
</details>
