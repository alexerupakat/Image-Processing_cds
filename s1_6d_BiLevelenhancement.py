#Bi-level or binary contrast enhancement

import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\tire.tif')
ht=img.shape[0];
wd=img.shape[1];
cenhimg=np.zeros((ht,wd))
threshold=50

for i in range(ht):
    for j in range(wd):
        if (img.item(i,j,0)<threshold):
            cenhimg[i,j]= 0
        else:
            cenhimg[i,j]=255

plt.subplot(121);plt.imshow(img,'gray');
plt.title('Orginal Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122);plt.imshow(cenhimg,'gray');
plt.title('Binary Contrast Enhanced image');
plt.xticks([]), plt.yticks([])
plt.show()
