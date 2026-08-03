"""
Task 2: Emotion from Text Detector
Hex Softwares Internship

What it does:
- Takes user text input (or reads from a .txt file)
- Uses TextBlob to calculate polarity (positive/negative) and subjectivity
- Maps the polarity score to a human-readable emotion label

Requirements:
    pip install textblob
    python -m textblob.download_corpora
"""

from textblob import TextBlob


def get_emotion(polarity, subjectivity):
    """
    Map polarity (-1 to 1) and subjectivity (0 to 1) to an emotion label.
    This is a simple rule-based mapping on top of TextBlob's sentiment score.
    """
    if polarity > 0.5:
        emotion = "Very Happy 😄"
    elif polarity > 0.1:
        emotion = "Happy 🙂"
    elif polarity < -0.5:
        emotion = "Very Sad / Angry 😠"
    elif polarity < -0.1:
        emotion = "Sad 🙁"
    else:
        emotion = "Neutral 😐"

    tone = "Opinion-based" if subjectivity > 0.5 else "Fact-based"
    return emotion, tone


def analyze_text(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    emotion, tone = get_emotion(polarity, subjectivity)

    print("\n--- Analysis Result ---")
    print(f"Text        : {text}")
    print(f"Polarity    : {polarity:.2f}  (-1 = very negative, +1 = very positive)")
    print(f"Subjectivity: {subjectivity:.2f}  (0 = factual, 1 = opinion)")
    print(f"Emotion     : {emotion}")
    print(f"Tone        : {tone}")
    print("------------------------\n")

    return {
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "emotion": emotion,
        "tone": tone
    }


def analyze_file(file_path):
    """Analyze each line of a text file separately."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    results = [analyze_text(line) for line in lines]
    return results


if __name__ == "__main__":
    print("Emotion from Text Detector")
    print("1. Analyze typed text")
    print("2. Analyze a .txt file (line by line)")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        while True:
            user_text = input("\nEnter text (or 'exit' to quit): ").strip()
            if user_text.lower() == "exit":
                break
            if user_text:
                analyze_text(user_text)
    elif choice == "2":
        path = input("Enter file path: ").strip()
        try:
            analyze_file(path)
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Invalid choice.")