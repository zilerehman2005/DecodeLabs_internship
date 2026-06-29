<div align="center">

# 🤖 DecoBot — Rule-Based AI Chatbot

### *DecodeLabs AI Industrial Training Kit | Project 1 | Batch 2026*

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Type-Rule--Based%20AI-00C896?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete%20✅-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

<br>

> *"Before you can manage the chaos of a probability engine,*
> *you must master the precision of a logic engine."*
> — DecodeLabs Architecture Briefing

<br>

```
╔══════════════════════════════════════════════════════════╗
║                  DecoBot  🤖  v1.0                       ║
║          Rule-Based AI Chatbot — DecodeLabs              ║
║      Type 'help' for commands  |  'exit' to quit         ║
╚══════════════════════════════════════════════════════════╝

You: hello
DecoBot: Hello! I'm DecoBot 🤖 — How can I help you today?

You: what is ai
DecoBot: Artificial Intelligence (AI) is the simulation of
human intelligence by machines...

You: tell me a joke
DecoBot: Why do programmers prefer dark mode? 🌑
         Because light attracts bugs! 🐛😄
```

</div>

---

## 📌 Table of Contents

- [About This Project](#-about-this-project)
- [The Architecture](#-the-architecture)
- [Project Specification](#-project-specification-the-logic-skeleton)
- [Features](#-features)
- [Getting Started](#-getting-started)
- [Available Commands](#-available-commands)
- [What I Learned](#-what-i-learned)
- [Project Structure](#-project-structure)
- [The Roadmap Ahead](#-the-roadmap-ahead)

---

## 🎯 About This Project

This is **Project 1** of the **DecodeLabs AI Industrial Training Kit**, completed as part of my AI Engineering internship. The goal was to build a **Rule-Based AI Chatbot** entirely from scratch using pure Python — no external libraries, no machine learning, no magic.

Before building systems that *learn on their own*, an AI engineer must first master the art of **teaching a machine through explicit logic**. This project is the foundation.

| Property | Details |
|---|---|
| 🏢 Organization | DecodeLabs (Batch 2026) |
| 🐍 Language | Python 3.10+ |
| 📦 Dependencies | None (stdlib only) |
| 🧠 AI Type | Deterministic / Rule-Based |
| ⚡ Complexity | O(1) Dictionary Lookup |
| 🔒 Safety | Zero hallucination risk |

---

## 🏗 The Architecture

This chatbot is built on the **IPO Model** — a foundational blueprint for transparent, controlled AI systems.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   USER INPUT  ──►  SANITIZE  ──►  PROCESS  ──►  OUTPUT │
│                                                         │
│   "HeLLo  "       "hello"       dict.get()    "Hi! 👋" │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Why a Dictionary, not If-Elif?

Most beginners write a tower of `if-elif` statements. Here's why that's an **Anti-Pattern**:

| Approach | Complexity | Maintainability | Status |
|---|---|---|---|
| `if-elif` ladder | O(n) — linear scan | High technical debt | ❌ UNSTABLE |
| `dict.get()` lookup | **O(1) — instant** | Just add a key-value pair | ✅ PROFESSIONAL |

The dictionary lookup is an **atomic operation** — it handles lookup *and* fallback in a single line:

```python
# ❌ Amateur approach — scans every rule
if user_input == "hello":
    reply = "Hi!"
elif user_input == "bye":
    reply = "Goodbye!"
# ... 20 more elif blocks

# ✅ Professional approach — instant O(1) lookup
reply = RESPONSES.get(user_input, "I don't understand that yet.")
```

### The 'White Box' Advantage

Rule-based systems are **fully transparent** — the opposite of a neural network black box:

```
// TRACEABILITY:  Input → Logic → Output. No mystery.
// SAFETY:        Zero hallucination risk. 100% hard-coded.
// COMPLIANCE:    Essential for Finance & Healthcare.
```

---

## 📋 Project Specification: The Logic Skeleton

All five checkboxes from the DecodeLabs specification — completed:

- [x] **INPUT LOOP** — Continuous `while True` cycle with clean exit handling
- [x] **SANITIZATION** — `.lower().strip()` normalizes all user input
- [x] **KNOWLEDGE BASE** — Dictionary with **10+ intents** (far exceeds the 5+ requirement)
- [x] **FALLBACK** — Default response for unknown inputs with a helpful prompt
- [x] **EXIT STRATEGY** — Clean `break` command on `bye`, `exit`, `quit`, etc.

---

## ✨ Features

- 🗣 **Smart Input Sanitization** — "HeLLo  " and "hello" are treated identically
- ⚡ **O(1) Lookup** — Dictionary-based response engine, not a slow if-elif ladder
- 💬 **10+ Intents** — Greetings, AI concepts, jokes, time, help menu, and farewells
- 🛡 **Graceful Error Handling** — Handles `Ctrl+C` and empty inputs without crashing
- 🕐 **Live Data** — `time` command returns the actual current date and time
- 🎨 **Formatted UI** — ASCII banner and clean labeled output in the terminal
- 🚫 **Zero Dependencies** — Runs on any machine with Python 3.10+, nothing to install

---

## 🚀 Getting Started

### Prerequisites

```bash
python --version   # Must be Python 3.10 or higher
```

### Installation & Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/rule-based-chatbot.git

# 2. Navigate into the project folder
cd rule-based-chatbot

# 3. Run the chatbot (no pip install needed!)
python chatbot.py
```

That's it. No virtual environment, no `requirements.txt`, no setup. Just pure Python.

---

## 💬 Available Commands

| Command | Response |
|---|---|
| `hello` / `hi` / `hey` | Greeting responses |
| `good morning` / `good evening` | Time-based greetings |
| `help` | Full command menu |
| `what is ai` | AI overview |
| `what is rule based ai` | Explains this chatbot's architecture |
| `what is machine learning` | ML basics |
| `what is deep learning` | Deep learning basics |
| `what is nlp` | Natural Language Processing |
| `what is a neural network` | Neural network explanation |
| `who are you` / `what are you` | About DecoBot |
| `tell me a joke` | A programmer joke 😄 |
| `time` | Current date and time |
| `creator` | Who built this bot |
| `decodelabs` | About the organization |
| `bye` / `exit` / `quit` | Graceful shutdown |

---

## 🧠 What I Learned

This project was more than just writing a chatbot. Here's the real depth behind it:

**1. The Two Minds of AI**
There are two fundamentally different AI paradigms: *Probabilistic* (ML/Neural Networks) and *Deterministic* (Rule-Based). You cannot appreciate one without understanding the other.

**2. Algorithmic Thinking**
Choosing `dict.get()` over `if-elif` is an algorithmic decision — O(1) vs O(n). This is the kind of thinking that separates a developer from an engineer.

**3. The IPO Model**
Every intelligent system, no matter how complex, follows Input → Process → Output. Internalizing this model makes designing any AI system clearer.

**4. Why Rules Matter in AI**
Modern AI (LLMs) run on probabilistic engines. But in production, they are always wrapped with a **rule-based guardrail layer** (like NVIDIA NeMo or Llama Guard) for safety and compliance. Project 1 is literally that guardrail layer.

**5. Software Design Principles**
Separation of concerns (sanitize → process → output), meaningful variable names, inline documentation, and writing code that another developer can read instantly.

---

## 📁 Project Structure

```
rule-based-chatbot/
│
├── chatbot.py        # Main application — the complete chatbot
└── README.md         # This file
```

Clean and simple. One file does one job perfectly.

---

## 🗺 The Roadmap Ahead

This is Project 1 of a series. Here's what's coming next:

```
Project 1 (✅ Done)   →   Rule-Based Chatbot      (Exact Key Match)
Project 2 (🔜 Next)   →   NLP Chatbot             (Semantic / TF-IDF Match)
Project 3 (🔜 Later)  →   ML Classifier           (Trained Model)
Project 4 (🔜 Later)  →   Deep Learning System    (Neural Networks)
```

Each project builds on the last. The dictionary key from Project 1 becomes a vector embedding in Project 2. The logic skeleton stays the same — only the intelligence grows.

---

<div align="center">

**Built with 💻 + ☕ during the DecodeLabs AI Industrial Training Program**

*"An LLM without rules is a hallucination engine.*
*Today, we build the skeleton that holds the intelligence."*

⭐ If this project helped you understand rule-based AI, drop a star!

</div>
