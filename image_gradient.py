from PIL import Image

img_file = Image.open('lena_rgb.png').convert('L')
img = img_file.load()
width, height = img_file.size

for x in range(width-1):
    for y in range(height):
        gradient = img[x, y] - img[x+1, y]
        img[x, y] = gradient
img_file.save("lena_gradient.png")