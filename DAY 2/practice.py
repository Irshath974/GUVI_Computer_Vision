import cv2
import matplotlib.pyplot as plt

img=cv2.imread("noise img.jpeg")
median = cv2.medianBlur(img,3)
plt.imshow(cv2.cvtColor(median,cv2.COLOR_BGR2RGB))
plt.show()