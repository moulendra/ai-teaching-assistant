class KnowledgeTracing:

    def __init__(self, learning_rate=0.2, decay=0.1):
        self.learning_rate = learning_rate
        self.decay = decay

    def update_mastery(self, mastery, correct):
        if correct:
            mastery += self.learning_rate * (1 - mastery)
        else:
            mastery -= self.decay * mastery

        return max(0, min(1, mastery))
