from PIL import Image
import array
import numpy as np

from core.exr import ExrImage, MaskImage
from core.error import mse, rms, absdiff
from core.utils import minmax


def diffluminance(img1, img2, minimum=0.0, maximum=float("inf"), mask=None):
    
    luminance1 = img1.computeLuminance()
    luminance2 = img2.computeLuminance() 
    differences_lum = array.array('f', [])
    _min = 0.0
    _max = 0.07
    
    if mask == None:
        mask = array.array('I', [1 for i in range(len(luminance1))])

    for i in range(len(luminance1)):
        if mask[i] == 1 and luminance1[i] != 0.0:
            differences_lum.append(minmax(minimum, maximum, absdiff(luminance1[i], luminance2[i])))
        else:
            differences_lum.append(0.0)
    
    return differences_lum, differences_lum, differences_lum


def diffcolor(img1, img2, minimum=0.0, maximum=float("inf"), mask=None):
    
    differences_r = array.array('f', [])
    differences_g = array.array('f', [])
    differences_b = array.array('f', [])
    
    if mask == None:
        mask = array.array('I', [1 for i in range(len(img1.red))])

    for i in range(len(img1.red)):
        if mask[i] == 1:
            differences_r.append(minmax(minimum, maximum, absdiff(img1.red[i], img2.red[i])))
            differences_g.append(minmax(minimum, maximum, absdiff(img1.green[i], img2.green[i])))
            differences_b.append(minmax(minimum, maximum, absdiff(img1.blue[i], img2.blue[i])))
        else:
            differences_r.append(0.0)
            differences_g.append(0.0)
            differences_b.append(0.0)
    
    return differences_r, differences_g, differences_b

def diffimage(exr1, exr2, mask, minimum=0.0, maximum=float("inf"), method="luminance"):
    
    if method == "color":
        r, g, b = diffcolor(exr1, exr2, minimum=minimum, maximum=maximum, mask=mask)
    else :
        r, g, b = diffluminance(exr1, exr2, minimum=minimum, maximum=maximum, mask=mask)

    r_data = array.array('f', [l * 255.0 for l in r])
    g_data = array.array('f', [l * 255.0 for l in g])
    b_data = array.array('f', [l * 255.0 for l in b])

    r_data = Image.frombytes("F", exr1.size, r_data.tostring())
    g_data = Image.frombytes("F", exr1.size, g_data.tostring())
    b_data = Image.frombytes("F", exr1.size, b_data.tostring())
    
    data = [r_data, g_data, b_data]

    imgdiff = Image.new("RGB", exr1.size)
    imgdiff = Image.merge("RGB", [im.convert("L") for im in data])
    
    return imgdiff
