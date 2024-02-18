import numpy as np
import cv2
import math
import operator
from scipy import misc
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Std Images\\washedoutpollen.tif')
gimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imght=gimg.shape[0]
imgwd=gimg.shape[1]
no_pix=imght*imgwd
Heq=np.zeros((imght, imgwd))
ihist=np.zeros((256,1))
cdfprob=np.zeros((256,1))
cum=np.zeros((256,1))
eqhist=np.zeros((256,1))
for i in range(imght):
    for j in range(imgwd):
            pixint=gimg[i,j]
            ihist[pixint+1]=ihist[pixint+1]+1
csum=0
no_bins=255
for i in range(256):
    csum=csum+ihist[i]
    cum[i]=csum;
    cdfprob[i]=cum[i]/no_pix
    eqhist[i]=round(cdfprob[i]*no_bins)
for i in range(imght):
    for j in range(imgwd):
        pixint=gimg[i,j]
        Heq[i,j]=eqhist[pixint+1]

plt.subplot(121);plt.imshow(gimg,'gray');plt.title('orginal image')
plt.subplot(122);plt.imshow(Heq,'gray');plt.title('Result of Histogram equalization')
plt.show()