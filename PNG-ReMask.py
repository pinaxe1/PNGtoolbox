# -*- coding: utf-8 -*-
"""
Created on Sun Apr  11 .
@author: pinaxe

Renumber classes to unify and then join different datasets.

"""
import cv2
from os import listdir
from os.path import isfile, join

"""List masks with image mode name and classes present on each mask image.
List only images with unusual masks
Allowed Masks are
0  - Unlabeled          - Unlabeled
33 - Pine Leaf          - Bicycle
21 - Vegetation         - Vegetation 
7  - Desk or concrete   - Road
27 - Soil               - Ground
6  - Any solid thing    - Truck 
"""
ExpectedLClasses={0, 33, 6, 7, 27, 21} # Classes I currently use in the dataset for FCN-128 

sourceList={33, 27, 21}# Classes to be "renamed" so they wouldn't exceed NUmClasses in my FCN-128 
dstList={8,9,10}       # A new "names" for the classes

mypath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/1/"
destpath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/3/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fi in onlyfiles :
    dst=cv2.imread(mypath+fi) # CV2.read  always converts image to RGB.
    print('RGB', fi) # CV2 wouldn't maintain source image mode. It always converts to RGB.
    for sourceClass, dstClass in zip(sourceList, dstList) : 
        dst[dst==sourceClass]=dstClass 
    cv2.imwrite(destpath+fi,dst)