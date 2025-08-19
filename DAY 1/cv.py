import cv2
import matplotlib.pyplot as plt

img = cv2.imread("copy ninja.jpg")
print(img.shape)


cv2.rectangle(img,(900,900),(1000,750),(550,50,50),2)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()