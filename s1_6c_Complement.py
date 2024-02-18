#Complement of an image

import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\mammogram.tif')

negimg=255-img

plt.subplot(121);plt.imshow(img,'gray');
plt.title('Orginal Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122);plt.imshow(negimg,'gray');
plt.title('Complement of image');
plt.xticks([]), plt.yticks([])
plt.show()

