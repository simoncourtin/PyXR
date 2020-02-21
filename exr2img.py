import sys
import optparse

from core.exr import ExrImage
from core.export import expotToPng, expotToJpg


def main(exrfile, imgfile, ext):
    imgExr1 = ExrImage(exrfile)
    if ext == "PNG":
        expotToPng(imgExr1,imgfile)
    
    if ext == "JPG":
        expotToPng(imgExr1,imgfile)
    
if __name__ == "__main__":

    parser = optparse.OptionParser()
    parser.add_option('-i','--input', help="Imput Exr image 1")
    parser.add_option('-o','--output', help="Output image")
    parser.add_option('-f','--format', help="Output format : PNG | JPG", default="PNG")
    (opts,args) = parser.parse_args()

    exrinput = opts.input
    imgoutput = opts.output
    outputformat = opts.format

    main(exrinput, imgoutput, outputformat)