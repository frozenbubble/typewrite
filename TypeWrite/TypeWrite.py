from math import ceil, ceil
from PIL import Image
import urllib3 as urllib
import os.path
import sys
import re
import io


shades = ['_', '-', '^', '/', '(', 'u', 'w', 'g', 'W', '%', '&', '#']
chars = 100

if (len(sys.argv) != 2):
    print('Usage: typewrite <filename | url>')
    exit()

arg = sys.argv[1]

if (os.path.isfile(arg)):
    im = Image.open(arg)

else:
    http = urllib.PoolManager()
    r = http.request('GET', arg)
    im = Image.open(io.BytesIO(r.data))
    

w,h = im.size
im.thumbnail((chars, int(h/(w/chars))))
w,h = im.size
im = im.resize((w, int(h/2)))
w,h = im.size

typed = [['0' for x in range(w)] for y in range(h)]

for i, p in enumerate(im.im):
    brightness = p[0] + p[1] + p[2]
    shade = shades[int((brightness*12)/768) - 1]

    x = int(i/w)
    y = i - int(i/w)*w

    typed[x][y] = shade

for row in typed:
    r = "".join(row)

    print(r)