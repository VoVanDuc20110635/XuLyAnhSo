# Image denoising. Implement at least two of the various image denoising techniques described in this chapter and compare them on both synthetically noised image sequences and real-world (low-light) sequences. Does the performance of the algorithm depend on the correct choice of noise level estimate? Can you draw any conclusions as to
# which techniques work better?

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

plt.style.use('seaborn')

def get_file(tenTep):

    duong_DAn=os.path.split(os.path.abspath(__file__))[0]

    tepTin = os.path.join(duong_DAn, tenTep)

    return tepTin

hinhAnh = cv2.imread(get_file('vovanduc_1.jpg'))

# image = cv2.cvtColor(image_in, cv2.COLOR_GRAY2BGR)

susimaka = cv2.fastNlMeansDenoisingColored(hinhAnh, None, 11, 6, 7, 21)
 
dong, cot = 1, 2

fig, axs = plt.subplots(dong, cot, figsize=(15, 10))

fig.tight_layout()

#n earlier chapters, we have seen many image smoothing techniques like Gaussian Blurring, Median Blurring etc and they were good to some extent in removing small quantities of noise. In those techniques, we took a small neighbourhood around a pixel and did some operations like gaussian weighted average, median of the values etc to replace the central element. In short, noise removal at a pixel was local to its neighbourhood.

axs[0].imshow(cv2.cvtColor(hinhAnh, cv2.COLOR_BGR2RGB))

axs[0].set_title('dau vao')

axs[1].imshow(cv2.cvtColor(susimaka, cv2.COLOR_BGR2RGB))

axs[1].set_title('dau ra')

plt.show()