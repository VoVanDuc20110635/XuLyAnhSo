from cv2 import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

# Local histogram equalization. Compute the gray level (luminance) histograms for
# each patch, but add to vertices based on distance (a spline).
# 1. Build on Exercise 3.7 (luminance computation).
# 2. Distribute values (counts) to adjacent vertices (bilinear).
# 3. Convert to CDF (look-up functions).
# 4. (Optional) Use low-pass filtering of CDFs.
# 5. Interpolate adjacent CDFs for final lookup

flower = cv2.imread("anhbai8.png")
flower = cv2.resize(flower, (800,600))
s = flower.shape

flowerGray = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)
flowerGray = cv2.convertScaleAbs(flowerGray, alpha=1.10, beta=-20)

H = np.zeros(shape=(256,1))
for i in range(s[0]):
    for j in range(s[1]):
        k = flowerGray[i,j]
        H[k,0] = H[k,0] + 1

print(H)
plt.plot(H)
plt.show()
