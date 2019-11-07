import time



def satisfiable(CL, LC, heur_mono, heur_pur, recherche):
    noeuds = 0
    if heur_pur == 1 and recherche == 1:
        return (noeuds,"recherche de tous les modèles incompatible avec l'heuristique de littéraux purs")
    if CL == []:
        return (noeuds,"ensemble vide : valide")
    for elt in CL:
        if elt == []:
            return (noeuds,"insatisfiable")
    noeuds=1
    nc = len(CL)
    nl = len(LC)
    I = []
    mod = []
    etat = [0] * nc
    long = []
    for j in CL:
        long += [len(j)]

    l = 0
    b = 0
    back = False
    fin = False
    while not fin:
        if b != 0:
            parite = b % 2
            if I == [] and parite == 0:
                fin = True
            if parite == 1:
                l = b + 1
            elif not fin:
                back = True
                b = I[-1]
                del I[-1]
                for i in etat:
                    if i == b:
                        i = 0
                for j in LC[neg(b) - 1]:
                    long[j - 1] += 1
        if not back and not fin:
            if l == 0:
                if heur_mono == 1:
                    for i in range(nc):
                        if etat[i] == 0 and long[i] == 1:
                            for k in CL[i]:
                                if k not in I and neg(k) not in I:
                                    l = k
                                    break
                if l == 0 and heur_pur == 1:
                    for j in range(1, nl, 2):
                        if j not in I and j + 1 not in I:
                            occu1 = 0
                            occu2 = 0
                            for c in LC[j - 1]:
                                if etat[c - 1] == 0:
                                    occu1 = 1
                                    break
                            for d in LC[j - 1]:
                                if etat[d - 1] == 0:
                                    occu2 = 1
                                    break
                            if (occu1 == 0 and occu2 != 0):
                                l = j + 1
                                break
                            elif (occu1 != 0 and occu2 == 0):
                                l = j
                                break
                if l == 0:
                    for j in range(1, nl, 2):
                        if j not in I and j + 1 not in I:
                            l = j
                            break

            if l == 0:
                return (noeuds,"pb")
            noeuds+=1
            n_l = neg(l)
            viol = False
            for k in (LC[n_l - 1]):
                if long[k - 1] == 1:
                    viol = True
            if not viol:
                if len(I) == nl / 2 - 1:
                    if recherche == 1:
                        J = I + [l]
                        mod += [J]
                        b = l
                    else:

                        return (noeuds,I + [l])
                else:
                    I += [l]
                    for k in (LC[n_l - 1]):
                        long[k - 1] -= 1
                    for j in (LC[l - 1]):
                        etat[j - 1] = l
                    b = 0
            else:
                b = l
        l = 0
        back = False

    if mod == []:
        return (noeuds,"insatisfiable")
    else:
        return (noeuds,mod)


def neg(l):
    return (l + 2 * (l % 2) - 1)


# pigeon 2
CL = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 11], [10, 12], [2, 6], [2, 10], [6, 10], [4, 8], [4, 12], [8, 12]]
LC = [[1], [2, 7, 8], [1], [2, 10, 11], [3], [4, 7, 9], [3], [4, 10, 12], [5], [6, 8, 9], [5], [6, 11, 12]]

cl = [[1, 3], [2], [4, 5]]
lc = [[1], [2], [1], [3], [3], []]

cl2 = [[1, 4], [2, 3, 7], [6, 4, 7], [2, 8, 5]]
lc2 = [[1], [2, 4], [2], [1, 3], [4], [3], [2, 3], [4]]

cl3 = [[1, 3, 6], [4, 1], [4, 5]]
lc3 = [[1, 2], [], [1], [2, 3], [3], [1]]


# Debut du decompte du temps
start_time = time.time()
(n,m)=satisfiable(cl, lc, 0, 0, 0)
# Affichage du temps d execution
t= (time.time() - start_time)
print(n,m,t)


