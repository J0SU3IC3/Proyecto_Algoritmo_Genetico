def aptitudfcn_1(matriz):
    cont=0
    #Esta parte concierne a las diagonales del tipo \
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            pos_in = matriz[i][(len(matriz) - 2) - j]
            memoria = (len(matriz) - 2) - j
            for m in range(1, len(matriz) ):
                if (i+m) < len(matriz) and (memoria+m) < len(matriz):
                    elem_diag = matriz[i+m][memoria + m]
                    if (pos_in == 1) and (pos_in == elem_diag):
                        cont += 1
    #Esta parte es para las diagonales del tipo /
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            pos_in = matriz[len(matriz)-1-j][len(matriz)-1-i]
            memoria_1=len(matriz)-1-j
            memoria_2=len(matriz) - 1 - i
            for m in range(1,len(matriz)):
                if (memoria_1 + m)<len(matriz) and (memoria_2-m)>= 0:
                    elem_diag=matriz[memoria_1 + m][memoria_2-m]
                    if (pos_in == 1) and (elem_diag == pos_in):
                        cont += 1
    #columnas
    for i in range(0, len(matriz)):
        for j in range (0, len(matriz)):
            pos_in=matriz[i][j]
            for m in range(1, len(matriz)):
                if ((i+m)<len(matriz)):
                    elem_col =matriz[i+m][j]
                    if (pos_in == 1) and pos_in==elem_col:
                        cont += 1
#filas
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz)):
            pos_in=matriz[j][i]
            for m in range(1,len(matriz)):
                if (i+m)<len(matriz):
                    elem_fil=matriz[j][i+m]
                    if (pos_in ==1) and pos_in == elem_fil :
                        cont+=1
    numero_atk=cont

    return numero_atk

def aptfcn(vector):
    cont=0
    dim=len(vector)
    for i in range(dim):
        entr=vector[i]
        for j in range(i+1,dim):
            entr_2=vector[j]
            pen=(entr_2-entr)/(j-i)
            if pen==1 or pen==(-1):
                cont+=1
    return(cont)

