#Brightness enhancement

import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\office_1.jpg')

brimage=img+70;

plt.subplot(121);
plt.imshow(img,'gray');plt.title('Orginal image')
plt.xticks([]), plt.yticks([])

plt.subplot(122);
plt.imshow(brimage,'gray');plt.title('Brightness enhanced image');
plt.xticks([]), plt.yticks([])
plt.show()
