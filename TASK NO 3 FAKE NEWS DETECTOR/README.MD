# AI Fake News Detection System

**Hex Softwares Internship — Task 03 (Artificial Intelligence)**

An AI model that classifies news articles as **REAL** or **FAKE** using
NLP text preprocessing, TF-IDF feature extraction, and a machine
learning classifier (Logistic Regression).

## How it works
1. Loads the Kaggle "Fake and Real News Dataset" (`Fake.csv` + `True.csv`)
2. Cleans text (lowercasing, removing URLs, punctuation, numbers, HTML)
3. Converts text into TF-IDF vectors
4. Trains a Logistic Regression classifier
5. Evaluates with accuracy, confusion matrix, and classification report
6. Saves the trained model for reuse and predicts on new headlines

## Setup
```bash
pip install pandas scikit-learn joblib
```

Download the dataset from Kaggle and place `Fake.csv` and `True.csv`
in this folder:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Run
```bash
python fake_news_detector.py
```

This trains the model, prints accuracy/metrics, saves
`fake_news_model.pkl` + `tfidf_vectorizer.pkl`, and runs one sample
prediction.

## Predict on your own text
```python
import joblib
from fake_news_detector import predict_news

model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

print(predict_news("Your headline or article text here", model, vectorizer))
```

## Submission checklist (per Hex Softwares instructions)
- [ ] Push this whole project to a new GitHub repo named
      `HexSoftwares_FakeNewsDetection`
- [ ] Post your intern status update on LinkedIn, tagging Hex Softwares
- [ ] After finishing, post a completion update on LinkedIn with a short
      video explanation + the GitHub repo link
- [ ] Submit via the official Hex Softwares submission form

---
*Code today, conquer tomorrow with Hex Softwares Pvt. Ltd*