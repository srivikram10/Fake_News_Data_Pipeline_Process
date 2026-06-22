import pandas as pd
import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Project root
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Read cleaned data
file_path = os.path.join(
    project_root,
    "data",
    "processed",
    "clean_news.csv"
)

df = pd.read_csv(file_path)

# Features and target
X = df["text"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X = vectorizer.fit_transform(X)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,
    test_size=0.2,
    random_state=42
)

# Save vectorizer
vectorizer_path = os.path.join(
    project_root,
    "models",
    "tfidf_vectorizer.pkl"
)

joblib.dump(vectorizer, vectorizer_path)

print("Feature Engineering Completed!")
print("Training Records:", X_train.shape[0])
print("Testing Records:", X_test.shape[0])