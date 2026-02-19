from src.intent_model import IntentModel
from src.difficulty_model import DifficultyModel

print("Training Intent Model...")
intent = IntentModel()
intent.train("data/synthetic_queries.csv")

print("\nTraining Difficulty Model...")
difficulty = DifficultyModel()
difficulty.train("data/synthetic_queries.csv")

print("\nModels trained and saved successfully!")
