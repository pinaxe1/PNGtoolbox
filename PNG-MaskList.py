# -*- coding: utf-8 -*-
"""
Created on Sun Apr  11 .
@author: pinaxe

List masks with image mode name and classes present on each mask image.

"""
import numpy
from PIL import Image 
from os import listdir
from os.path import isfile, join


mypath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/1/"
#mypath="src/"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fi in onlyfiles :
    dst=Image.open(mypath+fi)
    
    dst1 = numpy.array(dst).flatten().tolist()
    dstClass=set(dst1)
    print(dst.mode, fi, dstClass)