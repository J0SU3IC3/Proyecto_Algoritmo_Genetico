from Funcion_generadora_poblacion import vector_per
from Funcion_Aptitud import aptfcn
from funcion_seleccion_padres import parent_slec
from funcion_cruza import cruza
from funcion_mutacion import mutacion
from funcion_reemplazo import reemplazo
import numpy as np
import pandas as pd

print('¡Hola!,se bienvenido a mi algoritmo genetico')

input("Pulsa enter para continuar...")

print('Primero generaremos una población aleatoria de individuos (generación) que representan tableros de ajedrez')
print('en los que se ha colocado una reina por fila, de modo que no se tengan 2 o mas reinas por columnas.')
print('Esto se logro representando a las posiciones como vectores de permutacion,')
print('luego, en base a una seleccion de padres por ruleta, una cruza ciclica, una mutacion por intercambio')
print('y  un reemplazo por elitismo, se obtendra una población nueva que sera la "descendia" de la poblacion orignal. ')
input()
print('\n')
print('Tú podras determinar cuantas veces o generaciones quieres que este proceso se repita')
print('\n')

cantidad=int(input('¿Cuantos individuos quieres que tenga tu poblacion original?'))

pob_ori = vector_per(8, cantidad)

gnss=int(input('¿Cuantas generaciones quieres observar?'))


mejor_ind_gen = []
peor_ind_gen = []
ind_prom_gen = []
desv_est = []
for i in range(gnss):
    #seleccion de padres
    cndts, cndts_par = parent_slec(pob_ori)
    #cruza
    descn = []
    for j in range(len(cndts_par)):
        padres = cndts_par[j]
        desc_1, desc_2 = cruza(padres)
        descn.append(desc_1)
        descn.append(desc_2)
    #mutacion
    for j in range(len(descn)):
        descn[j] = mutacion(descn[j])
    #reemplazo
    pob_fin = reemplazo(cndts, descn)
    pob_ori = pob_fin

    #individuos con mejor fitnes por generacion
    fitness_pob=[]

    for i in range(len(pob_ori)):
        indiv = pob_ori[i]
        fitness_pob.append(aptfcn(indiv))
    minfit = min(fitness_pob)

    fittest_ind = []
    for j in range(len(pob_ori)):
        if minfit == fitness_pob[j]:
            fittest_ind.append(pob_ori[j])
    mejor_ind_gen.append(fittest_ind)

    #individuos con peor fitnes por geeneracion
    maxfit = max(fitness_pob)

    men_fittest_ind = []
    for j in range(len(pob_ori)):
        if maxfit == fitness_pob[j]:
            men_fittest_ind.append(pob_ori[j])
    peor_ind_gen.append(men_fittest_ind)
    #individuos promedio
    promedio = int(sum(fitness_pob)/len(fitness_pob))

    ind_prom = []
    for i in range(len(fitness_pob)):
        if promedio == fitness_pob[i]:
            ind_prom.append(pob_ori[i])
    ind_prom_gen.append(ind_prom)
    #desviacion estandar
    suma = 0
    for i in range(len(fitness_pob)):
        desv = (fitness_pob[i]-promedio)**2
        suma += desv
    varianza = suma/(len(fitness_pob))
    desv_est.append(np.sqrt(varianza))

#tabla de algoritmo genetico
tab1 = pd.DataFrame({mejor_ind_gen, peor_ind_gen, ind_prom_gen, desv_est },
                    columns = ['Mejores individuos', 'Peores individuos', 'Individuos promedio','Desv. Est.' ])











