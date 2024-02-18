#Low-pass filtering

import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\pattern.tif')

krnl = np.ones((5,5),np.float32)/25
smoothimg = cv2.filter2D(img,-1,krnl)

plt.subplot(121);
plt.imshow(img,'gray');
plt.title('Orginal Image')
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(smoothimg)
plt.title('Smoothened Image')
plt.xticks([]), plt.yticks([])
plt.show()
