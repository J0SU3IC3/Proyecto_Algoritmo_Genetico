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

def selec_padres(poblacion):
    fit_pobla=[] # fitness de cada individuo
    pobla_padres=[]
    for i in range(len(poblacion)):
        fitness=aptfcn(poblacion[i])
        fit_pobla.append(fitness)
    max_fit=max(fit_pobla)
    Anorm=[]
    for i in range(len(fit_pobla)):
        anorm=fit_pobla[i]-max_fit
        Anorm.append(anorm)
    S_Anorm=sum(Anorm)
    if S_Anorm==0:
        valor_verdad = 0
        return valor_verdad
    else:
        pro_selec=[] # Probabilidad de ser selecionados
        pro_acumu=[] # Probabilidad acumulada
        for i in range(len(Anorm)):
            p_n=(Anorm[i])/S_Anorm # Probabilidad de ser seleccionado de cada individuo
            pro_selec.append(p_n)
            proacumu=sum(pro_selec)
            pro_acumu.append(proacumu)
        while len(pobla_padres)<int(len(poblacion)/2):
            par_padres=[]
            r_1=random.random()
            r_2=random.random()
            j_1=0
            j_2=0
            while pro_acumu[j_1]<r_1:
                j_1+=1
            while pro_acumu[j_2]<r_2:
                j_2+= 1
            papa_1=poblacion[j_1]
            papa_2=poblacion[j_2]
            par_padres.append(papa_1)
            par_padres.append(papa_2)
            pobla_padres.append(par_padres)
        return pobla_padres





