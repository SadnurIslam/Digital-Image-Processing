import cv2 
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('images/bird.jpg')  # Load the image from the specified path
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display
    
    # Split the image into its RGB channels
    # r, g, b = cv2.split(img_rgb)
    r = img_rgb[:, :, 0]  # Red channel
    g = img_rgb[:, :, 1]  # Green channel
    b = img_rgb[:, :, 2]  # Blue channel
    
    print(img_rgb)
    
    print(r)
    
    print(g)
        
    # Display the original and individual RGB channels
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 4, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 4, 2)
    plt.imshow(r, cmap='Reds')
    plt.title("Red Channel")
    plt.axis('off')
    
    plt.subplot(1, 4, 3)
    plt.imshow(g, cmap='Greens')
    plt.title("Green Channel")
    plt.axis('off')
    
    plt.subplot(1, 4, 4)
    plt.imshow(b, cmap='Blues')
    plt.title("Blue Channel")
    plt.axis('off')
    
    plt.show()
    
if __name__ == '__main__':
    main()