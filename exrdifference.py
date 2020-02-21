from PIL import Image
import array
import sys
import optparse

from core.exr import ExrImage, MaskImage
from core.error import mse, rms, absdiff
from core.diff import diffimage


def main(exrfile1, exrfile2, maskimg=None, output="diff_img.png"):
    imgExr1 = ExrImage(exrfile1)
    imgExr2 = ExrImage(exrfile2)
    
    mask = MaskImage(maskimg).mask if maskimg is not None else None

    print("rms : " + str(rms(imgExr1, imgExr2, mask)))  

    imgdiff = diffimage(imgExr1, imgExr2, mask)
    
    imgdiff.save("difference.png")

if __name__ == "__main__":
   
    parser = optparse.OptionParser()
    parser.add_option('-i','--input1', help="Exr image 1")
    parser.add_option('-j','--input2', help="Exr image 2")
    parser.add_option('-m','--mask', help="Mask Image")
    parser.add_option('-o','--output', help="Output Image")
    (opts,args) = parser.parse_args()

    exr1 = opts.input1
    exr2 = opts.input2
    maskFile = opts.mask
    outputfile = "diff_img.png" if opts.output is None else opts.output 
    
    main(exr1, exr2, maskimg=maskFile, output=outputfile)
    