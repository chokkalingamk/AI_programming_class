import cv2
import imutils

# Load an image
image = cv2.imread('ColourImage.jpg')

# Resize using imutils.resize
resized_imutils = imutils.resize(image, width=200)

# Resize using cv2.resize
resized_cv2 = cv2.resize(image, (200, 200))

cv2.imshow('imutils.resize', resized_imutils)
cv2.imshow('cv2.resize', resized_cv2)
cv2.waitKey(100000)
cv2.destroyAllWindows()
