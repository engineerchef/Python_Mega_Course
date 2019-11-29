import numpy
import cv2

# n = numpy.arange(27)
# print(n)
# print(n.reshape(3, 3, 3))
# m = numpy.asarray([[123, 23, 123, 12, 33], [], []])
# print(m)

im_g = cv2.imread("smallgray.png", 0)
# print(im_g)

im_c = cv2.imread("1.jpg", 5)
# cv2.imwrite("new.jpg", im_c)
# print(im_c)

# print(im_g[0:2,2:4])

# Dizinin normal hali
# for i in im_g:
#     print(i)

# Dizinin transpozesi
# for i in im_g.T:
#     print(i)

# Dizideki tüm değerleri teker teker yaazar
# for i in im_g.flat:
#     print(i)

# Yatay olarak birleştirir
imh = numpy.hstack((im_g, im_g, im_g))
imh_file = cv2.imwrite("horizontal_file.png", imh)
print(imh)

# Dikey olarak birleştirir
imv = numpy.vstack((im_g, im_g, im_g))
imv_file = cv2.imwrite("vertical_file.png", imv)
print(imv)
