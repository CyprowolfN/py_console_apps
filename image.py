import cv2
import sys

image = cv2.imread("Guildwars2.jpg")
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GREY)
greyImageInv = 255 - grayImage
greyImageInv = cv2.GaussianBlur(greyImageInv, (21,21), 0)
output = cv2.divide(grayImage, 255-greyImageInv, scale=256.0)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("image", image)
cv2.imshow("pencilsketch", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
