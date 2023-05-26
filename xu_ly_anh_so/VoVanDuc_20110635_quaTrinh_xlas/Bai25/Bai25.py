# Local image warping. Open an image and deform its appearance in one of the
# following ways:184 Computer Vision: Algorithms and Applications (March 27, 2021 draft)
# 1. Click on a number of pixels and move (drag) them to new locations. Interpolate the
# resulting sparse displacement field to obtain a dense motion field (Sections 3.6.2 and
# 3.5.1).
# 2. Draw a number of lines in the image. Move the endpoints of the lines to specify their
# new positions and use the Beier–Neely interpolation algorithm (Beier and Neely 1992),
# discussed in Section 3.6.2, to get a dense motion field.

from PIL import Image
import math
import cv2
import os

def do_dai_vector(vector):
  return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def points_distance(point1, point2):
  return do_dai_vector((point1[0] - point2[0],point1[1] - point2[1]))

def clamp(value, minimum, maximum):
  return max(min(value,maximum),minimum)

## Warps an image accoording to given points and shift vectors.
#  
#  @param image input image
#  @param points list of (x, y, dx, dy) tuples
#  @return warped image


# 3. Overlay a spline control grid and move one grid point at a time (optionally select the
# level of the deformation).
# 4. Have a dense per-pixel flow field and use a soft “paintbrush” to design a horizontal and
# vertical velocity field.
# 5. (Optional): Prove whether the Beier–Neely warp does or does not reduce to a sparse
# point-based deformation as the line segments become shorter (reduce to points)

def warp(image, points):

  ketqua = hinhAnh = Image.new("RGB",image.size,"black")

  pixelhinhanh = image.load()

  pixelketqua = ketqua.load()

  for y in range(image.size[1]):

    for x in range(image.size[0]):

      offset = [0,0]

      for item in points:

        point_position = (item[0] + item[2],item[1] + item[3])

        shift_vector = (item[2],item[3])

        helper = 1.0 / (3 * (points_distance((x,y),point_position) / do_dai_vector(shift_vector)) ** 4 + 1)

        offset[0] -= helper * shift_vector[0]

        offset[1] -= helper * shift_vector[1]

      coords = (clamp(x + int(offset[0]),0,image.size[0] - 1),clamp(y + int(offset[1]),0,image.size[1] - 1))


      pixelketqua[x,y] = pixelhinhanh[coords[0],coords[1]]

  return ketqua


duong_dan_file=os.path.split(os.path.abspath(__file__))[0]

ten_file='vovanduc_1.jpg'

tap_tin = os.path.join(duong_dan_file, ten_file)


image = Image.open(tap_tin)

img=cv2.imread(tap_tin)

cv2.imshow('daura', img) #cho 1 chut

cv2.waitKey(0)

image = warp(image,[(220,286,110,-110), (20,87,-20,-20), (87,463,60,-90)])

image.save("fileketqua.png","PNG")

img=cv2.imread("fileketqua.png")

cv2.imshow('out', img)

cv2.waitKey(0)
