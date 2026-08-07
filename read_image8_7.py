# import cv2 as cv
# img = cv.imread("images/cat.jpg")
# rotate = cv.flip(img, 1)
# cv.imshow("Cat", img)
# cv.imshow("Rotated", rotate)
# # cv.imshow("Rotated", rotate)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv2.line()
# cv2.rectangle()
# cv2.circle()
# cv2.putText()
import cv2
import numpy as np

image = cv2.imread("images/cat.jpg")

height, width = image.shape[:2]

matrix = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#to convert the image to gray scale we use cvtColor and then we have to specify the color space we want to convert to in this case we want to convert to gray scale so we use cv2.COLOR_BGR2GRAY

blurred = cv2.GaussianBlur(gray, (5, 5), 0)#to blur the image we use GaussianBlur and then we have to specify the kernel size in this case we use (5, 5) and then we have to specify the standard deviation in this case we use 0

edges = cv2.Canny(blurred, 100, 200)#to detect edges in the image we use Canny and then we have to specify the threshold values in this case we use 100 and 200
rectangle = cv2.rectangle(image.copy(), (50, 50), (200, 200), (0, 255, 0), 2)#in shape lke circle rectangle and line we have to go image.cop() otherwise it will change the original image and we will not be able to see the original image in the end
translated = cv2.warpAffine(image, matrix, (width, height))
blurr = cv2.GaussianBlur(image, (3, 3), 0)#kernel must be odd number 
cv2.imshow("Original", image)
cv2.imshow("rectangle", rectangle)
cv2.imshow("blurred", blurr)
cv2.imshow("Gray", gray)
cv2.imshow("Blurred", blurred)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(edges.dtype)
print(edges.min())
print(edges.max())