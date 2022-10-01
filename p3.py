import cv2
img = cv2.imread("k.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("this is gray image!",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()