from Funcion_generadora_poblacion import vector_per
from Funcion_Aptitud import aptfcn
from funcion_seleccion_padres import parent_slec
from funcion_cruza import cruza
from funcion_mutacion import mutacion
from funcion_reemplazo import reemplazo
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

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

pob_ori_mem = vector_per(8, cantidad)
pob_ori = pob_ori_mem


gnss=int(input('¿Cuantas generaciones quieres observar?'))


mejor_ind_gen = []
mejores_fitnes_gen=[]
peor_ind_gen = []
peores_fitness_gen = []
ind_prom_gen = []
fitnes_prom_gen=[]
desv_est = []
generaciones = []

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
    generaciones.append(pob_ori)

    #individuos con mejor fitnes por generacion
    fitness_pob=[]

    for i in range(len(pob_ori)):
        indiv = pob_ori[i]
        fitness_pob.append(aptfcn(indiv))
    minfit = min(fitness_pob)
    mejores_fitnes_gen.append(minfit)
    fittest_ind = []
    for j in range(len(pob_ori)):
        if minfit == fitness_pob[j]:
            fittest_ind.append(pob_ori[j])
    mejor_ind_gen.append(fittest_ind)

    #individuos con peor fitnes por geeneracion
    maxfit = max(fitness_pob)
    peores_fitness_gen.append(maxfit)

    men_fittest_ind = []
    for j in range(len(pob_ori)):
        if maxfit == fitness_pob[j]:
            men_fittest_ind.append(pob_ori[j])
    peor_ind_gen.append(men_fittest_ind)
    #individuos promedio
    promedio = int(sum(fitness_pob)/len(fitness_pob))
    fitnes_prom_gen.append(sum(fitness_pob)/len(fitness_pob))
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
tab1 = pd.DataFrame({'Mejor Fitnes': mejores_fitnes_gen, 'Peor fitnes': peores_fitness_gen, 'Fitnes promedio': fitnes_prom_gen, 'Desv. Estandar':desv_est},
                    columns=['Mejor Fitnes', 'Peor fitnes', 'Fitnes promedio', 'Desv. Estandar'])

print('La siguiente tabla te muestra como se han desarrollado las poblaciones bajo los parametros que otorgaste')
print(tab1)
time.sleep(4)
input('Presiona Enter para continuar')

Resp=input('¿Te gustaria observar alguna generacion? \n [S/N]' )

while Resp=='S':
    original = input('¿Quieres ver la poblacion original?[S/N]')
    if original == 'S':
        for i in range(len(pob_ori_mem)):
            print(pob_ori_mem[i], '\n')
        fitnes_pob=[]
        for i in range(len(pob_ori_mem)):
            fitnes_pob.append(aptfcn(pob_ori_mem[i]))
        minval=min(fitnes_pob)
        min_fit=[]
        for i in range(len(pob_ori_mem)):
            if minval == fitnes_pob[i]:
                min_fit.append(pob_ori_mem[i])
        maxval=max(fitnes_pob)
        max_fit = []
        for i in range(len(pob_ori_mem)):
            if maxval == fitnes_pob[i]:
                max_fit.append(pob_ori_mem[i])
        promen=sum(fitnes_pob)/len(pob_ori_mem)

        print('Esta generacion tiene a los elementos')
        for j in range(len(pob_ori_mem)):
            print(pob_ori_mem[j], '\n')
        print('Sus mejores individuos tienen un fitness de', minval, 'y estos son')
        for j in range(len(min_fit)):
            print(min_fit[j])
        print('Sus peores individuos tienen un fitness de', maxval, 'y estos son')
        for j in range(len(max_fit)):
            print(max_fit[j])
        print('En promedio la poblacion original tiene un fitnes de', promen)

    obs_gen= input('¿Quieres ver alguna otra generacion?[S/N]')
    if obs_gen == 'S':
        pos=int(input('¿Que generacion quieres observar? Las generaciones estan enumeradas de 0 en adelante'))

        observable=generaciones[pos]
        print('Esta generacion tiene a los elementos')
        for j in range(len(observable)):
            print(observable[j], '\n')
        print('Sus mejores individuos tienen un fitness de', mejores_fitnes_gen[pos], 'y estos son')
        best=mejor_ind_gen[pos]
        for j in range(len(best)):
            print(best[j])
        print('Sus peores individuos tienen un fitness de', peores_fitness_gen[pos], 'y estos son')
        worst = mejor_ind_gen[pos]
        for j in range(len(worst)):
            print(worst[j])
        print('En promedio esta generacion tiene un fitnes de', fitnes_prom_gen[pos])
    Resp = input('¿Quieres ver alguna otra generacion?[S/N]')

fitnes_pob=[]
for i in range(len(pob_ori_mem)):
    fitnes_pob.append(aptfcn(pob_ori_mem[i]))
minval=min(fitnes_pob)
min_fit=[]

for i in range(len(pob_ori_mem)):
    if minval == fitnes_pob[i]:
        min_fit.append(pob_ori_mem[i])

longitudes = []
longitudes.append(len(min_fit))
for i in range(len(mejor_ind_gen)):
    longitudes.append(len(mejor_ind_gen[i]))

print('la siguiente grafica muestra como se comportan las poblaciones a medida que pasa el tiempo \n'
      'es decir, muestra cuantos individuos tienen un buen fitness mientras mas pasa el tiempo ')
ejex = []
for i in range(len(mejor_ind_gen)+1):
    ejex.append(i)

plt.plot(ejex,longitudes)
plt.ylabel('Individuos mas aptos por generacion')
plt.xlabel('Generacion (tiempo)')
plt.show()


promedios_n = []
promedios_n.append(sum(fitnes_pob)/len(fitnes_pob))
for i in range(len(fitnes_prom_gen)):
    promedios_n.append(fitnes_prom_gen[i])
print('tambien se puede notar que a medida que pase el tiempo el promedio de fitnes en la poblacion va descendiendo \n'
      'esto quiere decir que mientras mas pase el tiempo futuras generaciones seran cada vez mas aptas dados \n'
      'los parametros establecidos')
plt.plot(ejex,promedios_n)
plt.ylabel('Promedio por generacion')
plt.xlabel('Generacion (tiempo)')
plt.show()


