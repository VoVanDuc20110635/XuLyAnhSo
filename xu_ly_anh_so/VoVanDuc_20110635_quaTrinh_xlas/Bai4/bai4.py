import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
#Blue screen matting requires a reference image of a non-blue foreground against a pureblue background. The blue background from the monitor did not photograph as pure blue and light reflections onto the foreground caused confusion in the algorithm. For pixels what were significantly more blue than they were either red or yellow, an alpha value was calculated to be one minus the pixel's blue channel.

def thayDoiBackGround(image_in):
      hinhAnh = cv2.imread(image_in)
      cv2.imshow('in',hinhAnh)
      cv2.waitKey(0)
      print('Hinh anh hien tai:', type(hinhAnh),
            ' dich den:', hinhAnh.shape)

      hinhAnhCopy = np.copy(hinhAnh)
      plt.imshow(hinhAnhCopy)

      hinhAnhCopy = cv2.cvtColor(hinhAnhCopy, cv2.COLOR_BGR2RGB)
      plt.imshow(hinhAnhCopy)

      xanhThuong = np.array([0,0,230])
      xanhHoa = np.array([250,250,255])

      mask = cv2.inRange(hinhAnhCopy, xanhThuong, xanhHoa)
      plt.imshow(mask, cmap='gray')

      anhKhauTrang = np.copy(hinhAnhCopy)
      anhKhauTrang[mask != 0] = [0, 0, 0]
      plt.imshow(anhKhauTrang)

      nenAnh = np.zeros(hinhAnh.shape, np.uint8)
      nenAnh[:] = (0, 128, 0)

      #This solution did not wor well for the image below. All three of the results are entirely tinted blue because the reference background was not pure blue. For this same reason, the water bottle blends into the rest of the constructed scenes.
      nenAnh = cv2.cvtColor(nenAnh, cv2.COLOR_BGR2RGB)
      crop_background = nenAnh[0:hinhAnh.shape[0], 0:hinhAnh.shape[1]]


      crop_background[mask == 0] = [0,0,0]
      plt.imshow(crop_background)

      complete_image = anhKhauTrang + crop_background
      plt.imshow(complete_image)
      plt.show()

duong_dan_file =os.path.split(os.path.abspath(__file__))[0]
ten_file='vovanduc.jpg'
fileInput = os.path.join(duong_dan_file, ten_file)

thayDoiBackGround(fileInput)







