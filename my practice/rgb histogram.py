import cv2 
import matplotlib.pyplot as plt
import numpy as np

def histogram(r):
    hist = np.zeros(256,dtype=int)  # Initialize histogram array for 256 intensity levels
    row, col = r.shape  # Get the dimensions of the red channel image
    for i in range(row):
        for j in range(col):
            intensity = r[i, j]  # Get the intensity value of the pixel
            hist[intensity] += 1  # Increment the count for this intensity level
            
    return hist  # Return the histogram array
    

def main():
    img = cv2.imread('images/bird.jpg')  # Load the image from the specified path
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for correct color display
    
    # Split the image into its RGB channels
    # r, g, b = cv2.split(img_rgb)
    r = img_rgb[:, :, 0]  # Red channel
    g = img_rgb[:, :, 1]  # Green channel
    b = img_rgb[:, :, 2]  # Blue channel
    
    red_hist = histogram(r)
    
    green_hist = histogram(g)
    
    blue_hist = histogram(b)
    
    # Display the original image and its RGB channels
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.plot(red_hist, color='red')
    plt.title("Red Channel Histogram")
    plt.xlim([0, 255])
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.grid()
    plt.axis('on')
    
    plt.subplot(2, 2, 3)
    plt.plot(green_hist, color='green')
    plt.title("Green Channel Histogram")
    # plt.xlim([0, 255])
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.grid()
    plt.axis('on')
    
    plt.subplot(2, 2, 4)
    plt.plot(blue_hist, color='blue')
    plt.title("Blue Channel Histogram")
    plt.xlim([0, 255])
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.grid()
    
    plt.show()
    
if __name__ == '__main__':
    main()