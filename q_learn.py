#coding: utf-8
import numpy as np
from config import *
from agent import Agent


class Q_Learn:
    def __init__(self):
        self.agent1 = Agent()
        self.agent2 = Agent()

    def learn(self, n_rounds, t_max):
        for i in range(n_rounds):
            s = "dd"
            self.agent1.currentState = s
            self.agent2.currentState = s
            for t in range(t_max):
                a1 = self.agent1.decide_action()
                a2 = self.agent2.decide_action()
                next_s1, reward1 = self.agent1.do_action(a1, a2)
                next_s2, reward2 = self.agent2.do_action(a2, a1)
                self.agent1.Q[self.agent1.currentState][a1] += ALPHA * (reward1 + GAMMA*self.agent1.Q[next_s1].max() - self.agent1.Q[self.agent1.currentState][a1])
                self.agent2.Q[self.agent2.currentState][a2] += ALPHA * (reward2 + GAMMA*self.agent1.Q[next_s2].max() - self.agent2.Q[self.agent2.currentState][a2])
                self.agent1.currentState = next_s1
                self.agent2.currentState = next_s2

            # test
            s = "cc"
            self.agent1.currentState = s
            self.agent2.currentState = s
            for t in range(t_max):
                a1 = self.agent1.Q[s].argmax()
                a2 = self.agent2.Q[s].argmax()
                self.agent1.currentState = recogState(a1, a2)
                self.agent2.currentState = recogState(a2, a1)
            self.agent1.score_history.append(evaluate(a1, a2))
            self.agent2.score_history.append(evaluate(a2, a1))
            print ("agent1:: test result: {0} = {1}".format(self.agent1.currentState, self.agent1.score_history[i]))
            print ("agent2:: test result: {0} = {1}".format(self.agent2.currentState, self.agent2.score_history[i]))
