#Brightness slicing

import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\kidney.tif')
ht=img.shape[0];
wd=img.shape[1];
slcwtbg=np.zeros((ht,wd))
slcwotbg=np.zeros((ht,wd))
L=256
a=175
b=256

for i in range(ht):
    for j in range(wd):
        if (img.item(i,j,0)>=a and img.item(i,j,0)<=b):
            slcwotbg[i,j]= L;
            slcwtbg[i,j]=L;
        else:
            slcwotbg[i,j]=0;
            slcwtbg[i,j]=img.item(i,j,0);

plt.subplot(232);plt.imshow(img,'gray');
plt.title('Orginal Image') 
plt.xticks([]),plt.yticks([])
plt.subplot(236);plt.imshow(slcwotbg,'gray');
plt.title('Slicing Without Background'); 
plt.xticks([]), plt.yticks([])
plt.subplot(234);plt.imshow(slcwtbg,'gray');
plt.title('Slicing With Background'); 
plt.xticks([]), plt.yticks([])
plt.show()
