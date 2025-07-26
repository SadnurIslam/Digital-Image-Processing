import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('images/bird.jpg')  # Replace with your image filename
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create negative
negative_img = 255 - img_rgb

# Display original and negative images
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(negative_img)
plt.title('Negative Image')
plt.axis('off')

plt.show()
