import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('C:\\Std Images\\localnoise.tif')

M = img.shape[0]
N = img.shape[1]
mid=round((M*N)/2)
inp=0

for i in range(M):
    for j in range(N):  
        inp=inp+1;
        if(inp==mid):
            MPad=i+1-1
            NPad=j+1-1
            break;
padimage=cv2.copyMakeBorder(img,MPad,MPad,NPad,NPad,cv2.BORDER_CONSTANT,0)
iht=padimage.shape[0]
iwd=padimage.shape[1]
nht=iht-((MPad*2)+1)
nwd=iwd-((NPad*2)+1)
loc_Heq=np.zeros((nht,nwd))

ele=0
for i in range(nht-1):
    for j in range(nwd-1):
        cdf=np.zeros((256,1))
                
inc=1
for x in range(M):
    for y in range(N):
        if(inc==mid):
            ele=padimage[(i+1)+(x+1)-1,(j+1)+(y+1)-1][0]+1
        pstnx=i+x+1
        pstny=j+y+1
        pos=padimage.item(pstnx, pstny,0)
        cdf[pos]=cdf.item(pos)+1
        inc=inc+1
    for l in range(256):
        cdf[l]=cdf.item(l)+cdf.item(l-1)
loc_Heq[i+1,j+1]=round(cdf[ele][0]/(M*N)*255)

plt.subplot(121);plt.imshow(img,'gray');
plt.title('    Original Image      ')
plt.xticks([]), plt.yticks([])

plt.subplot(122);plt.imshow(loc_Heq,'gray');
plt.title('Local Histogram equalized Image')
plt.xticks([]), plt.yticks([])
plt.show()
