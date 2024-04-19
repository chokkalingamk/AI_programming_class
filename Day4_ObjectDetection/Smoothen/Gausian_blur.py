import cv2
import imutils

org_image=cv2.imread("OriginalImg.png")



img_input=imutils.resize(org_image,width=200)


#Inputs:
# img     = RGB or grayscale image data
# ksize   = Tuple of kernel dimensions, e.g. (5, 5)
# sigmax  = standard deviation in X direction; if 0, calculated from kernel size
# sigmay  = standard deviation in Y direction; if sigmaY is None, sigmaY is taken to equal sigmaX

Blurred_image=cv2.GaussianBlur(img_input,(25,25),0)

Blurred_image1=cv2.GaussianBlur(img_input,(51,51),0)

Blurred_image2=cv2.GaussianBlur(img_input,(81,81),0)

Blurred_image3=cv2.GaussianBlur(img_input,(91,91),0)

cv2.imshow("Original",org_image)
cv2.imshow("BlurredShivan1",Blurred_image)
cv2.imshow("BlurredShivan2",Blurred_image1)
cv2.imshow("BlurredShivan3",Blurred_image2)
cv2.imshow("BlurredShivan4",Blurred_image3)
cv2.imwrite("BlurredIMAGE.jpg",Blurred_image)

cv2.waitKey(100000)
cv2.destroyAllWindows()