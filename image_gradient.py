from PIL import Image

img_file = Image.open('lena_rgb.png').convert('L')
img = img_file.load()
row, col = img_file.size

for x in range(row-1):
    for y in range(col):
        gradient = img[x, y] - img[x+1, y]
        img[x, y] = gradient
img_file.save("lena_gradient.png")