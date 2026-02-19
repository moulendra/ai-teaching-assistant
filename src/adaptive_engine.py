from src.knowledge_tracing import KnowledgeTracing
from src.reinforcement_learning import QLearning

class AdaptiveEngine:

    def __init__(self):
        self.kt = KnowledgeTracing()
        self.rl = QLearning()

        self.topic_flow = {
            "Backpropagation": "Gradient Descent",
            "Gradient Descent": "Optimization",
            "Optimization": "Neural Networks",
            "Neural Networks": "Advanced Neural Networks"
        }

    def recommend(self, profile):
        mastery = profile["mastery"]
        score = profile["score"]
        attempts = profile["attempts"]
        time_spent = profile["time_spent"]
        current_topic = profile["current_topic"]

        state = self.rl.get_state(mastery)
        action_index = self.rl.choose_action(state)

        actions = ["Revision", "Practice", "Advance"]
        action = actions[action_index]

        if action == "Revision":
            difficulty = "Decrease"
            next_topic = current_topic
        elif action == "Advance":
            difficulty = "Increase"
            next_topic = self.topic_flow.get(current_topic, current_topic)
        else:
            difficulty = "Same"
            next_topic = current_topic

        return {
            "next_topic": next_topic,
            "action": action,
            "difficulty_adjustment": difficulty
        }
