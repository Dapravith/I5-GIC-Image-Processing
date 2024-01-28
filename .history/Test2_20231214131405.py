import cv2 as cv
import numpy as np

def convert_to_grayscale(image_path):
    # Read the image
    img = cv.imread(image_path)

    # Check if the image is loaded successfully
    if img is None:
        print("Error: Unable to load the image.")
        return

    # Get the height and width of the image
    height, width = img.shape[:2]

    # Create a new image with the same size as the original
    grayscale_img = np.zeros((height, width), dtype=np.uint8)

    # Convert each pixel to grayscale using the formula: 0.299*R + 0.587*G + 0.114*B
    for h in range(height):
        for w in range(width):
            R = img[h, w, 0]
            G = img[h, w, 1]
            B = img[h, w, 2]
            grayscale_img[h, w] = int(0.299 * R + 0.587 * G + 0.114 * B)

    return grayscale_img

def main():
    image_path = './images/Test1.jpg'
    grayscale_img = convert_to_grayscale(image_path)

    # Display the original and grayscale images
    cv.imshow('Original Image', cv.imread(image_path))
    cv.imshow('Grayscale Image', grayscale_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
