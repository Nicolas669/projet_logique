import random
import time


def neg(l):
    return(l+2*(l%2)-1)

def gen_3sat(clauses,variables):
    litteraux=2*variables
    CL = []
    LC=[[]]*litteraux
    def unique(l,k):
        t = random.randint(1,k)
        while (t in l or neg(t) in l):
            t = random.randint(1,k)
        return t
    for i in range(clauses):
        x = unique([],litteraux)
        y = unique([x],litteraux)
        z = unique([x, y],litteraux)
        CL.append([x,y,z])

        LC[x-1]=LC[x-1]+[i+1]

        LC[y-1]=LC[y-1]+[i+1]

        LC[z-1]=LC[z-1]+[i+1]


    return (CL,LC)


# Debut du decompte du temps


def satisfiable(CL, LC, heur_mono, heur_pur, recherche):
    if heur_pur == 1 and recherche == 1:
        return "recherche de tous les modèles incompatible avec l'heuristique de littéraux purs"
    if CL == []:
        return "ensemble vide : valide"
    for elt in CL:
        if elt == []:
            return "insatisfiable"
    nc = len(CL)
    nl = len(LC)
    I = []
    mod = []
    etat = [0] * nc
    long = []
    for j in CL:
        long += [len(j)]
    noeuds=1
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
                return "pb"
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
                        print(noeuds)

                        return I + [l]
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
    print(noeuds)
    if mod == []:
        return "insatisfiable"
    else:
        return mod


(CL,LC)=gen_3sat(50,20)
start_time = time.time()
print(satisfiable(CL,LC,0,0,0))
print(satisfiable(CL,LC,0,1,0))

# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))