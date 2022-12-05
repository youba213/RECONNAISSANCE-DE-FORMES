import numpy as np
from skimage import io
from matplotlib import pyplot as plt


def MomentsGeometriques(I,pmax,qmax):

    [dimX,dimY]=np.shape(I)
    x=np.arange(0,dimX)
    y=np.arange(0,dimX)


    Vx=np.vander(x,dimX,True)
    Vy=np.vander(y,dimY,True)


    M=np.zeros([pmax,qmax])

    for p in range (0,pmax):
         for q in range(0,qmax):
             if p+q<5 :
                for x in range (0,dimX):
                     for y in range(0,dimY):
                         if I[x,y]==1 :
                            M[p,q]+=Vx[x,p]*Vy[y,q]

    return M
def momentsCentresEtNormes(I,pmax,qmax):
    M=MomentsGeometriques(I, pmax, qmax)
    omega=M[0,0]
    x_bar=M[1,0]/omega
    y_bar=M[0,1]/omega

    [dimX, dimY] = np.shape(I)
    x = np.arange(0, dimX)
    y = np.arange(0, dimX)

    Vx=np.vander(x-x_bar,dimX,True)
    Vy=np.vander(y-y_bar,dimY,True)


    Mcn=np.zeros([pmax,qmax])

    for p in range (0,pmax):
         for q in range(0,qmax):
             if p+q<5 :
                dem = omega ** ((p + q + 2) / 2)
                for x in range (0,dimX):
                     for y in range(0,dimY):
                         if I[x,y]==1 :
                            Mcn[p,q]+=Vx[x,p]*Vy[y,q]
                Mcn[p,q]=Mcn[p,q]/dem

    return Mcn


