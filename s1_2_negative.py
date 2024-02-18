import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Std Images\\mammogram.tif')
negative = abs(255-img);

plt.subplot(121);plt.imshow(img);plt.title('orginal image')
plt.xticks([]), plt.yticks([])
plt.subplot(122);plt.imshow(negative);plt.title('negative image')
plt.xticks([]), plt.yticks([])
