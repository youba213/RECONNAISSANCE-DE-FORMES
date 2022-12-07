import numpy as np
from skimage import io
from Moments import MomentsGeometriques,momentsCentresEtNormes
from matplotlib import pyplot as plt

def coefficientLegendre(n,i):
    if (n==0 and i==0):
        return 1
    else:
        if (n==1 and i==0):
            return 0
        else:
            if(n!=1 and i==0):
                return ((-n-1) / n) * coefficientLegendre(n - 2, 0);
            else:
                if (i >= n-1):
                    return (((2 * (n-1) + 1)/n) * coefficientLegendre(n-1,i-1));
                else:
                    return (((2 *(n-1)+1)/n) * coefficientLegendre(n - 1, i - 1) + (-(n-1) / n) * coefficientLegendre(n - 2, i));
def matCoefficientLegendre(x,y):
    M = np.zeros([x, y])
    for i in range (x):
         for j in range(y):
             if j <= i:
                 M[i,j]=coefficientLegendre(i,j)
    return M

def momentsDeLegendre(p,q,pmax,qmax,I,N):             #fonction pour calculer les moments de legendre
    a=matCoefficientLegendre(pmax,qmax)
    n=momentsCentresEtNormes(I,pmax,qmax,N)
    C = coefDeNormalisation(pmax, qmax)
    res=0
    for i in range(pmax):
        for j in range(qmax):
            res+=a[p,i]*a[q,j]*n[i,j]
    return  res*C

def coefDeNormalisation(pmax,qmax):
    return (2*pmax+1)*(2*qmax+1)/4


def MatMomentsDeLegendre(I,pmax,qmax,N):          #fonction pour remplir la matrice des moments de legendre
    M=np.zeros([pmax,qmax])
    for p in range (pmax):
        for q in range(qmax):
            if p+q<N:
                 M[p,q]=momentsDeLegendre(p,q,pmax,qmax,I,N)
    return M
def PolyDeLegendre(x,n):
    poly=0
    for i in range (n):
        poly+=coefficientLegendre(n-1,i)*x
    return poly