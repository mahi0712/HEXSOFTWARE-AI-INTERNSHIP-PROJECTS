# Emotion from Text Detector

A simple Python tool that analyzes text and detects the underlying emotion using **TextBlob**'s sentiment analysis (polarity + subjectivity).

Built as part of the **Hex Softwares Internship** (Python Programming track).

---

## 📌 What It Does

- Takes text input — either typed directly or read from a `.txt` file (line by line)
- Calculates two scores using TextBlob:
  - **Polarity** → ranges from `-1` (very negative) to `+1` (very positive)
  - **Subjectivity** → ranges from `0` (factual) to `1` (opinion-based)
- Maps the polarity score to a human-readable **emotion label**:

| Polarity Range | Emotion            |
|-----------------|---------------------|
| `> 0.5`          | Very Happy 😄       |
| `0.1` to `0.5`   | Happy 🙂            |
| `-0.1` to `0.1`  | Neutral 😐          |
| `-0.5` to `-0.1` | Sad 🙁              |
| `< -0.5`         | Very Sad / Angry 😠 |

---

## 🛠️ Requirements

- Python 3.7+
- `textblob` library

## ⚙️ Installation

```bash
pip install textblob
python -m textblob.download_corpora
```

---

## ▶️ How to Run

```bash
python 2_emotion_text_detector.py
```

You'll see a menu:

```
Emotion from Text Detector
1. Analyze typed text
2. Analyze a .txt file (line by line)
Enter choice (1/2):
```

### Option 1 — Analyze typed text
Type any sentence and press Enter. The result (polarity, subjectivity, emotion, tone) is printed instantly. Type `exit` to quit.

### Option 2 — Analyze a text file
Provide the path to a `.txt` file. Each non-empty line is treated as a separate piece of text and analyzed individually.

---

## 📷 Example Output

```
Enter text: I absolutely love how this project turned out!

--- Analysis Result ---
Text        : I absolutely love how this project turned out!
Polarity    : 0.62  (-1 = very negative, +1 = very positive)
Subjectivity: 0.75  (0 = factual, 1 = opinion)
Emotion     : Very Happy 😄
Tone        : Opinion-based
------------------------
```

---

## 📁 Project Structure

```
emotion-text-detector/
├── 2_emotion_text_detector.py   # main script
└── README.md                    # this file
```

---

## ✍️ Notes

- Emotion detection here is based on a simple rule-based mapping applied on top of TextBlob's built-in sentiment scores — it's a beginner-friendly approach, not a deep learning model.
- Works best on English text with clear emotional tone; sarcasm and mixed emotions may not be detected accurately.

---

## 👩‍💻 Author

Mahi — Hex Softwares Internship (Python Programming)