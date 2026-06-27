# Tiny Transformer From Scratch — Training Curriculum

A self-paced curriculum for building real understanding of transformers
*before* writing a line of the actual project. The goal: by the time the
build starts (whether that's solo or with an AI coding assistant), the
person doing it should be driving — able to ask "wait, why is this scaled
by `sqrt(d_k)`?" — not just watching it get built.

> Keep this file in the project root even after the build starts. It's the
> reference to come back to when something in the code stops making sense.

---

## Prerequisites

No prior LLM or ML knowledge is assumed — this curriculum is the on-ramp,
not a thing to complete before attempting it. What's actually needed
going in:

- **Basic Python.** Comfort with functions, loops, classes, and reading a
  stack trace. No ML libraries required up front — Phase 2 introduces
  PyTorch as part of the build itself.
- **High-school-level math comfort.** Specifically: what it means to
  multiply two matrices (dimensions lining up), what a probability
  distribution is, and derivatives at a conceptual level ("the slope says
  which direction to adjust"). Deriving anything by hand isn't required —
  Phase 0 builds the intuition — but if matrix multiplication itself is
  unfamiliar, a short refresher beforehand is worth it.

Not required, but helpful:

- **Having used an LLM as a end user** (ChatGPT, Claude, etc.) isn't
  technically necessary, but it gives useful intuition to anchor new
  concepts to ("oh, *that's* what's happening when I type a prompt").
- **No GPU or ML infrastructure experience is needed.** The Project Setup
  section below covers what's required, and scope is intentionally kept
  small enough to avoid needing real infra knowledge.

---

## How to Use This Document

- Work through phases **in order**. Each one assumes the last.
- For video resources: watch once passively (just absorb shape/intuition),
  then a second time *actively* — pause constantly, and if coding along,
  type every line by hand rather than copy-pasting.
- Don't move to the next phase until the current one's "Checkpoint"
  question can be answered out loud, in your own words, without notes.
- Rough total time investment: **20-30 hours** across all phases (15-20
  without Phase 0), spread out over days or weeks. Phase 2 alone is 6-8
  hours done properly — if it's taking less, the active pass is probably
  being rushed. This isn't a weekend project — let it breathe.

---

## Phase 0 — Neural Net Fundamentals (skip if not rusty)

Skip this phase entirely if already comfortable with "what is a gradient,
and why do we descend it" and basic backprop intuition.

- [ ] **[3Blue1Brown — "Neural Networks" series](https://youtu.be/aircAruvnKk)** (YouTube, ~4 videos, 1-2 hrs)
      The best visual intuition for gradient descent/backprop available.
      No code, pure intuition-building.
- [ ] **[Karpathy — "The spelled-out intro to neural networks and
      backpropagation"](https://youtu.be/VMj-3S1tku0)** (YouTube, ~2.5 hrs)
      Builds backprop from scratch in Python (micrograd). More hands-on
      than 3Blue1Brown — a good choice for anyone who wants the
      "build-it-yourself" version of fundamentals before moving on.

**Checkpoint:** Explain, without notes, what a gradient is doing when a
network "learns," and roughly why backprop is just the chain rule applied
mechanically.

---

## Phase 1 — Attention, Conceptually, Before Any Code

The goal of this phase is being able to explain what Q/K/V are doing and why
attention is "soft lookup" — entirely in plain English, no math required.

- [ ] **[3Blue1Brown — "But what is a GPT? Visual intro to Transformers"](https://youtu.be/wjZofJX0v4M)**
      (YouTube) — a 30,000-foot view of the architecture, with the best
      visual explanation of tokens-as-vectors available anywhere.
- [ ] **[3Blue1Brown — "Attention in transformers, visually explained"](https://youtu.be/eMlx5fFNoYc)**
      (YouTube) — the direct follow-up, focused specifically on what
      attention is doing geometrically (routing information between
      positions in a sequence).
- [ ] **[Jay Alammar — "The Illustrated Transformer"](https://jalammar.github.io/illustrated-transformer)** (blog post)
      The classic. Walks through the full architecture diagram piece by
      piece with diagrams. Recommended almost universally — treat this as
      required reading, not optional.
- [ ] *(Optional, for the encoder/decoder picture before the decoder-only
      GPT picture)* **[Jay Alammar — "The Illustrated GPT-2"](https://jalammar.github.io/illustrated-gpt2)** (blog post)
      Narrows Alammar's general transformer explanation down to the
      decoder-only architecture this project actually builds.

**Checkpoint:** In your own words — what are Q, K, and V? Why is attention
described as a "soft lookup" rather than a hard lookup? What problem does
multi-head attention solve that single-head attention doesn't?

---

## Phase 2 — Karpathy's Build, in Order

This is the centerpiece. Karpathy's video builds a GPT-like model from raw
Python up through a working character-level transformer, explaining every
line along the way.

- [ ] **[Karpathy — "Let's build GPT: from scratch, in code, spelled out."](https://youtu.be/kCc8FmEb1nY)**
      (YouTube, ~2 hrs)
      - **Pass 1 — Passive watch.** No coding along. Just absorb the shape
        of the thing: what sections exist, roughly what order pieces get
        built in, what the end result looks like running.
      - **Pass 2 — Active build.** Watch again, but pause constantly this
        time. Type every line by hand, don't copy-paste. Whenever something
        doesn't click, stop the video and sit with the "why this line"
        question before moving on — this is where the real learning
        happens, not the first watch.
- [ ] *(Reference while doing Pass 2)* **[nanoGPT repo](https://github.com/karpathy/nanoGPT)** (Karpathy, GitHub)
      The "official" cleaned-up version of what the video builds. Useful to
      diff a typed-along version against afterward — not to copy from.

**Checkpoint:** Sketch, from memory, the rough shape of a single transformer
block (attention → residual → feedforward → residual) and explain why
residual connections matter.

---

## Phase 3 — The Formal Version (optional but recommended)

Once there's working intuition from Phases 1-2, this phase connects it to
the "official" academic formulation and terminology — useful so that papers
and other people's code stop looking like a different language.

- [ ] **["The Annotated Transformer"](https://nlp.seas.harvard.edu/annotated-transformer)** (Harvard NLP)
      The original "Attention Is All You Need" paper, annotated line-by-line
      with executable PyTorch code inline. Denser and more academic than
      Karpathy's video — best done *after* Phase 2, as a "now see it the
      formal way" pass rather than a first introduction to the material.
- [ ] *(Optional, for the historically curious)* **["Attention Is All You
      Need"](https://arxiv.org/abs/1706.03762)** (Vaswani et al., 2017) — the original paper itself. Mostly
      useful at this point to see where the now-familiar terminology
      actually originated.

**Checkpoint:** Open the original paper's architecture diagram cold. Label
every box without looking anything up.

---

## Phase 4 — Bridging to the Actual Project

Before opening a code editor (or an AI coding assistant), get clear on what
this particular implementation is trying to teach, since "tiny transformer
from scratch" can mean several different scopes:

- [ ] Decide the **training corpus**. Something small and a little fun
      tends to keep motivation up (a body of commit messages, a favorite
      short text, Shakespeare as in Karpathy's example). Character-level,
      not word-level, to match what was just covered.
- [ ] Decide the **scope boundary** up front — e.g. "single GPU/CPU,
      character-level, a few hundred thousand parameters, train for minutes
      not hours." The goal is understanding, not a usable model — keep it
      tiny on purpose. A concrete signal that scope has crept too large: if
      training a single epoch takes more than ~5-10 minutes on your
      hardware, cut the model size or corpus until it doesn't. Slow
      feedback loops kill experimentation.
- [ ] Decide on **raw tensor operations** (recommended — keeps the math
      visible) vs. a higher-level library. Avoid `transformers`/
      `accelerate`-style libraries entirely for this project; they hide
      exactly the things it's meant to teach.
- [ ] Re-read Phase 2 notes/typed-along code once more, right before
      starting the real build, so it's fresh.

**Checkpoint:** State, in one or two sentences, what this project is *for*
— i.e. what question it's meant to answer — before writing the first line
of the real implementation.

---

## Project Setup (for later — briefing a coding assistant or collaborator)

Captured ahead of time so it's ready when the actual build starts. This is a
normal git-tracked, GitHub-hosted repo — "from scratch" refers to skipping
high-level ML abstraction libraries, not to avoiding standard dev tooling.

- **Language:** Python. The ML ecosystem, autograd, and GPU acceleration
  paths are overwhelmingly Python-first, and the reference material this
  curriculum points to is all Python — there's little reason to fight that
  with a different language for this particular project.
- **Core framework:** PyTorch — tensors + autograd only. The transformer
  architecture itself (attention, embeddings, blocks) is hand-written, not
  imported.
- **Explicitly excluded:** `transformers`, `accelerate`, `peft`, or any
  other high-level model library — they hide exactly what this project is
  meant to expose.
- **Hardware:** runs fine on a modern laptop, via CPU or a local GPU
  backend (e.g. PyTorch's MPS backend on Apple Silicon, or CUDA on
  supported hardware) — the model is small enough that no cloud GPU is
  required.
- **Model:** none pretrained or downloaded — a tiny model is trained from
  random initial weights on a small text corpus (see Phase 4). There's no
  model-serving component involved, unlike agent-style projects that wrap
  an existing local LLM.
- **Supporting tools:** `venv` or `uv` for environment management; a
  Jupyter notebook or plain `.py` scripts (notebooks are genuinely useful
  here for inspecting tensor shapes interactively while building);
  `matplotlib` optionally, for plotting the training loss curve; standard
  git/GitHub for version control.
- **Debugging texture, worth expecting:** bugs here are often shape
  mismatches (e.g. "expected `[B, T, C]`, got `[B, C, T]`") rather than
  control-flow/logic errors — a different debugging muscle than typical
  application code. Training also has a "wait and watch a number go down"
  phase that most software doesn't really have.

---

## Glossary (fill in while working through the curriculum)

A running scratchpad. Each time a term clicks, write a one-line definition
in your own words here — don't copy one from a textbook. If it can't be
written simply, it isn't understood yet.

| Term | Definition (in your own words) |
|---|---|
| Token | |
| Embedding | |
| Query / Key / Value | |
| Attention head | |
| Multi-head attention | |
| Positional encoding | |
| Residual connection | |
| Layer norm | |
| Feedforward block | |
| Causal mask | |
| Logits | |
| Temperature (sampling) | |

---

## Notes / Things That Were Confusing

*(Running log — add to this while working through the curriculum. Whoever
is debugging the actual project later will appreciate having a record of
exactly where the "aha" moments happened, and what almost-understanding
looked like right before them.)*

*(Example entry: "Phase 1 — kept conflating K and V. The thing that
unlocked it: K is what a word advertises about itself; V is what it
actually hands over once selected. They can be different because the
model learns them separately.")*

-
