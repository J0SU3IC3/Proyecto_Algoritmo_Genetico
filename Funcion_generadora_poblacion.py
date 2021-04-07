import random
import numpy as np

def matrices50(num_mat, fil, col):
    pob = np.zeros([num_mat, fil, col])
    for n in range(0, num_mat):
        for i in range(0, col):
            p = random.randrange(0, col)
            pob[n, i, p] = 1
    return pob

def vector_per(dim , cant):
    pob = []
    pos = []
    for i in range(0,dim):
        pos.append(i)
    while len(pob)!=cant:
        indiv=[]
        for j in range(0, dim):
            valor=random.choice(pos)
            pos.remove(valor)
            indiv.append(valor)
        for i in range(0, dim):
            pos.append(i)
        pob.append(indiv)
    return pob