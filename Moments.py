import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def MomentsGeometriques(I,pmax,qmax,N):

    [dimX,dimY]=np.shape(I)       # recuperer les dimensions de I
    x=np.arange(0,dimX)
    y=np.arange(0,dimY)
    M = np.zeros([pmax, qmax])       # init de la matrice des moments


    Vx=np.vander(x,dimX,True)       #creation d'une matrice vandermonde pour x
    Vy=np.vander(y,dimY,True)




    for p in range (pmax):              #parcourir la matrice  des moments en p et q
         for q in range(qmax):
             if p+q<N :
                for x in range (dimX):           #parcourir l'image en x et y
                     for y in range(dimY):
                         if I[x,y]==1 :     # si le pixel egale a 1
                            M[p,q]+=Vx[x,p]*Vy[y,q]

    return M
def momentsCentresEtNormes(I,pmax,qmax,N):
    M=MomentsGeometriques(I, pmax, qmax,N)
    omega=M[0,0]
    x_bar=M[1,0]/omega
    y_bar=M[0,1]/omega

    [dimX, dimY] = np.shape(I)
    x = np.arange(0, dimX)
    y = np.arange(0, dimY)

    Vx=np.vander(x-x_bar,dimX,True)
    Vy=np.vander(y-y_bar,dimY,True)


    Mcn=np.zeros([pmax,qmax])

    for p in range (0,pmax):
         for q in range(0,qmax):
             if p+q<N:
                dem = omega ** ((p + q + 2) / 2)
                for x in range (0,dimX):
                     for y in range(0,dimY):
                         if I[x,y]==1 :
                            Mcn[p,q]+=Vx[x,p]*Vy[y,q]
                Mcn[p,q]=Mcn[p,q]/dem

    return Mcn


