import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def MomentsGeometriques(I,dimX,dimY,p,q,Vx,Vy):
    res=0
    for i in range (dimX):           #parcourir l'image en x et y
        for j in range(dimY):
            if I[i,j]==1 :           # si le pixel egale a 1
                res+=Vx[i,p]*Vy[j,q]

    return res
def MomentsCentresEtNormes(I,p,q,Vx2,Vy2,omega,dimX,dimY):
    res=0
    dem = omega ** ((p + q + 2) / 2)
    for i in range (dimX):
        for j in range(dimY):
            if I[i,j]==1 :
                res+=Vx2[i,p]*Vy2[j,q]/dem

    return res

def MatMomentsCentresEtNormes(I,N):
    [dimX, dimY] = np.shape(I)
    x = np.arange(0, dimX)                                          # vecteur x
    y = np.arange(0, dimY)                                          # vecteur y
    Vx = np.vander(x, N, True)                                      # creation d'une matrice vandermonde pour x d'ordre p
    Vy = np.vander(y, N, True)

    omega=MomentsGeometriques(I,dimX,dimY,0,0,Vx,Vy)
    x_bar=MomentsGeometriques(I,dimX,dimY,1,0,Vx,Vy)/omega
    y_bar=MomentsGeometriques(I,dimX,dimY,0,1,Vx,Vy)/omega

    Vx2 = np.vander(x - x_bar, N, True)     # creer une matrice vandermonde pour x-x_bar
    Vy2 = np.vander(y - y_bar, N, True)
    M=np.zeros([N,N])                          #init de la mat des mom zeros

    for p in range (N):
        for q in range (N-p):
            M[p,q]=MomentsCentresEtNormes(I,p,q,Vx2,Vy2,omega,dimX,dimY)
    return M


