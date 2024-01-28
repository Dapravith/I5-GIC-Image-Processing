# import cv2 as cv

# img = cv.imread('./images/Test1.jpg')
# width, height = img.shape[:2]

# mirrorImg1 = mirrorImg2 = mirrorImg3 = img.copy()

# def mirror_ImgF1(img):
#     for h in range (height):
#         for w in range (width):
#             mirrorImg1[h,w] = img[1-h, w]
#             return mirrorImg1
        
# def mirror_ImgF2(img):
#     for h in range (height):
#         for w in range (width):
#             mirrorImg2[h,w] = img[h, 1-w]
#             return mirrorImg2

# def mirror_ImgF3(img):
#     for h in range (height):
#         for w in range (width):
#             mirrorImg3[h,w] = img[1-h, 1-w]
#             return mirrorImg3


# cv.imshow('Test2', mirror_ImgF1(img))

# cv.imshow('Test3', mirror_ImgF2(img))

# cv.imshow('Test4', mirror_ImgF3(img))

# cv.waitKey(0)
# cv.destroyAllWindows()
import cv2 as cv

def mirror_color_image_cv(input_path, output_path):
    # Read the image using OpenCV
    original_image = cv.imread(input_path)

    # Get the height and width of the image
    height, width, _ = original_image.shape

    # Create an empty image with the same dimensions
    mirrored_image = original_image.copy()

    # Iterate through each pixel and mirror the color
    for x in range(width):
        for y in range(height):
            # Get the color of the current pixel
            pixel_color = original_image[y, x].copy()

            # Calculate the mirrored x-coordinate
            mirrored_x = width - 1 - x

            # Set the mirrored pixel color in the new image
            mirrored_image[y, mirrored_x] = pixel_color

    # Save the mirrored image
    cv.imwrite(output_path, mirrored_image)

# Example usage:
input_image_path = './images/facetree.jpg'
output_image_path = './images//facetree.jpg'
mirror_color_image_cv(input_image_path, output_image_path)
