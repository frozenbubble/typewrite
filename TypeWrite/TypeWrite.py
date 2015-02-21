#import clr
#clr.AddReference("System.Drawing")
import sys
import System.Drawing as drawing

path = sys.argv[1]

shades = {' ', '¨', '`', '.', ',', '-', '^', '/' '(', 'u', 'w', 'g', 'W', '%', '&', '#'}


print('Hello world')

def get_intensity(r, g, b):
    return int((r + g + b) / 48)

def get_rgb(img):
    return 0