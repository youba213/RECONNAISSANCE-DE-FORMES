import numpy as np
from skimage import io
from skimage.color import rgb2gray
from Moments import MomentsGeometriques,momentsCentresEtNormes
from legendre import *
from matplotlib import pyplot as plt

# I=np.zeros((10,10))
# I[2:8,2:8]=1;
# p,q=5,5
# N=5

I=io.imread("caree3.png")
I=rgb2gray(I)
p,q=10,10
N=20

plt.figure(1)
plt.imshow(I, cmap='gray')
# plt.show()

# plt.xlim(0, 9)
# plt.ylim(0, 9)
# plt.show()




# [dimX,dimY]=np.shape(I)
print(np.shape(I))
# print(matCoefficientLegendre(5,5))
# print(momentsCentresEtNormes(I,p,q))
print(MatMomentsDeLegendre(I,p,q,N))
# print(PolyDeLegendre(1,5))


