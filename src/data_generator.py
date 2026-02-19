import pandas as pd
import random

intents = ["Explanation", "Example", "Doubt clarification", "Revision"]
topics = ["Backpropagation", "Gradient Descent", "Neural Networks", "Optimization"]
difficulties = ["Beginner", "Intermediate", "Advanced"]

templates = {
    "Explanation": [
        "Explain {} in detail",
        "Can you explain {}?",
        "I don't understand {}"
    ],
    "Example": [
        "Give example of {}",
        "Show example for {}"
    ],
    "Doubt clarification": [
        "Why does {} work this way?",
        "I am confused about {}"
    ],
    "Revision": [
        "Revise {}",
        "Quick revision of {}"
    ]
}

def generate_queries(n=500):
    rows = []

    for _ in range(n):
        intent = random.choice(intents)
        topic = random.choice(topics)
        difficulty = random.choice(difficulties)
        query = random.choice(templates[intent]).format(topic)

        rows.append({
            "query": query,
            "intent": intent,
            "topic": topic,
            "difficulty": difficulty
        })

    df = pd.DataFrame(rows)
    df.to_csv("data/synthetic_queries.csv", index=False)
    print("Synthetic dataset generated successfully!")

if __name__ == "__main__":
    generate_queries()
