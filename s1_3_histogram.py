import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:\\Std Images\\lena.jpg')
grayimg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.subplot(232);plt.imshow(image);plt.title('IMAGE') ;
plt.xticks([]), plt.yticks([])

imght=grayimg.shape[0]
imgwd=grayimg.shape[1]
ihist = np.zeros(256)

for x in range(imght):
    for y in range(imgwd):
        pixint=grayimg[x,y]
        ihist[pixint]=ihist[pixint]+1

plt.subplot(234);plt.plot(ihist);plt.title('Histogram')
plt.subplot(236);plt.hist(grayimg.flatten(),256,[0,256]);plt.title('Histogram(using built in function)')
plt.show()
