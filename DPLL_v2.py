
def satisfiable(CL,LC,heur_mono,heur_pur):
    if CL==[]:
        return "ensemble vide : valide"
    for elt in CL:
            if elt==[]:
                return "insatisfiable"
    nc=len(CL)
    nl=len(LC)
    I = []
    etat=[0]*nc
    long=[]
    for j in CL:
        long+=[len(j)]

    l=0
    b=0
    back=False
    while 0 in etat:
        print(I)
        print(etat)
        print(long)
        if b!=0:
            parite=b%2
            if I==[] and parite==0:
                return "insatisfiable"
            if parite==1:
                l=b+1
            else:
                back=True
                b=I[-1]
                del I[-1]
                for i in etat:
                    if i==b:
                        i=0
                for j in LC[neg(b)-1]:
                    long[j-1] += 1
        if not back:
            if l==0:
                if heur_mono==1:
                    for i in range(nc):
                        if etat[i] == 0 and long[i] == 1:
                            l=CL[i][0]
                if l==0 and heur_pur==1:
                    for j in range(1,nl,2):
                        occu1 = len(LC[j-1])
                        occu2 = len(LC[j])
                        if (occu1 == 0 and occu2 != 0 and j not in I and j+1 not in I):
                            l=j+1
                            break
                        elif (occu1 != 0 and occu2 == 0 and j not in I and j+1 not in I):
                            l=j
                            break
                if l==0:
                    for j in range(1,nl,2):
                        if j not in I and j+1 not in I:
                            l=j
                            break
            print(l)
            if l==0:
                return "pb"
            n_l=neg(l)
            viol=False
            for k in (LC[n_l - 1]):
                if long[k-1]==1:
                    viol=True
            if not viol:
                I += [l]
                for k in (LC[n_l - 1]):
                    long[k - 1] -= 1
                for j in (LC[l - 1]):
                    etat[j - 1] = l
                b=0
            else:
                b=l
        l=0
        back=False
    return (I)
#les heuristiques sont fausses
def neg(l):
    return(l+2*(l%2)-1)

CL=[[1,3],[2,4],[5,7],[6,8],[9,11],[10,12],[2,6],[2,10],[6,10],[4,8],[4,12],[8,12]]
LC=[[1],[2,7,8],[1],[2,10,11],[3],[4,7,9],[3],[4,10,12],[5],[6,8,9],[5],[6,11,12]]
print(satisfiable(CL,LC,0,0))