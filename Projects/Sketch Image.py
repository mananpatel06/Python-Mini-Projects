import cv2
img = cv2.imread("1.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertBlure = cv2.bitwise_not(blur)
sketch = cv2.divide(gray,invertBlure,scale=256.0)

# cv2.imshow("gray",gray)
# cv2.imshow("invert",invert)
# cv2.imshow("invertBlure",invertBlure)
cv2.imshow("Sketch",sketch)

cv2.waitKey(0)