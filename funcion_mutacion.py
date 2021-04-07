import random

def mutacion(indiv):
    alea_1=random.randint(0,len(indiv)-1)
    alea_2 = random.randint(0, len(indiv)-1)
    interc_1=indiv[alea_1]
    interc_2=indiv[alea_2]
    indiv[alea_1] = interc_2
    indiv[alea_2] = interc_1

    return indiv

