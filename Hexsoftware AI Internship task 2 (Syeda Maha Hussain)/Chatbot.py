
import re
import random

INTENTS = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening", "salam", "assalam"],
        "responses": [
            "Hello! Welcome to our support chat. How can I help you today?",
            "Hi there! What can I do for you today?",
        ],
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "thanks bye", "exit", "quit"],
        "responses": [
            "Thanks for chatting with us! Have a great day.",
            "Goodbye! Feel free to come back if you need anything.",
        ],
    },
    "order_status": {
        "patterns": ["order status", "track my order", "where is my order", "order tracking", "shipment status"],
        "responses": [
            "You can track your order status by going to 'My Orders' in your account dashboard.",
            "Please share your order ID and I can guide you on how to check its status.",
        ],
    },
    "refund": {
        "patterns": ["refund", "return item", "money back", "cancel order", "return policy"],
        "responses": [
            "Our refund policy allows returns within 7 days of delivery. Please visit the Returns section in your account.",
            "I can help with refunds — please provide your order ID to proceed.",
        ],
    },
    "working_hours": {
        "patterns": ["working hours", "open time", "business hours", "when are you open", "timing"],
        "responses": [
            "Our support team is available Monday to Saturday, 9 AM to 8 PM.",
            "We're open all week from 9 AM to 8 PM, except Sundays.",
        ],
    },
    "payment_issue": {
        "patterns": ["payment failed", "payment issue", "card declined", "unable to pay", "transaction failed"],
        "responses": [
            "Sorry to hear that! Please try again or use an alternate payment method. If the issue persists, contact your bank.",
            "Payment issues are usually resolved within a few minutes. Please retry, or share the error message you're seeing.",
        ],
    },
    "contact_human": {
        "patterns": ["talk to agent", "human support", "real person", "customer care", "speak to representative"],
        "responses": [
            "Sure! Connecting you to a live support agent. Please hold on.",
            "I'll transfer this chat to a human agent shortly.",
        ],
    },
    "thanks": {
        "patterns": ["thank you", "thanks", "appreciate it", "thanks a lot"],
        "responses": [
            "You're welcome! Is there anything else I can help with?",
            "Happy to help!",
        ],
    },
}

FALLBACK_RESPONSES = [
    "I'm sorry, I didn't quite understand that. Could you rephrase?",
    "I'm not sure I follow. You can ask me about orders, refunds, payments, or working hours.",
    "Could you please provide more details? I'm still learning!",
]


# ---------------------------------------------------------
# 2. Basic NLP - text cleaning
# ---------------------------------------------------------
def clean_text(text: str) -> str:
    """Lowercase, remove punctuation, and normalize whitespace."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ---------------------------------------------------------
# 3. Intent Matching
# ---------------------------------------------------------
def match_intent(user_text: str):
    """
    Returns the best-matching intent name based on keyword overlap,
    or None if nothing matches well enough.
    """
    cleaned = clean_text(user_text)
    user_words = set(cleaned.split())

    best_intent = None
    best_score = 0

    for intent_name, intent_data in INTENTS.items():
        for pattern in intent_data["patterns"]:
            pattern_clean = clean_text(pattern)

            # Direct substring match -> strong signal
            if pattern_clean in cleaned:
                return intent_name

            # Otherwise score by keyword overlap
            pattern_words = set(pattern_clean.split())
            overlap = len(user_words & pattern_words)
            if overlap > best_score:
                best_score = overlap
                best_intent = intent_name

    if best_score >= 1:
        return best_intent
    return None


# ---------------------------------------------------------
# 4. Response Generator
# ---------------------------------------------------------
def get_response(user_text: str) -> str:
    intent = match_intent(user_text)
    if intent:
        return random.choice(INTENTS[intent]["responses"])
    return random.choice(FALLBACK_RESPONSES)


# ---------------------------------------------------------
# 5. Chat Loop (CLI demo)
# ---------------------------------------------------------
def run_chat():
    print("🤖 Customer Support Bot (type 'bye' to exit)")
    print("-" * 45)
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        if match_intent(user_input) == "goodbye":
            break


if __name__ == "__main__":
    run_chat()
