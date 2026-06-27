# deadweights

> A tiny transformer trained from scratch on a CPU and a prayer. The weights start dead. Some of them stay that way.

![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-tensors%20only-EE4C2C?logo=pytorch&logoColor=white)
![Hardware](https://img.shields.io/badge/hardware-CPU%20%2F%20Apple%20Silicon-lightgrey?logo=apple&logoColor=white)
![Status](https://img.shields.io/badge/status-pre--training-yellow)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

---

A character-level transformer built from raw tensor operations — no pretrained weights, no high-level model libraries, no shortcuts. The point isn't a usable model. The point is understanding what's actually happening inside one.

Built with PyTorch for tensors and autograd only. Everything else — attention, embeddings, positional encoding, the transformer blocks themselves — is written by hand.

---

## Curriculum

Before any code gets written, there's a self-paced reading and video curriculum that builds the mental model first. The goal is to be *driving* the implementation, not just watching it get built.

**[tiny-transformer-curriculum.md](./tiny-transformer-curriculum.md)** — phases, checkpoints, and a running glossary. Keep this open while building; it's the reference to return to when something in the code stops making sense.

---

## Scope

Intentionally small:

- **Architecture:** decoder-only transformer (GPT-style)
- **Granularity:** character-level tokenization
- **Scale:** a few hundred thousand parameters
- **Training time:** minutes on a laptop, not hours
- **Hardware:** CPU or Apple Silicon (MPS backend) — no cloud GPU required
- **Corpus:** a small text dataset chosen in Phase 4 of the curriculum

**Explicitly excluded:** `transformers`, `accelerate`, `peft`, or any other high-level model library. They abstract away exactly what this project is meant to expose.

---

## Project Setup

*To be filled in when the build starts (Phase 4 of the curriculum).*

Prerequisites when that time comes:

```bash
python -m venv .venv
source .venv/bin/activate
pip install torch
# optional: pip install matplotlib  # for loss curve plotting
```

---

## Structure

```
deadweights/
├── README.md
├── tiny-transformer-curriculum.md   # read this first
└── ...                              # model code lives here once the build starts
```

---

## Acknowledgements

This project wouldn't exist without the work of people who put exceptional
effort into making these ideas genuinely teachable:

- **[Grant Sanderson (3Blue1Brown)](https://www.3blue1brown.com)** — for visual
  explanations of neural networks and attention that set the bar for what
  technical intuition-building can look like.
- **[Andrej Karpathy](https://karpathy.ai)** — for building everything from
  scratch, on camera, and making it feel approachable rather than intimidating.
- **[Jay Alammar](https://jalammar.github.io)** — for the illustrated walkthroughs
  of the transformer architecture that have become required reading for anyone
  learning this material.

---

## License

MIT
