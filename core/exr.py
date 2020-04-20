import OpenEXR
import array
import Imath
from PIL import Image

from core.utils import encodeRelativeLuminance

class PyXrImage:
    
    blue = array.array('f', [])
    red = array.array('f', [])
    green = array.array('f', [])
    
    width = 0
    height = 0
    size = (width , height)
    
    def __init__(self, f):
        self.file = Image.open(f)
        self.width, self.height = self.file.size
        self.size = (self.width , self.height)

    def getpixel(x,y):
        i = y * self.width + x
        return [self.red[i], self.green[i], self.blue[i]]    
        
    def computeLuminance(self):
        luminance = array.array('f', [])
        for i in range(len(self.red)):
            luminance.append(encodeRelativeLuminance(self.red[i], self.green[i], self.blue[i]))

        return luminance

class MaskImage(PyXrImage):
    def __init__(self, f):
        self.file = Image.open(f)
        self.width, self.height = self.file.size
        self.size = (self.width , self.height)

        self.mask = array.array('I', [])

        lum_img = self.file.convert('L')        
        
        for y in range(self.height):
            for x in range(self.width):
                l = lum_img.getpixel((x,y))
                self.mask.append(1 if l > 0 else 0)


class ExrImage(PyXrImage):
    def __init__(self, f):
        self.file = OpenEXR.InputFile(f)
        pixelType = Imath.PixelType(Imath.PixelType.FLOAT)
        
        dw = self.file.header()['dataWindow']
        self.width = dw.max.x - dw.min.x + 1
        self.height = dw.max.y - dw.min.y + 1
        self.size = (self.width , self.height)

        redStr = self.file.channel('R', pixelType)
        greenStr = self.file.channel('G', pixelType)
        blueStr = self.file.channel('B', pixelType)

        self.blue = array.array('f', blueStr)
        self.red = array.array('f', redStr)
        self.green = array.array('f', greenStr)
    
    