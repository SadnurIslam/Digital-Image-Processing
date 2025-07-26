import cv2 
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('images/bird.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    mask = 300
    
    masked_img = img.copy()  # Create a copy of the original image for masking
    
    img[:mask, :mask] = 0  # Masking the top-left area of the image
    
    # Display the original and negative images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(masked_img)
    plt.title("Negative Image")
    plt.axis('off')
    plt.show()
    

if __name__ == '__main__':
    main()