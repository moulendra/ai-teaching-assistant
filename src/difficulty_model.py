import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.embeddings import EmbeddingModel

class DifficultyModel:

    def __init__(self):
        self.embedder = EmbeddingModel()
        self.model = RandomForestClassifier()

    def train(self, data_path):
        df = pd.read_csv(data_path)

        X = self.embedder.encode(df["query"].tolist())
        y = df["difficulty"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        preds = self.model.predict(X_test)
        print("Difficulty Classification Report:")
        print(classification_report(y_test, preds))

        joblib.dump(self.model, "models/difficulty_classifier.pkl")

    def predict(self, query):
        model = joblib.load("models/difficulty_classifier.pkl")
        emb = self.embedder.encode([query])
        return model.predict(emb)[0]
