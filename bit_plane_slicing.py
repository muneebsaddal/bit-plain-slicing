from PIL import Image
import numpy as np

#opening image
img = Image.open("lena_rgb.png").convert("L")

#function for logical and with array
def bit_plane(color_val, bit_val):
    
    return color_val & (2**bit_val)

#function to convert array to image
def img_from_array(arr):

    img = Image.fromarray(arr)
    img.show()

#image to array
color_val = np.array(img)

#calling function for bit plain slicing and converting array to img
for x in range(7):
    img_from_array(bit_plane(color_val, x))
