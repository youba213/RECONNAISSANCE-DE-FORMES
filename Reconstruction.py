from legendre import *
import numpy as np

def reconstuction(x,y,N,Ml,MPX,MPY,dimx,dimy):
    res=0
    for p in range (N) :
        for q in range (N-p):
            res+=Ml[p,q]*MPX[x,p]*MPY[y,q]

    return res

def ImgReconstruite(dimx,dimy,N,Ml):
    MPX=MatPolyDeLegendre(dimx,N)  # matice de polynome de legendre de dimx,N
    MPY=MatPolyDeLegendre(dimy,N)  # matice de polynome de legendre de dimy,N
    Img=np.zeros([dimx,dimy])
    for x in range(dimx):
        for y in range(dimy):
            Img[x,y]=reconstuction(x,y,N,Ml,MPX,MPY,dimx,dimy)
    return Img