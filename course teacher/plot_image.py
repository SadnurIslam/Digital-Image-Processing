import cv2
import matplotlib.pyplot as plt

# Load the image (change the filename as needed)
img = cv2.imread('images/bird.jpg')  # Replace 'image.jpg' with your actual file name

# Convert BGR to RGB for correct display in matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the image
plt.imshow(img_rgb)
plt.title('Uploaded Image')
plt.axis('off')  # Hide axis
plt.show()
