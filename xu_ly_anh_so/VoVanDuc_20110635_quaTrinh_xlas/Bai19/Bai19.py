# Pyramids. Construct an image pyramid. The inputs should be a grayscale or
# color image, a separable filter kernel, and the number of desired levels. Implement at least
# the following kernels:
# • 2 × 2 block filtering;
# • Burt and Adelson’s binomial kernel 1=16(1; 4; 6; 4; 1) (Burt and Adelson 1983a);
# • a high-quality seven- or nine-tap filter.
# Compare the visual quality of the various decimation filters. Also, shift your input image by
# 1 to 4 pixels and compare the resulting decimated (quarter size) image sequence.



import imutils
from skimage.transform import pyramid_gaussian as pg

import cv2
import os


def kimtuthap(image, scale=1.5, kichThuocNhoNhat=(32, 32)):

	yield image

	while True:

		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)

		if image.shape[0] < kichThuocNhoNhat[1] or image.shape[1] < kichThuocNhoNhat[0]:
			break

		yield image

#Pyramid, or pyramid representation, is a type of multi-scale signal representation developed by the computer vision, image processing and signal processing communities, in which a signal or an image is subject to repeated smoothing and subsampling
def build(image, scale_in):
	

	hinhAnh = cv2.imread(image)

	for (i, resized) in enumerate(kimtuthap(hinhAnh, scale=scale_in)):

		cv2.imshow("Layer {}".format(i + 1), resized)
		cv2.waitKey(0)

	cv2.destroyAllWindows()

	for (i, resized) in enumerate(pg(hinhAnh, downscale=2)):

		if  resized.shape[1] < 30 or  30 > resized.shape[0] :
			break

		cv2.imshow("Layer {}".format(i + 1), resized)
		cv2.waitKey(0)


duong_dan_fule=os.path.split(os.path.abspath(__file__))[0]
ten_file='vovanduc_1.jpg'
teptin = os.path.join(duong_dan_fule, ten_file)
build(teptin, 1.5)