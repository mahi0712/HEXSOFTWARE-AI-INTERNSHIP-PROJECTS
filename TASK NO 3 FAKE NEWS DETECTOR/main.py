
import re
import string
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib


def clean_text(text: str) -> str:
    """Basic text cleaning: lowercase, remove punctuation/urls/numbers/extra spaces."""
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)          # remove URLs
    text = re.sub(r"\[.*?\]", "", text)                  # remove text in brackets
    text = re.sub(r"<.*?>+", "", text)                   # remove html tags
    text = re.sub(r"[%s]" % re.escape(string.punctuation), "", text)  # punctuation
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\w*\d\w*", "", text)                 # numbers
    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_data(fake_path="Fake.csv", true_path="True.csv") -> pd.DataFrame:
    fake_df = pd.read_csv(fake_path)
    true_df = pd.read_csv(true_path)

    fake_df["label"] = 0   # 0 = fake
    true_df["label"] = 1   # 1 = real

    df = pd.concat([fake_df, true_df], axis=0).reset_index(drop=True)

    # Kaggle dataset has 'title' and 'text' columns — combine them
    if "title" in df.columns and "text" in df.columns:
        df["content"] = df["title"].fillna("") + " " + df["text"].fillna("")
    else:
        df["content"] = df.iloc[:, 0].astype(str)

    df["content"] = df["content"].apply(clean_text)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # shuffle
    return df[["content", "label"]]


def train_model(df: pd.DataFrame, model_type="logistic"):
    X_train, X_test, y_train, y_test = train_test_split(
        df["content"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
    )

    vectorizer = TfidfVectorizer(max_df=0.7, stop_words="english", max_features=50000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    if model_type == "naive_bayes":
        model = MultinomialNB()
    else:
        model = LogisticRegression(max_iter=1000)

    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)
    acc = accuracy_score(y_test, y_pred)

    print(f"\nModel: {model_type}")
    print(f"Accuracy: {acc:.4f}\n")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Fake", "Real"]))

    return model, vectorizer


def predict_news(text: str, model, vectorizer) -> str:
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    return "REAL" if pred == 1 else "FAKE"


def save_model(model, vectorizer, model_path="fake_news_model.pkl", vec_path="tfidf_vectorizer.pkl"):
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vec_path)
    print(f"\nSaved model to {model_path} and vectorizer to {vec_path}")


if __name__ == "__main__":
    print("Loading and preprocessing data...")
    data = load_data("Fake.csv", "True.csv")

    print("Training model...")
    model, vectorizer = train_model(data, model_type="logistic")

    save_model(model, vectorizer)

    # quick manual test
    sample_headline = "Scientists confirm the moon is made of cheese, NASA reports"
    result = predict_news(sample_headline, model, vectorizer)
    print(f"\nSample prediction -> '{sample_headline}'\nPredicted: {result}")