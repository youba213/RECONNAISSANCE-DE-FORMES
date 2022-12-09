import numpy as np
from skimage import io
from Moments import *
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
def matCoefficientLegendre(N):
    M = np.zeros([N, N])
    for i in range (N):
         for j in range(i+1):
                 M[i,j]=coefficientLegendre(i,j)
    return M

def momentsDeLegendre(p,q,I,N):             #fonction pour calculer les moments de legendre
    a=matCoefficientLegendre(N)
    C = coefDeNormalisation(N)
    res=0
    for i in range(p):
        for j in range(q):
            res+=a[p,i]*a[q,j]*MomentsCentresEtNormes(I,p,q)
    return  res*C

def coefDeNormalisation(N):
    return (2*N+1)*(2*N+1)/4


def MatMomentsDeLegendre(I,N):          #fonction pour remplir la matrice des moments de legendre
    M=np.zeros([N,N])
    for p in range (N):
        for q in range(N-p):
                 M[p,q]=momentsDeLegendre(p,q,I,N)
    return M
def PolyDeLegendre(x,n):
    poly=0
    for i in range (n):
        poly+=coefficientLegendre(n-1,i)*x
    return poly