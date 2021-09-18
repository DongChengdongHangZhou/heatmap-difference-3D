from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import tifffile as tiff
import cv2

img1 = tiff.imread('spectrum_fingerprint_real.tiff')
img2 = tiff.imread('spectrum_fingerprint_fake.tiff')
delta = img1 - img2

figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(0, 256, 1)
Y = np.arange(0, 256, 1)
#网格化数据
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**0.1 + Y**0.1)
Z = np.cos(R)
ax.plot_surface(X, Y, delta, rstride=1, cstride=1, cmap='rainbow')

plt.show()