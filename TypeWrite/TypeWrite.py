from __future__ import print_function
from PIL import Image

shades = {' ', '\'', '`', '.', ',', '-', '^', '/' '(', 'u', 'w', 'g', 'W', '%', '&', '#'}

print('Hello World')
im = Image.open("C:/Users/Peter/Pictures/Backgrounds Wallpapers HD/16699.jpg")
pixels = im.load();
print(im.format, im.size, im.mode)

for p in im.im:
    print(p)
