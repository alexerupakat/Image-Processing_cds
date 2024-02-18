import cv2
from matplotlib import pyplot as plt

image = cv2.imread('C:\\Std Images\\sailboat.jpg')

b,g,r = cv2.split(image)
image = cv2.merge([r,g,b])
imght = image.shape[0]
imgwd = image.shape[1]
cv2.imwrite('newimage.jpg',image)

plt.xticks([]), plt.yticks([])
newimg = cv2.imread('newimage.jpg')
plt.subplot(121);plt.imshow(image);plt.title('orginal image');
plt.xticks([]), plt.yticks([])
plt.subplot(122);plt.imshow(newimg);plt.title('copied image');
plt.xticks([]), plt.yticks([])

print ("   Image Information")
print ("Image Tyoe : ",type(image))
print ("Width      : ",imgwd)
print ("Height     : ",imght)
print ("Size       : ",image.size)
print ("Data Type  : ",image.dtype)
print ("Size of New Image  : ",newimg.size)
cpr = float(image.size/newimg.size)
print ("Compression Ration : ", cpr)
