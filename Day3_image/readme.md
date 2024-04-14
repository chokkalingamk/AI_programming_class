# Define the content of the README.md file
readme_content = """
# Image Color to Grayscale Converter

This program reads an image file, converts it to grayscale, displays both the original and the grayscale images, and saves the grayscale image as a new file.

## Getting Started

To run this program, you'll need to have Python installed on your machine. You'll also need to install the OpenCV library. You can install it using pip:

```bash
pip install opencv-python

```
The program will display the original image and its grayscale version. It will also save the grayscale image as graynew.png in the same directory.

## Example

```
import cv2

# Load the image
image = cv2.imread("/path/to/your/image.jpg")

# Convert the image to grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original', image)
cv2.imshow('Grayscale', grayImage)

# Save the grayscale image
cv2.imwrite('graynew.png', grayImage)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the shape and size of the original image
print("Original Image Shape:", image.shape)
print("Original Image Size:", image.size)

```