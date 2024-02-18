#High-Pass filtering

import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\cameraman.tif')
ht=img.shape[0];
wd=img.shape[1];
fltrmask1 = np.ones((3,3),np.float32)
fltrmask1[2,2]=-8;
actualimg=np.zeros((ht,wd))
hipasimg=cv2.filter2D(img,-1,fltrmask1);

for i in range(ht):
    for j in range(wd):
        actualimg[i,j]=img.item(i,j,0)+hipasimg.item(i,j,0)

plt.subplot(232);plt.imshow(img,'gray');
plt.title('Orginal Image')
plt.xticks([]), plt.yticks([])
plt.subplot(234);plt.imshow(hipasimg,'gray');
plt.title('Discontinuity Map');
plt.xticks([]), plt.yticks([])
plt.subplot(236);plt.imshow(actualimg,'gray');
plt.title('Highpass Filtered Image');
plt.xticks([]), plt.yticks([])
plt.show()
