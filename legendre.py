import numpy as np
from skimage import io
from Moments import MomentsGeometriques,momentsCentresEtNormes
from matplotlib import pyplot as plt

def coefficientLegendre(x,i):
    if (x==1 and i==0):
        return 1
    else:
        if (x==1 and i==0):
            return 0
        else:
            if(x!=1 and i==0):
                return ((-x-1) / x) * coefficientLegendre(x - 2, 0);
            else:
                if (i >= x - 1):
                    return (((2 * (x-1) + 1) / x) * coefficientLegendre(x - 1, i - 1));
                else:
                    return (((2 * (x-1) + 1) / x) * coefficientLegendre(x - 1, i - 1) + (
                                -(x-1) / x) * coefficientLegendre(x - 2, i));