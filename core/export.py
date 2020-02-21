import array
from PIL import Image

from core.utils import encodeToSRGB

def exportToImage(img, filename, extention):
    red = array.array('f', [encodeToSRGB(e) for e in img.red])
    green = array.array('f', [encodeToSRGB(e) for e in img.green])
    blue = array.array('f', [encodeToSRGB(e) for e in img.blue])
    
    rgbf = [Image.frombytes("F", img.size, red.tostring())]
    rgbf.append(Image.frombytes("F", img.size, green.tostring()))
    rgbf.append(Image.frombytes("F", img.size, blue.tostring()))
    
    rgb8 = [im.convert("L") for im in rgbf]
    Image.merge("RGB", rgb8).save(filename, extention, quality=95)


def expotToPng(img, filename):
    exportToImage(img, filename, "PNG")

def expotToJpg(img, filename):
    exportToImage(img, filename, "JPG")