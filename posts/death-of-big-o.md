<div class="by-collab">

What theoretical computer scientists do, essentially, is hide big constant terms inside the big O notation. Now a
lot of software systems and algorithms are subject to massive optimization by automated research with language
models. So it has become a trend to push some obscure constants to smaller and smaller values, while the overall
complexity still hides behind a rather big O. But in practice, does any of it make anything faster?

</div>

## What the O hides

<div class="by-ai">

Recall the definition. $f(n) = O(g(n))$ means that there are constants $c > 0$ and $n_0$ such that $f(n) \le c \cdot g(n)$ for every $n \ge n_0$. The notation hides two numbers: the factor $c$, and the size $n_0$
from which the bound holds at all. An algorithm with a better exponent and an enormous $c$ or $n_0$ is faster only
on inputs that nobody will ever have.

Such algorithms have a name. Richard Lipton called them
[galactic algorithms](https://rjlipton.com/2010/10/23/galactic-algorithms/) in 2010: an algorithm that is
"wonderful in its asymptotic behavior, but is never used to actual compute anything." He also noted that they
"can lead to new methods, new directions, and sometimes can be made practical."

The field knows the difference. Virginia Vassilevska Williams, in her survey
[*On some fine-grained questions in algorithms and complexity*](https://people.csail.mit.edu/virgi/eccentri.pdf),
explains why fast matrix multiplication is set apart from "combinatorial" algorithms. The notion is not
well-defined, she writes, "however it roughly means that the runtime should have a small constant in the big-O,
and that the algorithm is feasibly implementable."

</div>

## Exponents that never run

<div class="by-collab">

Take the recent breakthrough in integer multiplication. The size of the integers you are multiplying does not
matter: you never get to use the speed-up, because the assumptions that underlie the breakthrough are impractical.

</div>

<div class="by-ai">

In 2019 David Harvey and Joris van der Hoeven gave an algorithm that multiplies two integers of $n$ bits in $O(n \log n)$ bit operations
([Annals of Mathematics, 2021](https://annals.math.princeton.edu/2021/193-2/p04)), the bound that Schönhage and
Strassen conjectured in 1971. It is a theorem about the exponent: the factor and the input size from which it
wins stay inside the O.

Matrix multiplication shows the trend in motion. The exponent $\omega$ is the smallest $\tau$ such that two $n \times n$ matrices can be multiplied in $O(n^{\tau + \varepsilon})$ operations for every $\varepsilon > 0$.
Its recent history:

- $\omega < 2.371339$: Alman, Duan, Vassilevska Williams, Xu, Xu and Zhou,
  [April 2024](https://arxiv.org/abs/2404.16349).
- $\omega < 2.371177$: Dupont et al. (Google DeepMind, with Alman and Vassilevska Williams), who solved the
  underlying optimization problem with machine learning methods refined by AlphaEvolve,
  [August 2026](https://arxiv.org/abs/2608.16884).

Each bound holds as $n$ tends to infinity, and the factor hidden in the O may depend on $\varepsilon$.

None of these algorithms will multiply a matrix in any computer. They are real mathematics, but they are progress
on the exponent and not on the running time.

Models also polish constants inside theorems. In
[*Early science acceleration experiments with GPT-5*](https://arxiv.org/abs/2511.16072) (November 2025), Sébastien
Bubeck reports that GPT-5 Pro, given a paper on gradient descent, improved its sufficient step-size condition from $\eta \le 1/L$ to $\eta \le 1.5/L$. The authors of the paper had meanwhile shown, in their second version, that $1.75/L$ is sufficient, and the first version had already shown that the property fails beyond $1.75/L$. Bubeck's own assessment is that the result "could probably have been achieved by some experts in the field
in a matter of hours."

</div>

## Where the speed comes from

<div class="by-collab">

I feel this is a transient period, where people are optimizing exponents that do not really matter. Real gains
in efficiency will come from models that optimize automatically by exploiting the processor architecture,
memory access at the system level, and operation pipelining on the CPU or GPU. I think that is where the gain lies.

Companies are under high pressure to optimize the inference stack for LLMs. So they will also optimize the
algorithms where the boundary conditions are relatively normal, for everyday use.

</div>

<div class="by-ai">

Two examples show what such gains look like.

- **FlashAttention** ([Dao et al., NeurIPS 2022](https://arxiv.org/abs/2205.14135)) computes exact attention
  with the same quadratic number of operations as before. It changes only the order of the work, in tiles, so
  that far fewer values move between the GPU's large memory and its small on-chip memory. The paper reports a
  $3\times$ speed-up on GPT-2 at sequence length 1K. No exponent changed.
- **AlphaDev** ([DeepMind, 2023](https://deepmind.google/discover/blog/alphadev-discovers-faster-sorting-algorithms/))
  used reinforcement learning to search for assembly code that sorts three to five elements. The routines went
  into the LLVM `libc++` standard library, with reported gains of up to 70% on short sequences and about 1.7% on
  sequences of over 250,000 elements. Sorting stayed $\Theta(n \log n)$, and the instructions got fewer.

In both cases the asymptotic analysis says nothing happened.

</div>

## Ultra fine-grained complexity

<div class="by-collab">

That leaves us in a situation where the big O notation is not really useful. Even an algorithm that is optimal in
big O terms may not be good enough. For example, a problem has an $\Omega(n \log n)$ lower bound, and an algorithm
runs in $O(n \log n)$, but the big O hides a constant like 100 or 1000.

I think the next task in most optimization strategies, and maybe in modern theoretical computer science, is to
move beyond the big O and optimize the constants that hide under it. This will be the new **ultra fine-grained
complexity**.

</div>

<div class="by-ai">

The name places it next to an existing field. Fine-grained complexity, in Vassilevska Williams's words, is built
on reductions "that focus on exact running times," but exact there means the exponent: it asks whether a
problem solvable in $O(n^2)$ time can be solved in $O(n^{2 - \varepsilon})$ for some $\varepsilon > 0$. The
constant in front stays hidden.

Precedents for exact constants exist. Princeton's algorithms course, following Sedgewick and Wayne, teaches
*tilde notation*: $f(N) \sim g(N)$ if $f(N)/g(N)$ converges to 1. Big O, in
[the course notes](https://www.cs.princeton.edu/courses/archive/fall15/cos226/lectures/study/14AnalysisOfAlgorithms.html),
is "similar in spirit to Tilde notation, but throw[s] away leading constants." So $\sim 2n$ and $\sim 3n$ are
different statements, while $O(n)$ covers both.

Median selection has been studied at exactly this level for decades. Finding the median of $n$ elements takes at
most $2.95n$ comparisons ([Dor and Zwick, 1995](https://eccc.weizmann.ac.il/report/1995/031)), and at least $(2 + 2^{-80})n$ minus lower-order terms (Dor and Zwick, SIAM J. Discrete Math. 2001; see
[OEIS A215476](https://oeis.org/A215476)).
Both bounds are $\Theta(n)$. The open question is the constant between 2 and 2.95, and it has stayed open for
about thirty years.

The hard part is the cost model. Comparisons are a clean unit for a median, but FlashAttention and AlphaDev won by
counting other things: memory transfers, instructions, pipeline stalls. A constant is only meaningful relative to
a model of the machine. So ultra fine-grained complexity would need cost models close enough to real hardware for
its constants to predict running times, and simple enough to prove theorems in.

</div>

<details class="original">
<summary>Original input</summary>

<p class="note">Lightly edited for coherence: dictated as one paragraph, split into paragraphs, with capitalization and punctuation fixed. "Exposed" is read as "exposés", "efficiency will gains" as "efficiency gains", "process architecture" as "processor architecture". The instruction about the draft and the research is kept as the request.</p>

<div class="by-human">

Write another blog post about the death of big O notation.

What theoretical computer scientists do is essentially hide big constant terms inside big O notations. Now that a lot of the software systems and the algorithms are subject to massive optimization by automated research using language models, it has become a trend to optimize some obscure constants into smaller and smaller values, so that the overall complexity still hides behind some rather big O notation. But in practice, does it make anything any faster?

For example, take the recent breakthrough in integer multiplication. It does not even matter what the size of the integers that you are multiplying is, to essentially avail that speed-up, because the assumptions that underlie these breakthroughs are impractical.

But I feel this is just a transient period where people are optimizing for exponents which do not essentially matter. Real efficiency gains will come from models automatically optimizing for gains by exploiting processor architecture and system-level memory access and operational pipelining on the CPU or GPU. I think that's where the gain lies. And as companies have high pressure to optimize the inference stack for LLM inference, they will also try to optimize the algorithms where the boundary conditions are relatively normal and for everyday use.

So that leaves us in a situation where big O notation is not really useful. What we really want is, even for optimal algorithms that are claimed in terms of big O notation: for example, an algorithm has $\Omega(n \log n)$ complexity, the big O is also $O(n \log n)$, but the big O hides a constant like 100 or 1000 or something. I think the next task in most of the optimization strategies is that we move beyond, and maybe move with modern theoretical computer science, to optimize these constants that hide under the big O notation. And this will be the new ultra fine-grained complexity.

This is what I want the blog to be about. Find some examples, also research some of the things in the background, search for exposés regarding these things, find exposés from famous fine-grained complexity researchers, and make a draft.

</div>
</details>
