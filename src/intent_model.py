import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.embeddings import EmbeddingModel

class IntentModel:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.model = LogisticRegression(max_iter=1000)

    def train(self, data_path):
        df = pd.read_csv(data_path)

        X = self.embedder.encode(df["query"].tolist())
        y = df["intent"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        preds = self.model.predict(X_test)
        print("Intent Classification Report:")
        print(classification_report(y_test, preds))

        joblib.dump(self.model, "models/intent_classifier.pkl")

    def predict(self, query):
        model = joblib.load("models/intent_classifier.pkl")
        emb = self.embedder.encode([query])
        return model.predict(emb)[0]
