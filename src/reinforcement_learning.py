import numpy as np

class QLearning:

    def __init__(self):
        # states: low, medium, high mastery
        self.q_table = np.zeros((3, 3))
        self.alpha = 0.1
        self.gamma = 0.9

    def get_state(self, mastery):
        if mastery < 0.4:
            return 0
        elif mastery < 0.7:
            return 1
        else:
            return 2

    def choose_action(self, state):
        return np.argmax(self.q_table[state])
