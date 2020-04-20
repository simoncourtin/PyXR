# PyXR

PyXR is a tool for EXR images in python :
- Load EXR image
- Export EXR image to PNG and JPG format
- Compute error between 2 EXR image :
  - Mean square error (mse)
  - Root mean square error (rmse)
- Make Diference image with 2 EXR :
  - Absolute diference
  - Diference on luminance
  - Diference on color
- Load Mask png image for error and diference image


## Installation 

### Prerequisites

PyXR need Python version 3.5 or later.

Install OpenEXR tool for python to read and manipulate EXR files ([install](https://pypi.org/project/OpenEXR/)):

> pip install OpenEXR

For other Image formats, install Pillow lib ([install](https://pillow.readthedocs.io/en/stable/installation.html)) :

> python3 -m pip install --upgrade pip
> python3 -m pip install --upgrade Pillow

Clone PyXR reporitory :

> git clone https://github.com/simoncourtin/PyXR.git

Run one of the scripts at the root of the directory.