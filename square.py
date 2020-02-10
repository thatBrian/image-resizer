import sys
from PIL import Image
import math

try:
    filename = sys.argv[1]
except:
    print("Please enter a file name")
    sys.exit()
im = Image.open(filename)
try:
    im = Image.open(filename)
except:
    print("Can't find file or wrong format")
    sys.exit()
name,ext = filename.split(".")
width,height = im.size

if(width>height):
    start = math.floor((width-height)/2)
    im.crop((start,0,start+height,height)).save(name + "_cropped." + ext,)
else:
    start = math.floor((height-width)/2)
    im.crop((0,start,width,start+width)).save(name + "_cropped." + ext,)
