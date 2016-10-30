#coding: utf-8
import numpy as np
from config import *

class Agent:
    def __init__(self):
        self.pos = np.array([0.25, 0.25])
        self.current_score = 2
        self.currentState = "dd"
        self.Q = {}
        self.A = (0, 1)
        self.Q["cc"] = np.random.rand(2) * 5
        self.Q["cd"] = np.random.rand(2) * 5
        self.Q["dc"] = np.random.rand(2) * 5
        self.Q["dd"] = np.random.rand(2) * 5
        self.score_history = []

    def decide_action(self):
        if np.random.random() < EPS:
            return self.Q[self.currentState].argmax()
        else:
            return np.random.choice(self.A)

    def do_action(self, mya, youra):
        next_s = recogState(mya, youra)
        reward = evaluate(mya, youra) - self.current_score
        return next_s, reward
