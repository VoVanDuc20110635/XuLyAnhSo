# Separable filters. Implement convolution with a separable kernel. The input should
# be a grayscale or color image along with the horizontal and vertical kernels. Make sure you
# support the padding mechanisms developed in the previous exercise. You will need this functionality for some of the later exercises. If you already have access to separable filtering in an
# image processing package you are using (such as IPL), skip this exercise


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('theIntern2015.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)


#Which filters are separable?
#What is a separable filter? A two-dimensional filter kernel is separable if it can be expressed as the outer product of two vectors. For example, let's look at a Sobel kernel. This kernel can be written as a matrix product of a column and a row vector.

titles = ['image', '2D convolution']
images = [img, dst]

for i in range(2):
    plt.subplot(1,2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()