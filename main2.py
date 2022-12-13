import numpy as np
from skimage import io
from skimage.color import rgb2gray
from Moments import *
from legendre import *
from matplotlib import pyplot as plt
from Reconstruction import *

I=io.imread("triangle.png")
I=rgb2gray(I)
plt.figure(1)
plt.imshow(I, cmap='gray')
[dimX,dimY]=np.shape(I)

N=50

Ml=MatMomentsDeLegendre(I,N)
# poly=PolyDeLegendre(9,20)
# print(matCoefficientLegendre(N))
# print(MomentsCentresEtNormes(I,4,4))
IR=ImgReconstruite(dimX,dimY,N,Ml)
print(Ml)


plt.figure(2)
plt.imshow(IR, cmap='gray')
plt.show()