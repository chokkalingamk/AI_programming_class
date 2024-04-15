import cv2
image = cv2.imread("ColourImage.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', image)
cv2.imshow('Gray', grayImage)
##
cv2.imwrite('graynew.png', grayImage)
# ##
#
cv2.waitKey(10000)
cv2.destroyAllWindows()
print(image.shape)
print(image.size)
