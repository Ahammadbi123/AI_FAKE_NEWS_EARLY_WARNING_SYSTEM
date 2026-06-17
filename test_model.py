import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

samples = [
    "Aliens attacked Delhi yesterday",
    "Secret miracle medicine discovered",
    "Government launched new education policy",
    "India won cricket match"
]

for text in samples:
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    print(text)
    print("Prediction =", pred)
    print("-" * 30)