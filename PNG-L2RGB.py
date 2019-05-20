# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:24:01 2019

@author: p
"""
from PIL import Image 
from os import listdir
from os.path import isfile, join

mypath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/2/"
destpath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/3/"
#mypath="./src/"
#destpath="./dst/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fi in onlyfiles :
    frame=Image.open(mypath+fi).convert("RGB")
    print( frame.mode,fi)
    frame.save(destpath+fi)