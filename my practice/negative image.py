import cv2 
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('images/bird.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    negative_img = 255 - img  # Create the negative image by subtracting pixel values from 255
    
    # Display the original and negative images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(negative_img)
    plt.title("Negative Image")
    plt.axis('off')
    plt.show()
    

if __name__ == '__main__':
    main()