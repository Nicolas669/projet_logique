import random
#m est le nb de clauses, k le nb de variables
def tcnfgen(m,k,horn=1):
    cnf = []
    def unique(l,k):
        t = random.randint(1,k)
        while(t in l):
            t = random.randint(1,k)
        return t
    r = (lambda : random.randint(0,1))
    for i in range(m):
        x = unique([],k)
        y = unique([x],k)
        z = unique([x, y],k)
        if horn:
            cnf.append([(x,1), (y,0),(z,0)])
        else:
            cnf.append([(x,r()), (y,r()),(z,r())])
    return cnf

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

#nb de trous
def gen_pigeons(n):
    CL=[]
    LC=[[]]*(2*n*(n+1))
    compte=0
    for i in range (1,n+2):
        C=[]
        p=2*(i-1)*n+1
        while p<2*n*i+1:
            C+=[p]
            p+=2

        CL+=[C]
        compte+=1
        for l in C:
            LC[l-1]=LC[l-1]+[compte]
        for a in range (1,n):
            for b in range (a+1,n+1):
                D=[2*((i-1)*n+a),2*((i-1)*n+b)]
                CL+=[D]
                compte+=1
                for l in D:
                    LC[l - 1] = LC[l - 1] + [compte]
    for j in range (1,n+1):
        for a in range (1,n+1):
            for b in range (a+1,n+2):
                E=[(a-1)*n+2*j,(b-1)*n+2*j]
                CL+=[E]
                compte+=1
                for l in E:
                    LC[l - 1] = LC[l - 1] + [compte]
    return(CL,LC)




