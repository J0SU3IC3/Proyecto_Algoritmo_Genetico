def cruza(pareja):
    papa_1 = pareja[0]
    papa_2 = pareja[1]
    tocsp_1=[]
    tocsp_2=[]
    cont=0
    used_pos=[]
    for i in range(len(papa_1)):
        llave = 0
        if len(used_pos)>0:
            for j in used_pos:
                if i==j:
                    llave=1
            if llave==0:
                alelo_1 = papa_1[i]
                alelo_2 = papa_2[i]
                tocp1 = []
                tocp2 = []
                tocp1.append(alelo_1)
                tocp2.append(alelo_2)
                used_pos.append((i))
                cont += 1
                while alelo_2 != alelo_1:
                    for j in range(len(papa_1)):
                        aleloar = papa_1[j]
                        if alelo_2 == aleloar:
                            tocp1.append(aleloar)
                            alelo_2 = papa_2[j]
                            tocp2.append(alelo_2)
                            used_pos.append(j)
                            cont += 1
                    if cont > len(papa_1):
                        break
                tocsp_1.append(tocp1)
                tocsp_2.append(tocp2)
            if cont == len(papa_1):
                break
        else:
            alelo_1 = papa_1[i]
            alelo_2 = papa_2[i]
            tocp1 = []
            tocp2 = []
            tocp1.append(alelo_1)
            tocp2.append(alelo_2)
            used_pos.append((i))
            cont+=1
            while alelo_2 != alelo_1:
                for j in range(len(papa_1)):
                    aleloar = papa_1[j]
                    if alelo_2 == aleloar:
                        tocp1.append(aleloar)
                        alelo_2 = papa_2[j]
                        tocp2.append(alelo_2)
                        used_pos.append(j)
                        cont+=1
                if cont>len(papa_1):
                    break
            tocsp_1.append(tocp1)
            tocsp_2.append(tocp2)
            if cont==len(papa_1):
                break
    hijo_1 = []
    hijo_2 = []
    for i in range(len(papa_1)):
        hijo_1.append(0)
        hijo_2.append(0)

    # creacion hijo1
    genes = []
    for i in range(len(tocsp_1)):
        if 2*i < len(tocsp_1):
            gen_1 = tocsp_1[2*i]
            genes.append(gen_1)
        if (2*i+1) < len(tocsp_1):
            gen_2 = tocsp_2[2*i+1]
            genes.append(gen_2)
    gestacion = []
    for i in range(len(genes)):
        gen_pos = genes[i]
        for j in range(len(gen_pos)):
            gestacion.append(gen_pos[j])
    for i,j in zip(used_pos, gestacion):
        hijo_1[i] = (j)
    #creacion hijo2
    genes = []
    for i in range(len(tocsp_1)):
        if 2 * i < len(tocsp_1):
            gen_1 = tocsp_2[2 * i]
            genes.append(gen_1)
        if (2 * i + 1) < len(tocsp_1):
            gen_2 = tocsp_1[2 * i + 1]
            genes.append(gen_2)
    gestacion = []
    for i in range(len(genes)):
        gen_pos = genes[i]
        for j in range(len(gen_pos)):
            gestacion.append(gen_pos[j])
    for i, j in zip(used_pos, gestacion):
        hijo_2[i] = (j)

    return hijo_1, hijo_2