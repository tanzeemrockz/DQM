# DQM (Deterministic Query Model)

A lightweight, trie-based lookup engine that traverses pre-built JSON "brains".

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[![Version](https://img.shields.io/badge/version-v2.1.0-blue.svg)](https://github.com/tanzeemrockz/DQM)

[![Python Version](https://img.shields.io/badge/python-v3-blue.svg)](https://python.org)

## What is DQM?

Instead of using power and resource-hungry, slow LLMs, We can now clear doubts using this lookup engine that walks through a pre-built "brain" (`.tqm` format).

**Try it out: [Official Page](https://dqm.cyberslayercorpz.dev/)**

## Overview

### Why does DQM exist?

You may ask, why does DQM exist? The short answer is, accuracy and speed. I was tired of seeing people using AI for the most  trivial things — "How hot is the sun? How deep is the sea?", these are in fact very simple questions and there should've been a better alternative. Sure, search engines exist for a reason but many people have stopped using them and moved over to AI — Search engines themselves are starting to implement AI **heavily** into them. I was tired of it providing wrong answers and making-up stuff that are simply – not real. So now, we have **DQM**.

### Our guarantees

We guarantee zero-hallucinations, fully predictable, and absolute offline capability. But any community-made brains are not guarenteed these qualities — as they will turn out to be the brain developers' fault.

## What's new in v2.1.0

### v2.1.0 Changelog

* A compatibility verification system to stop older/newer brains from malfunctioning on unsupported engines
* Standardised metadata for `.tqm` brains
* Normaliser that fixes contractions like `who's` and turns slang like `hiiiiiiii` into plain `hi`

## How it works 

* **Step 1 — Normalisation**: Lowercases, expands slang/contractions, removes repeated characters that serve no purpose, strips punctuation, and normalises delimiters.
* **Step 2 — Trie Traversal**: Splits the normalised queries into tokens and walks through the dictionary nodes.
* **Step 3 — Resolution**: Returns the string leaf, picks randomly if the leaf is an array, or throws clear status messages (`Path not found...` or `Incomplete query...`)

## The `.tqm` brain schema

Nothing fancy, just good ole JSON 

### Example:

```json
{
  "brain_id": "custom_core",
  "version": "1.0.0",
  "author": "John Doe",
  "info": "Rocket science, quantum physics, etc...",
  "description": "Custom brain for Rocket Science and Quantum Physics",
  "licence": "CC-BY-NC-SA-4.0",
  "compatibility": ">=2.1.0",
  "routes": {...}
}
```

## Quick start & CLI usage

* **Cloning and running:**

```bash
git clone https://github.com/tanzeemrockz/DQM.git
cd DQM
python main.py
```
* **CLI Commands:**
Interactive brain selector on startup, `cls/clear` clears the screen, and `exit/quit` to quit.

## Contributing & Brain Guidelines

You can follow the example brain snippet provided north of this section / take a look at `/brains/main.tqm` for reference on making your own brain. You shall either create a brain and create a PR to add to this repository / create your own GitHub repository.

## Credits & Licence

This code and the default `/brains/main.tqm` and any other brain added to this repository are ...are licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.

All code listed in this repository were made and are managed by **Mohamed Tanzeem I (a.k.a. CyberDev / tanzeemrockz)**

[CyberSlayerCorpz](https://cyberslayercorpz.dev)

