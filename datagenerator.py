import numpy as np






a = [(1251/1734), (350/1734), (116/1734), (17/1734)]    
pa = np.random.RandomState().dirichlet(alpha = a, size = 1000)

b = [(731/1258), (512/1258), (15/1258)]
pb = np.random.RandomState().dirichlet(alpha = b, size = 1000)

c = [(1312/1749), (437/1749)]
pc = np.random.RandomState().dirichlet(alpha = c, size = 1000)


np.savetxt('a.csv', pa)
np.savetxt('b.csv', pb)
np.savetxt('c.csv', pc)

