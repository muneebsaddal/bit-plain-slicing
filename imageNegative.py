from PIL import Image
import numpy as np

#opening image
img = Image.open("lena_rgb.png")

#getting negative of image
color_val = np.array(img)
color_val = 255 - color_val
img = Image.fromarray(color_val)

#saving new image
img.save("lena_negative.png")
