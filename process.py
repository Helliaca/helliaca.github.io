import cv2
import numpy
import math

img = cv2.imread("sample.png")

# create an alpha channel
img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

pi = 3.1415926535
img_size = img.shape
max_x = img_size[0]-1
max_y = img_size[1]-1
low_x = max_x - (math.tan(31 * pi / 180)*max_y)
low_x = int(low_x)
triangle = numpy.array([[max_x, 0], [max_x, max_y], [low_x, max_y]])
color = [255, 255, 255, 0] #white
cv2.fillConvexPoly(img, triangle, color)

img = cv2.GaussianBlur(img, (21, 21), 20, 20)
# img = cv2.GaussianBlur(img, (21, 21), 20)
#img = cv2.GaussianBlur(img, (21, 21), 20)
#img = cv2.GaussianBlur(img, (21, 21), 20)
#img = cv2.GaussianBlur(img, (21, 21), 20)
# img = cv2.blur(img, (29,29))


cv2.imwrite("with_triangle.png", img)
