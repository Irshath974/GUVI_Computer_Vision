import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("shadow.jpg")
rows,cols=img.shape[:2]
(h,w)=img.shape[:2]

print(img.shape)


cv2.rectangle(img,(300,300),(100,750),(50,50,50),2)
circle = cv2.circle(img,(30,30),50,(0,0,255),1)
M = np.float32([[1,0,-110],[0,1,0]])
translate=cv2.warpAffine(img,M,(cols,rows))
RM = cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv2.warpAffine(img,RM,(w,h))
plt.imshow(cv2.cvtColor(translate,cv2.COLOR_BGR2RGB))

plt.axis("off")
plt.show()