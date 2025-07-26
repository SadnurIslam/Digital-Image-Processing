import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert to RGB
img = cv2.imread('images/bird.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# # Extract channels
R = img_rgb[:, :, 0]
G = img_rgb[:, :, 1]
B = img_rgb[:, :, 2]

print(R)
# #  color 
plt.subplot(3,2,1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(3, 2, 2)
plt.imshow(R, cmap='Reds')    
plt.title('Red Channel')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.imshow(G, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.imshow(B, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

img_sum = cv2.merge((R, G, B))

plt.subplot(3, 2, 5)
plt.imshow(img_sum)
plt.title('Combined Channels')
plt.axis('off')

plt.tight_layout()
plt.show()

if(img_rgb==img_sum).all():
    print("The sum of the channels equals the original image.")
else:
    print("The sum of the channels does not equal the original image.")
