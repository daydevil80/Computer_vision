'''
import cv2
image=cv2.imread('images/cat.jpg')
print(image.shape)
print(image)
print(image.dtype)
print(image.size)
print(image[100,100])
print(image.ndim)
print(image[100:200])
cv2.imshow('cat',image)
small = cv2.resize(image, (600, 800))

cv2.imshow("Cat", small)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
'''
import cv2

image = cv2.imread("images/cat.jpg")

blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()
print(image.shape)

print(blue.shape)

print(green.shape)

print(red.shape)
'''
import cv2

image = cv2.imread("images/cat.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image.shape)
print(gray.shape)

cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()