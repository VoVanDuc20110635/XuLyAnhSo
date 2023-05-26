import cv2
import numpy as np


def gammaC(src, gamma):
    daoNguocGamma = 1 / gamma
    #Gamma is an important but seldom understood characteristic of virtually all digital imaging systems. It defines the relationship between a pixel's numerical value and its actual luminance. Without gamma, shades captured by digital cameras wouldn't appear as they did to our eyes (on a standard monitor). It's also referred to as gamma correction, gamma encoding or gamma compression, but these all refer to a similar concept. Understanding how gamma works can improve one's exposure technique, in addition to helping one make the most of image editing.
    table = [((i / 255) ** daoNguocGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


hinhAnh = cv2.imread('test.jpg')
anhGamma = gammaC(hinhAnh, 2.2)

cv2.imshow('Anh ban dau', hinhAnh)

cv2.imshow('Anh ket thuc', anhGamma)

cv2.waitKey(0)

cv2.destroyAllWindows()