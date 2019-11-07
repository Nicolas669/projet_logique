

def satisfiable(CL,LC,var,tousmodele):
    if CL==[]:
        return "valide"
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
    Lvar=[i for i in range(1,var+1)]

    while len(I) != var:
        back=False
#check monolit
        for c in range(nc):
            if etat==0 and long[c]==1:
                l=CL[c-1][0]
                n_l = neg(l)
                for k in (LC[n_l - 1]):
                    if long[k - 1] == 0:
                        back=True
                        break
                if back:
                    m=I[-1]
                    del I[-1]
                    Lvar+=[m]
                    Lvar+=[neg(m)]
                    for i in LC[m]:
                        etat[i]=0
                    for j in LC[neg(m)]:
                        long[j]+=1
                    #on a remis a jour, qu'est ce qu on fait mtn ?
                else:
                    for k in (LC[n_l - 1]):
                        long[k - 1] -= 1
                    I += [l]
                    del Lvar[Lvar.index(l // 2)]
                    for j in (LC[l - 1]):
                        etat[j - 1] = l

#check lit purs
        if not tousmodele:
            for v in Lvar:
                i=2*v-1
                pair=len(LC[i-1])
                impair=len(LC[i])
                if (pair==0 and impair!=0) :
                    I+=[i]
                    for j in (LC[i - 1]):
                        etat[j-1] = i
                    del Lvar[Lvar.index(v)]

                elif(impair==0 and pair!=0):
                    I+=[i+1]
                    for j in (LC[i]):
                        etat[j-1] = i+1
                    del Lvar[Lvar.index(v)]

#execution
        if heur==:

        elif heur==:

        else:
            v=Lvar[0]
        l=v*2-1
        n_l = neg(l)
        #refaire toute cette partie c'est tout bzzzzzzzzzzzzzzzzzzzz
        litvrai=False
        for k in (LC[n_l - 1]):
            if long[k - 1] == 0:
                litvrai = True
                break
        if litvrai:
            for k in (LC[l - 1]):
                if long[k - 1] == 0:
                    back = True
                    break
            for k in (LC[n_l - 1]):
                long[k - 1] -= 1
            I += [l]
            del Lvar[Lvar.index(l // 2)]
            for j in (LC[l - 1]):
                etat[j - 1] = 1
        elif back:
            m = I[-1]
            del I[-1]
            Lvar += [m]
            Lvar += [neg(m)]
            for i in LC[m]:
                etat[i] = 0
            for j in LC[neg(m)]:
                long[j] += 1
            # on a remis a jour, qu'est ce qu on fait mtn ?
        else:
            for k in (LC[n_l - 1]):
                long[k - 1] -= 1
            I += [l]
            del Lvar[Lvar.index(l // 2)]
            for j in (LC[l - 1]):
                etat[j - 1] = 1




#evalue l a vrai et maj les donnees
def verif(CL,LC,var,etat,long,I,l,Lvar):
    I += [l]
    n_l=neg(l)
    del Lvar[Lvar.index(l//2)]
    for j in (LC[l-1]):
        etat[j-1]=1
        #on chage la longueur dela clause ?
    for k in (LC[n_l-1]):
        long[k-1]-=1
        if long[k-1]==0:
            return False
    return True


#donne la negation d un litteral
def neg(l):
    return(l+2*(l%2)-1)





