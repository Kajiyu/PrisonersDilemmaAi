#coding: utf-8
MAXLEARNNUM = 100000
ALPHA = 0.1
GAMMA = 0.99
EPS = 0.1

def recogState(mya, youra):
    if (mya == 1) and (youra == 1):
        return "cc"
    elif (mya == 1) and (youra == 0):
        return "cd"
    elif (mya == 0) and (youra == 1):
        return "dc"
    else:
        return "dd"

def evaluate(value1, value2):
    if (value1 == 1) and (value2 == 1):
        return 3
    elif (value1 == 1) and (value2 == 0):
        return 5
    elif (value1 == 0) and (value2 == 1):
        return 0
    else:
        return 1
