from Funcion_Aptitud import aptfcn

def reemplazo(gen_padres,desc):
    poblacion = []
    for i in range(len(gen_padres)):
        indiv = gen_padres[i]
        poblacion.append(indiv)
    for i in range(len(desc)):
        indiv = desc[i]
        poblacion.append(indiv)
    fitnes_pob = []
    for i in range(len(gen_padres)+len(desc)):
        fit_indiv = aptfcn(poblacion[i])
        fitnes_pob.append(fit_indiv)
    elit_pob = []
    while len(elit_pob)<len(gen_padres):
        orden = min(fitnes_pob)
        posi = fitnes_pob.index(orden)
        fitnes_pob.remove(orden)
        elit = poblacion.pop(posi)
        elit_pob.append(elit)

    return elit_pob


