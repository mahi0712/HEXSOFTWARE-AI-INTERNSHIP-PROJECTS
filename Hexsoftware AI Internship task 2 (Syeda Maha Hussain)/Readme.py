# 🤖 AI Chatbot for Customer Support

**HexSoftwares Internship — Artificial Intelligence — Project 01**

## 📋 About
A simple, dependency-free AI chatbot that answers common customer support queries (order status, refunds, payments, working hours, etc.) using **predefined intents** and **basic NLP** (text cleaning + keyword/pattern matching). This is the same style of chatbot widely deployed on company websites for first-line customer support.

## ✨ Features
- Predefined intents: greeting, order status, refunds, payment issues, working hours, human handoff, thanks, goodbye
- Basic NLP text preprocessing (lowercasing, punctuation removal, whitespace normalization)
- Keyword-overlap based intent matching with substring fast-path
- Randomized natural-sounding responses per intent
- Fallback response when no intent matches
- Simple CLI chat loop for live testing

## 🗂️ File Structure
```
proj1_ai_chatbot/
├── chatbot.py          # Main chatbot logic + CLI demo
├── requirements.txt     # Dependencies (none external)
└── README.md              # This file
```

## 🚀 How to Run
```bash
python chatbot.py
```
Then type messages like:
```
You: hi
Bot: Hello! Welcome to our support chat. How can I help you today?

You: where is my order
Bot: You can track your order status by going to 'My Orders' in your account dashboard.

You: bye
Bot: Goodbye! Have a great day.
```

## 🛠️ Tech Used
- Python 3.8+
- Built-in `re` and `random` modules only (no external NLP libraries needed)

## 🔧 Extending This Project
- Add more intents to the `INTENTS` dictionary in `chatbot.py`
- Swap keyword matching with `scikit-learn`'s TF-IDF + cosine similarity for smarter matching
- Wrap `get_response()` in a Flask/FastAPI endpoint to connect it to a real website widget

## 📤 Submission Notes (as per HexSoftwares instructions)
- Push this code to GitHub with repo name: `HexSoftwares_AIChatbot`
- Share LinkedIn post with `@HexSoftwares` tag + video explanation
- Submit GitHub repo link via the internship submission form

## 🎯 Learning Goal
Hands-on experience building a rule-based conversational AI system using basic NLP techniques.
