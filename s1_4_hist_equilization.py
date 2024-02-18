import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Std Images\\cameraman.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = (cdf / cdf.max()) * hist.max()

plt.title('Original Image')
plt.imshow( img, cmap = 'gray')
plt.show();

plt.title('Histogram of Image')
plt.plot(cdf, color = 'r')
plt.xlim([0,256])
plt.show(); 

plt.title('Normalized Histogram')
plt.plot(cdf_normalized, color = 'r')
plt.plot(hist, color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show(); 

img2 = cdf_normalized[img]

hist,bins = np.histogram(img2.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = (cdf / cdf.max()) * hist.max()

plt.title('Histogram Equalized Image')
plt.imshow( img2, cmap = 'gray')
plt.show()
plt.title('Histogram Of Equalized Image')
plt.plot(cdf_normalized, color = 'r')
plt.plot(hist, color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

