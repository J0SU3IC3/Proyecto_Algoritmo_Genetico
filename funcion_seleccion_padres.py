from Funcion_Aptitud import aptfcn
import random
from Funcion_generadora_poblacion import vector_per

def parent_slec(vector_fam):
    fitnes_pob=0
    # TOTAL FITNES
    for i in range(len(vector_fam)):
        indiv = vector_fam[i]
        fitnes_pob += aptfcn(indiv)
    # Pronabilidad de seleccion
    prob_prev=0
    prob_acum=[]
    for i in range(0,len(vector_fam)):
        prob_prev += (aptfcn(vector_fam[i]))/fitnes_pob
        prob_acum.append(prob_prev)
    padres = []
    while len(padres)<(len(vector_fam)):
        dado=random.random()
        for i in range(len(prob_acum)):
            if (i+1)< len(prob_acum):
                prev=prob_acum[i]
                pos=prob_acum[i+1]
                if dado<prev:
                    padres.append(vector_fam[i])
                if len(padres) >= len(vector_fam):
                    break
                if (prev < dado) and (dado < pos):
                    padres.append(vector_fam[i+1])
                if len(padres) >= len(vector_fam):
                    break
    padres_pareja=[]
    for i in range(1,int((len(vector_fam)+2)/2)):
        pareja = []
        a=padres[2*i-2]
        b=padres[2*i-1]
        pareja.append(a)
        pareja.append(b)
        padres_pareja.append(pareja)
    return padres, padres_pareja






