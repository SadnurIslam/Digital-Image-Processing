import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('images/bird.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()
