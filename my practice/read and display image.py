import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/bird.jpg')  # Load the image from the specified path
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()
