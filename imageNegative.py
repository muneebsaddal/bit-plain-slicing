from PIL import Image

img = Image.open("lena_color.gif").convert("RGB").save("lena_rgb.png")

#Converting to Negative -- for RBG image
img_file = Image.open("lena_rgb.png")
img = img_file.load()
width, height = img_file.size

for x in range(width):
    for y in range(height):
        [r, g, b] = img[x, y]
        sr = 255 - r
        sg = 255 - g
        sb = 255 - b
        img[x, y] = (sr, sg, sb)
img_file.save("lena_negative.png")

#Converting to Negative -- for grayscale image
img_file = Image.open("lena_rgb.png").convert('L')
img = img_file.load()
width, height = img_file.size

for x in range(width):
    for y in range(height):
        gray_val = img[x, y]
        new_val = 255 - gray_val
        img[x, y] = new_val
img_file.save("lena_grayscale_negative.png")


#Converting to Negative -- for binarized image
img_file = Image.open("lena_rgb.png").convert('L').point((lambda x : 255 if x > 150 else 0), mode = '1')
img = img_file.load()
width, height = img_file.size

for x in range(width):
    for y in range(height):
        bi_val = img[x, y]
        new_bi_val = 255 - bi_val
        img[x, y] = new_bi_val
img_file.save("lena_binarized_negative.png")