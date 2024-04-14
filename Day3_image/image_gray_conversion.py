import cv2
image = cv2.imread("/Users/chokkalingamk/Downloads/ColourImage.jpg")
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






















##img = cv2.imread("novitech.png")
##print (img.shape) #(342, 548, 3)
##print (img.size)  #562248