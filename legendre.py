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
                return ((-n+1)/n) * coefficientLegendre(n-2, 0);
            else:
                if (i >= n-1):
                    return (((2 * (n-1) + 1)/n) * coefficientLegendre(n-1,i-1));
                else:
                    return (((2 *(n-1)+1)/n) * coefficientLegendre(n - 1, i - 1) + (-(n-1) / n) * coefficientLegendre(n - 2, i));
def matCoefficientLegendre(N):
    M = np.zeros([N, N])
    M[0,0]=1
    M[1,0]=0
    M[1,1]=1

    for n in range (2,N):
         for i in range(n+1):
             if (i == 0):
                 M[n,i]=((-n+1)/n) *M[n-2,0]
             else:
                 if (i>=n-1):
                     M[n][i]=((2*(n-1)+1)/n)* M[n-1,i-1];
                 else:
                     M[n,i]=((2*(n-1)+1)/n)* M[n-1,i-1] +((-n+1)/n)*M[n-2,i];

    return M

def momentsDeLegendre(p,q,MomG,a,C):             #fonction pour calculer les moments de legendre
    res=0
    for i in range(p):
        for j in range(q):
            res+=a[p,i]*a[q,j]*MomG[i,j]
    return  res*C

def coefDeNormalisation(N):
    return (2*N+1)*(2*N+1)/4


def MatMomentsDeLegendre(I,N):          #fonction pour remplir la matrice des moments de legendre
    MomG=MatMomentsCentresEtNormes(I,N)
    a = matCoefficientLegendre(N)
    C = coefDeNormalisation(N)
    M=np.zeros([N,N])
    for p in range (N):
        for q in range(N-p):
                 M[p,q]=momentsDeLegendre(p,q,MomG,a,C)
    return M
def PolyDeLegendre(x,n,M):
    poly=0
    for i in range (n+1):
        poly+=M[n,i]*pow(x,i)
    return poly
def MatPolyDeLegendre(dimX,N):
    MP=np.zeros([dimX,N])
    M = matCoefficientLegendre(N)
    for x in range(dimX):
        for n in range (N):
            MP[x,n]=PolyDeLegendre(2*x/dimX-1,n,M)
    return MP