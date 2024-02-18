import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

image = mpimg.imread('C:\\Std Images\\cameraman.tif');

#TRANSLATION
row,col = np.shape(image);
transImg = np.zeros((row,col),dtype='double'); 
tx = int(input('Enter the value of tx   = '));#50; 
ty = int(input('Enter the value of ty   = '));#50; 
for i in range(row-tx):
    for j in range(col-ty): 
        transImg[i+tx,j+ty]=image[i,j];

#ROTATION
r,c=np.shape(image);
angle = int(input('Enter the Rotaion angle = '));#45; 
radian = angle*(np.pi/180); x=np.uint8(np.floor(r/2)); 
y=np.uint8(np.floor(c/2)); 
l=0.0;
m=0.0;
rotImg=np.zeros((r+r,c+c),dtype='double')
for i in range(r):
    p=i-x;
    for j in range(c):
        q=j-y;
        l=p*np.cos(radian)-q*np.sin(radian);
        m=p*np.sin(radian)+q*np.cos(radian);
        l=l+x+(r/2);
        m=m+y+(c/2);
        l=np.uint16(np.round(l));
        m=np.uint16(np.round(m));
        rotImg[l,m]=image[i,j];
        rotImg[l,m-1]=image[i,j];
        rotImg[l,m+1]=image[i,j];
        rotImg[l-1,m]=image[i,j];
        rotImg[l+1,m]=image[i,j];


#SCALING
row,col=np.shape(image); 
scaledImg=np.zeros([row,col]) 
sx = float(input('Enter the value of sx   = '));#0.8; 
sy = float(input('Enter the value of sy   = '));#0.5; 
S=[[sx, 0],[0,sy]];
for i in range(0,row): 
    for j in range(0,col):
        P=[[i],[j]]
        Scal=np.int16(np.floor(np.matmul(S,P)));
        scaledImg[Scal[0],Scal[1]]=image[i,j]

#SKEWING
row,col=np.shape(image)
skx = float(input('Enter the value of skx = '));#0.1;
sky = float(input('Enter the value of sky = '));#1; 
SK=[[1, skx],[sky,1]]; 
skewImg=np.zeros([row+np.int(skx*row),col+np.int(sky*col)]) 
for i in range(0,row):
    for j in range(0,col): 
        P=[[i],[j]] 
        Skew=np.int16(np.floor(np.matmul(SK,P))); 
        skewImg[Skew[0],Skew[1]]=image[i,j];
    
plt.subplot(231);
plt.title('Original Image');
plt.imshow(image); plt.xticks([]), plt.yticks([])

plt.subplot(232);
plt.title('Translated Image'); 
plt.imshow(transImg); plt.xticks([]), plt.yticks([])

plt.subplot(233);
plt.title('Rotated Image');
plt.imshow(rotImg); plt.xticks([]), plt.yticks([])

plt.subplot(235);
plt.title('Scaled Image'); 
plt.imshow(scaledImg); plt.xticks([]), plt.yticks([])

plt.subplot(236);
plt.title('Skewed Image'); 
plt.imshow(skewImg); plt.xticks([]), plt.yticks([])
plt.show();
