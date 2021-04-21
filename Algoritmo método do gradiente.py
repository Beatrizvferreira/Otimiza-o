import numpy as np
from numpy import linalg as la

def grad(X):
    A = np.multiply(X,[2,4])
    return A
    
def metgradconst(X,t):
    tol=np.float(0.000001)
    cont=0
    while (la.norm(grad(X))> tol):
        cont= cont+1
        X=X - t*grad(X)
    f = X[0]**2 + 2*X[1]**2
    print("X = ",X)
    print("f = ",f)
    print("g = ",grad(X))
    print("Iteracoes = ",cont)
    
X= np.array([1,2])
metgradconst(X,0.495)
