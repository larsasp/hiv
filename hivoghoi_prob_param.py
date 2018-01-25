import numpy as np
R = np.random.RandomState(1234)


# Må ha "trekkningen som funksjon" (Som i hboc modell: må finne ut om man kan indexe en DF og benytte lagrede verdier!)
pa = np.genfromtxt('a.csv')
pb = np.genfromtxt('b.csv')
pc = np.genfromtxt('c.csv')



def p_a2a(s): 
    return pa[s, 0]

def p_a2b(s):
    return pa[s, 1]

def p_a2c(s):
    return pa[s, 2]

def p_a2d(s):
    return pa[s, 3]

def a0(s):
    a = [p_a2b(s), p_a2c(s), p_a2d(s)] # Transition probabilities away from a
    b = 1 - sum(a) # Probability of staying in a
    c = [b, a[0], a[1], a[2]]
    a0 = R.multinomial(1, pvals = c)
    return a0

def p_b2b(s):
    return pb[s, 0]

def p_b2c(s):
    return pb[s, 1]

def p_b2d(s):
    return pb[s, 2]

def b0(s):
    a = [p_b2c(s), p_b2d(s)]
    b = 1 - sum(a)
    c = [b, a[0], a[1]]
    b0 = R.multinomial(1, pvals = c)
    return b0

def p_c2c(s):
    return pc[s, 0]

def p_c2d(s):
    return pc[s, 1]

def c0(s):
    a = p_c2d(s)
    b = 1 - a
    c = [b, a]
    c0 = R.multinomial(1, pvals = c)
    return c0
     

def d2d():
    d2d = 1
    return d2d