import cv2
from matplotlib import pyplot as plt
import numpy as np


# Padding for neighborhood operations. Write down the formulas for computing
# the padded pixel values f~(i; j) as a function of the original pixel values f(k; l) and the image
# width and height (M; N) for each of the padding modes shown in Figure 3.13. For example,
# for replication (clamping)
#

img = cv2.imread('meo.jpg')
kernal = np.array([(1,1,1),(1,1,1),(1,1,1)]) * (1/9)
kernal1 = np.array([(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1),(1,1,1,1,1)])*(1/9)
cv2.imshow('original', img)
s = img.shape
K = kernal1.shape


top = bottom = 150
left = right  = 150
constant = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT)
print('image= ', constant)
cv2.imshow('Padded image', constant)
cv2.waitKey(0)




# Since neighborhood operations will require you to access
# pixels "off the edge" of the image when you are near the
# borders, it is necessary to first pad the image.
# In this manner, you effectively make a somewhat larger
# image (with padding) and can begin processing the image by
# centering the kernel in the interior of the image (instead
# of the upper left corner).