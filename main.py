#coding: utf-8
from config import *
import numpy as np
import sys, time
from q_learn import Q_Learn

if __name__ == '__main__':
    np.random.seed(123)
    q_learn = Q_Learn()
    q_learn.learn(1000,20)
