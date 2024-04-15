import cv2
img = cv2.imread('new.png')

#dst = cv2.GaussianBlur(src, (kernel),borderType)

gaussianImg = cv2.GaussianBlur(img, (71, 51), 0)

gaussianImg1 = cv2.GaussianBlur(img, (21, 21), 10)


cv2.imshow("GaussianBlur", gaussianImg)
cv2.imshow("GaussianBlur1", gaussianImg1)
		
cv2.imwrite('GaussianBlur.jpg', gaussianImg)
cv2.imwrite('GaussianBlur1.jpg', gaussianImg1)