from fastapi import FastAPI
from src.intent_model import IntentModel
from src.difficulty_model import DifficultyModel
from src.topic_model import TopicModel
from src.llm_refinement import LLMRefinement
from src.adaptive_engine import AdaptiveEngine

app = FastAPI()

intent_model = IntentModel()
difficulty_model = DifficultyModel()
topic_model = TopicModel()
llm_refiner = LLMRefinement()
adaptive_engine = AdaptiveEngine()

@app.post("/analyze")
def analyze(query: str):
    # ML prediction
    ml_intent = intent_model.predict(query)
    difficulty = difficulty_model.predict(query)
    topic = topic_model.predict(query)

    # LLM refinement
    final_intent = llm_refiner.refine_intent(query, ml_intent)

    return {
        "intent": final_intent,
        "topic": topic,
        "difficulty_level": difficulty
    }

@app.post("/recommend")
def recommend(profile: dict):
    return adaptive_engine.recommend(profile)


