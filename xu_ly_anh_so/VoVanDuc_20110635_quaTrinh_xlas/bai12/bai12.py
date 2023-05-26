#  Sharpening, blur, and noise removal. Implement some softening, sharpening, and
# non-linear diffusion (selective sharpening or noise removal) filters, such as Gaussian, median,
# and bilateral (Section 3.3.1), as discussed in Section 3.4.2.
# Take blurry or noisy images (shooting in low light is a good way to get both) and try to
# improve their appearance and legibility.

import cv2
import numpy as np

img = cv2.imread('cuocduakythu.png')
rows, cols = img.shape[:2]

#Sharpening tends to make image noise more visible. Increasing the threshold can help to reduce this by telling the unsharp mask to ignore certain parts of the image. However, this can also mean that different parts of the image are not sharpened consistently.

kernel_25 = np.ones((25,25), np.float32) / 625.0
output_kernel = cv2.filter2D(img, -1, kernel_25)
output_blur = cv2.blur(img, (25,25))
output_box = cv2.boxFilter(img, -1, (5,5), normalize=False)


cv2.imshow('kernel blur', output_kernel)
cv2.imshow('Blur() output', output_blur)
cv2.imshow('Box filter', output_box)
cv2.imshow('Original', img)
cv2.waitKey(0)