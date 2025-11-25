import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

data = {
    "review": [
        "Excellent product, highly recommended!",
        "Worst item ever, waste of money",
        "Seller gave me refund instantly, nice!",
        "I love it so much!",
        "This is fake, don’t buy",
        "Very bad quality, completely fraud",
    ],
    "label": [0, 1, 0, 0, 1, 1]   # 1 = fake, 0 = genuine
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["label"], test_size=0.2, random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")
