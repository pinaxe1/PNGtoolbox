# -*- coding: utf-8 -*-
"""
Created on Sun Apr  11 .
@author: pinaxe

List masks with image mode name and classes present on each mask image.
List only images with unusual masks
Allowed Masks are
0  - Unlabeled          - Unlabeled
33 - Pine Leaf          - Bicycle
21 - Vegetation         - Vegetation 
7  - Desk or concrete   - Road
27 - Soil               - Ground
6  - Any solid thing    - Truck 
"""
import numpy
from PIL import Image 
from os import listdir
from os.path import isfile, join

ExpectedLClasses={0, 33, 6, 7, 27, 21}
mypath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/3/"
#mypath="src/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fi in onlyfiles :
    img=Image.open(mypath+fi)
    allClasses = numpy.array(img).flatten().tolist()
    unicClasses=set(allClasses)
    for classi in unicClasses:
        if classi not in ExpectedLClasses:
            print(img.mode, fi, unicClasses)