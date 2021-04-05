from Funcion_Aptitud import aptfcn
from funcion_cruza import cruza
def reemplazo(gen_padres,desc):
    poblacion = []
    for i in range(len(gen_padres)):
        indiv = gen_padres[i]
        poblacion.append(indiv)
    print(poblacion)
    for i in range(len(desc)):
        indiv = desc[i]
        poblacion.append(indiv)
    print(poblacion)
    fitnes_pob = []
    for i in range(len(gen_padres)+len(desc)):
        fit_indiv = aptfcn(poblacion[i])
        fitnes_pob.append(fit_indiv)
    print(fitnes_pob)
    elit_pob = []
    while len(elit_pob)<len(gen_padres):
        orden = min(fitnes_pob)
        elit = poblacion.pop(fitnes_pob.index(orden))
        elit_pob.append(elit)
    return elit_pob


