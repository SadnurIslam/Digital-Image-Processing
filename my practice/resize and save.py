import cv2
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('images/bird.jpg')  # Load the image from the specified path
    
    # Resize the image to 300x300 pixels
    resized_img = cv2.resize(img, (1000, 1000))
    
    # Save the resized image to a new file
    cv2.imwrite('images/bird_resized.jpg', resized_img)
    
    # Display the original and resized images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))
    plt.title("Resized Image")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()