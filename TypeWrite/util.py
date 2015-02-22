import clr
clr.AddReference('Typewrite')


def get_intensity(r, g, b):
    return int((r + g + b) / 48)

def get_rgb(img):
    return 0