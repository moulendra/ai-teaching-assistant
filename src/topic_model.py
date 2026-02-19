import numpy as np
from src.embeddings import EmbeddingModel

class TopicModel:

    def __init__(self):
        self.embedder = EmbeddingModel()

        self.topics = [
            "Backpropagation",
            "Gradient Descent",
            "Optimization",
            "Neural Networks"
        ]

        self.topic_embeddings = self.embedder.encode(self.topics)

    def predict(self, query):
        query_embedding = self.embedder.encode([query])[0]

        similarities = np.dot(self.topic_embeddings, query_embedding) / (
            np.linalg.norm(self.topic_embeddings, axis=1) *
            np.linalg.norm(query_embedding)
        )

        return self.topics[np.argmax(similarities)]
