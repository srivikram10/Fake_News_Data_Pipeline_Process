import pandas as pd
import os
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

file_path = os.path.join(
    project_root,
    "data",
    "processed",
    "clean_news.csv"
)

df = pd.read_csv(file_path)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)
report = classification_report(
    y_test,
    predictions
)

print(report)
print("Accuracy:", accuracy)

model_path = os.path.join(
    project_root,
    "models",
    "fake_news_model.pkl"
)
report_path = os.path.join(
    project_root,
    "reports",
    "model_report.txt"
)

with open(report_path, "w") as f:
    f.write(report)

joblib.dump(model, model_path)

print("Model Saved Successfully!")