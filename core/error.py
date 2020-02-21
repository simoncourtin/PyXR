import math
import array

def mse(img1, img2, mask=None):
    
    luminance1 = img1.computeLuminance()
    luminance2 = img2.computeLuminance() 
    
    if mask == None:
        mask = array.array('I', [1 for i in range(len(luminance1))])

    sum_mse = 0.0
    elements = 0

    for i in range(len(luminance1)):
        if mask[i] == 1:
            lum_ref = luminance1[i]
            lum_error = luminance2[i]
            sum_mse += (lum_ref - lum_error) * (lum_ref - lum_error)
            elements += 1
    
    
    if elements > 0:
        mse = sum_mse / float(elements)
    else:
         mse = 0.0
    
    return mse 

def rms(img1, img2, mask=None):
    return math.sqrt(mse(img1, img2, mask))

def absdiff(value1, value2):
    return abs(value2 - value1)