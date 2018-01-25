import numpy as np


def a2a():
    a2a = 1251/1734
    return a2a


def a2b():
    a2b = 350/1734
    return a2b

def a2c():
    a2c = 116/1734
    return a2c

def a2d():
    a2d = 17/1734
    return a2d
def a0():
    a = [a2b(), a2c(), a2d()] # Transition probabilities away from a
    b = 1 - sum(a) # Probability of staying in a
    c = [b, a[0], a[1], a[2]]
    a0 = np.random.multinomial(1, pvals = c)
    return a0

def b2b():
    b2b = 731/1258
    return b2b

def b2c():
    b2c = 512/1258
    return b2c

def b2d():
    b2d = 15/1258
    return b2d

def b0():
    a = [b2c(), b2d()]
    b = 1 - sum(a)
    c = [b, a[0], a[1]]
    b0 = np.random.multinomial(1, pvals = c)
    return b0

def c2c():
    c2c = 1312/1749
    return c2c

def c2d():
    c2d = 437/1749
    return c2d

def c0():
    a = c2d()
    b = 1 - c2d()
    c = [b, a]
    c0 = np.random.multinomial(1, pvals = c)
    return c0
     

def d2d():
    d2d = 1
    return d2d