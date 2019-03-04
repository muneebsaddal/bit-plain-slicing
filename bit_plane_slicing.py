import cv2
import numpy as np

img = cv2.imread("dollar.png", cv2.IMREAD_GRAYSCALE)
row, col = img.shape

#convert each pixel value to bit pixel value
img_1D = []
for x in range(row):
    for y in range(col):
        img_1D.append(np.binary_repr(img[x][y], width=8))

img_2D = np.reshape(img_1D, (row, col))

eight_bit_plane = [int(i[0]) for i in img_1D]
eight_bit = np.array(eight_bit_plane) * 128
eight_bit = np.reshape(eight_bit,(row,col))
cv2.imwrite("8bit_img.png", eight_bit)

seven_bit_plane = [int(i[1]) for i in img_1D]
seven_bit = np.array(seven_bit_plane) * 64
seven_bit = np.reshape(seven_bit,(row,col))
cv2.imwrite("7bit_img.png", seven_bit)

six_bit_plane = [int(i[2]) for i in img_1D]
six_bit = np.array(six_bit_plane) * 32
six_bit = np.reshape(six_bit,(row,col))
cv2.imwrite("6bit_img.png", six_bit)

five_bit_plane = [int(i[3]) for i in img_1D]
five_bit = np.array(five_bit_plane) * 16
five_bit = np.reshape(five_bit,(row,col))
cv2.imwrite("5bit_img.png", five_bit)

four_bit_plane = [int(i[4]) for i in img_1D]
four_bit = np.array(four_bit_plane) * 8
four_bit = np.reshape(four_bit,(row,col))
cv2.imwrite("4bit_img.png", four_bit)

three_bit_plane = [int(i[5]) for i in img_1D]
three_bit = np.array(three_bit_plane) * 4
three_bit = np.reshape(three_bit,(row,col))
cv2.imwrite("3bit_img.png", three_bit)

two_bit_plane = [int(i[6]) for i in img_1D]
two_bit = np.array(two_bit_plane) * 2
two_bit = np.reshape(two_bit,(row,col))
cv2.imwrite("2bit_img.png", two_bit)

one_bit_plane = [int(i[7]) for i in img_1D]
one_bit = np.array(one_bit_plane) * 1
one_bit = np.reshape(one_bit,(row,col))
cv2.imwrite("1bit_img.png",one_bit)


