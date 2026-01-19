import json
import string
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as file:
    data = json.load(file)

X, y = [], []

def preprocess(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation))

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        X.append(preprocess(pattern))
        y.append(intent["tag"])

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained successfully")
