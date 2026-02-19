from src.adaptive_engine import AdaptiveEngine

def evaluate_policy():

    engine = AdaptiveEngine()

    test_profiles = [
        {"mastery": 0.2, "score": 30, "attempts": 3, "time_spent": 120, "current_topic": "Backpropagation"},
        {"mastery": 0.5, "score": 60, "attempts": 2, "time_spent": 90, "current_topic": "Gradient Descent"},
        {"mastery": 0.85, "score": 90, "attempts": 1, "time_spent": 60, "current_topic": "Optimization"}
    ]

    print("\n=== Q2 Adaptive Policy Evaluation ===\n")

    for profile in test_profiles:
        recommendation = engine.recommend(profile)

        print(f"Input Mastery: {profile['mastery']}")
        print(f"Recommended Action: {recommendation['action']}")
        print(f"Next Topic: {recommendation['next_topic']}")
        print(f"Difficulty Adjustment: {recommendation['difficulty_adjustment']}")
        print("-" * 40)


if __name__ == "__main__":
    evaluate_policy()
