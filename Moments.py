import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def MomentsGeometriques(I,p,q):

    [dimX,dimY]=np.shape(I)       # recuperer les dimensions de I
    res=0
    x=np.arange(0,dimX)
    y=np.arange(0,dimY)
    # M = np.zeros([N,N])       # init de la matrice des moments


    Vx=np.vander(x,dimX,True)       #creation d'une matrice vandermonde pour x
    Vy=np.vander(y,dimY,True)

    for i in range (dimX):           #parcourir l'image en x et y
        for j in range(dimY):
            if I[i,j]==1 :     # si le pixel egale a 1
                res+=Vx[i,p]*Vy[j,q]

    return res
def MomentsCentresEtNormes(I,p,q):
    omega=MomentsGeometriques(I,0,0)
    x_bar=MomentsGeometriques(I,1,0)/omega
    y_bar=MomentsGeometriques(I,0,1)/omega
    res=0
    [dimX, dimY] = np.shape(I)
    x = np.arange(0, dimX)
    y = np.arange(0, dimY)

    Vx=np.vander(x-x_bar,dimX,True)
    Vy=np.vander(y-y_bar,dimY,True)

    dem = omega ** ((p + q + 2) / 2)
    for i in range (dimX):
        for j in range(dimY):
            if I[i,j]==1 :
                res+=Vx[i,p]*Vy[j,q]/dem

    return res

def MatMomentsCentresEtNormes(I,N):
    M=np.zeros([N,N])
    for p in range (N):
        for q in range (N-p):
            M[p,q]=MomentsCentresEtNormes(I,p,q,N)
    return M


