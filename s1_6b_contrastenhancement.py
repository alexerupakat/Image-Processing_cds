#Contrast enhancement

import numpy as np
import cv2
from matplotlib import pyplot as plt

I=cv2.imread('C:\\Std Images\\washedoutpollen.tif')

ht=I.shape[0];
wd=I.shape[1];
conimg=I.copy()

a=0;
b=255;
min=np.amin(I)
max=np.amax(I)
slope=(b-a)/(max-min);

for x in range(ht):
    for y in range(wd):
        conimg[x,y]=slope*(I[x,y]-min)+a;

plt.subplot(121);plt.imshow(I,'gray');
plt.title('Original Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122);plt.imshow(conimg,'gray');
plt.title('Contrast enhanced image');
plt.xticks([]), plt.yticks([])
plt.show()

