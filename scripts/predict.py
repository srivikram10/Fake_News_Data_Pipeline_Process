import joblib
import os

# Project root
project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Load model
model = joblib.load(
    os.path.join(
        project_root,
        "models",
        "fake_news_model.pkl"
    )
)

# Load vectorizer
vectorizer = joblib.load(
    os.path.join(
        project_root,
        "models",
        "tfidf_vectorizer.pkl"
    )
)

while True:

    news = input("\nEnter News Text: ")

    if news.lower() == "exit":
        break

    transformed = vectorizer.transform([news])

    prediction = model.predict(transformed)

    if prediction[0] == 0:
        print("Prediction: FAKE NEWS")
    else:
        print("Prediction: REAL NEWS")