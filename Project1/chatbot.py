"""
╔══════════════════════════════════════════════════════════╗
║           DecodeLabs AI Internship — Project 1           ║
║              Rule-Based AI Chatbot                     
║                  Batch: 2026                             ║
╚══════════════════════════════════════════════════════════╝
"""

# ─────────────────────────────────────────────
#  KNOWLEDGE BASE  (The Logic Skeleton)
#  Dictionary lookup: O(1) — not if-elif: O(n)
# ─────────────────────────────────────────────
RESPONSES = {
    # Greetings
    "hello":        "Hello! I'm DecoBot 🤖 — How can I help you today?",
    "hi":           "Hey there! 👋 What can I do for you?",
    "hey":          "Hey! Great to see you. Ask me anything!",
    "good morning": "Good morning! ☀️ Ready to learn something today?",
    "good evening": "Good evening! 🌙 Hope your day went well.",

    # About the bot
    "who are you":      "I'm DecoBot, a rule-based AI chatbot built during the DecodeLabs AI Internship (Batch 2026).",
    "what are you":     "I'm a deterministic chatbot — I follow hard-coded logic, not machine learning. Think of me as the 'white box' of AI!",
    "what can you do":  "I can respond to greetings, answer questions about AI, tell a joke, and much more. Try typing 'help' to see all commands!",

    # Help menu
    "help": (
        "\n📋 Available Commands:\n"
        "  hello / hi / hey          → Greet me\n"
        "  who are you               → About DecoBot\n"
        "  what is ai                → Learn about AI\n"
        "  what is rule based ai     → Rule-based AI explained\n"
        "  what is machine learning  → ML basics\n"
        "  what is deep learning     → Deep learning basics\n"
        "  tell me a joke            → I'll try 😄\n"
        "  time                      → Current date & time\n"
        "  creator                   → Who made me?\n"
        "  bye / quit / exit         → End the conversation\n"
    ),

    # AI Knowledge base
    "what is ai": (
        "Artificial Intelligence (AI) is the simulation of human intelligence by machines. "
        "It includes reasoning, learning, problem-solving, and decision-making. "
        "There are two main types: Rule-Based (deterministic) and ML-Based (probabilistic)."
    ),
    "what is rule based ai": (
        "Rule-Based AI uses explicit if-else logic defined by humans. "
        "It's a 'white box' — fully traceable, zero hallucination risk, "
        "and essential for compliance in finance & healthcare. That's exactly what I am!"
    ),
    "what is machine learning": (
        "Machine Learning (ML) is a subset of AI where systems learn from data "
        "instead of following hard-coded rules. It finds patterns and improves over time. "
        "Examples: spam filters, recommendation engines, image classifiers."
    ),
    "what is deep learning": (
        "Deep Learning is a subset of ML using neural networks with many layers. "
        "It powers GPT, image recognition, voice assistants, and more. "
        "It's the 'black box' side of AI — powerful but less explainable."
    ),
    "what is nlp": (
        "Natural Language Processing (NLP) lets computers understand human language. "
        "It powers chatbots, translators, sentiment analysis, and voice assistants."
    ),
    "what is a neural network": (
        "A neural network is a system inspired by the human brain. "
        "It consists of layers of nodes (neurons) that process data and learn patterns. "
        "Deep neural networks are the foundation of modern AI."
    ),

    # Fun / Personality
    "tell me a joke": (
        "Why do programmers prefer dark mode? 🌑\n"
        "Because light attracts bugs! 🐛😄"
    ),
    "are you smart":    "I'm deterministic — so I'm always right about what I know! 😎",
    "do you learn":     "Nope! I'm rule-based. I don't learn from data — a human has to update my rules manually.",
    "are you human":    "No, I'm DecoBot — a Python-powered rule-based AI. Fully transparent, zero mystery! 🤖",

    # Creator / Internship
    "creator":       "I was built by a DecodeLabs intern (Batch 2026) as Project 1 of the AI Industrial Training Kit.",
    "decodelabs":    "DecodeLabs is an AI training company based in Greater Lucknow, India. Website: www.decodelabs.tech",

    # Farewells
    "bye":       "Goodbye! Keep building awesome things! 🚀",
    "goodbye":   "See you later! Stay curious. 🌟",
    "quit":      "Exiting... Great session! 👋",
    "exit":      "Shutting down DecoBot. Farewell! 🤖",
    "see you":   "See you soon! Happy coding! 💻",
}

# Exit keywords — checked before dictionary lookup
EXIT_COMMANDS = {"bye", "goodbye", "quit", "exit", "see you"}


# ─────────────────────────────────────────────
#  PHASE 1: INPUT & SANITIZATION
# ─────────────────────────────────────────────
def sanitize(raw: str) -> str:
    """Normalize input: lowercase + strip whitespace."""
    return raw.lower().strip()


# ─────────────────────────────────────────────
#  PHASE 2: PROCESS — Intent Matching
# ─────────────────────────────────────────────
def get_response(clean_input: str) -> str:
    """
    O(1) dictionary lookup with a graceful fallback.
    Professional pattern: dict.get(key, default)
    """
    return RESPONSES.get(
        clean_input,
        "🤔 I don't understand that yet. Type 'help' to see what I can do!"
    )


# ─────────────────────────────────────────────
#  SPECIAL COMMANDS (require live data)
# ─────────────────────────────────────────────
def handle_special(clean_input: str) -> str | None:
    """
    Handle commands that need runtime data (e.g., time).
    Returns a string response or None if not a special command.
    """
    if clean_input == "time":
        from datetime import datetime
        now = datetime.now().strftime("%A, %B %d, %Y  |  %I:%M %p")
        return f"🕐 Current date & time: {now}"
    return None


# ─────────────────────────────────────────────
#  BANNER
# ─────────────────────────────────────────────
BANNER = """
╔══════════════════════════════════════════════════════════╗
║                  DecoBot  🤖  v1.0                       ║
║          Rule-Based AI Chatbot — DecodeLabs              ║
║      Type 'help' for commands  |  'exit' to quit         ║
╚══════════════════════════════════════════════════════════╝
"""


# ─────────────────────────────────────────────
#  PHASE 3: OUTPUT — The Heartbeat Loop
# ─────────────────────────────────────────────
def main():
    print(BANNER)

    while True:
        # ── INPUT ──
        try:
            raw_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nDecoBot: Interrupted. Goodbye! 👋")
            break

        # ── SANITIZATION ──
        clean_input = sanitize(raw_input)

        # Guard: ignore empty input
        if not clean_input:
            print("DecoBot: Please type something! 😊")
            continue

        # ── EXIT STRATEGY ──
        if clean_input in EXIT_COMMANDS:
            print(f"DecoBot: {RESPONSES[clean_input]}")
            break

        # ── SPECIAL COMMANDS ──
        special = handle_special(clean_input)
        if special:
            print(f"DecoBot: {special}")
            continue

        # ── PROCESS + OUTPUT ──
        response = get_response(clean_input)
        print(f"DecoBot: {response}")


if __name__ == "__main__":
    main()
