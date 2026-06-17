import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load Dataset
df = pd.read_csv(
    "data/news_dataset.csv",
    encoding="utf-8"
)

# Remove empty rows
df = df.dropna(subset=["text", "label"])

# Check labels
print("\nOriginal Labels:")
print(df["label"].value_counts())

# Features
X = df["text"].astype(str)

# Labels
y = df["label"].astype(str).str.upper()

# Convert Labels
y = y.map({
    "FAKE": 1,
    "REAL": 0
})

# Remove invalid labels
mask = y.notna()
X = X[mask]
y = y[mask]

print("\nMapped Labels:")
print(y.value_counts())

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=30000,
    ngram_range=(1, 2),
    stop_words="english"
)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Balanced Model
model = LogisticRegression(
    max_iter=3000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print(f"\nAccuracy = {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, pred))

# Save Model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel Saved Successfully")

