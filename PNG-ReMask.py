# -*- coding: utf-8 -*-
"""
Created on Sun Apr  11 .
@author: pinaxe

Renumber class to unify and then join different datasets.

"""
import cv2
from os import listdir
from os.path import isfile, join

sourceClass=33   # The class to be "renamed"
dstClass=11     # A new "name" for the class

mypath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/1/"
destpath="C:/D/notebooks/fcn-mobilenet-128/Data_zoo/camvid/2/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fi in onlyfiles :
    dst=cv2.imread(mypath+fi)
    print( fi)
    dst[dst==sourceClass]=dstClass 
    cv2.imwrite(destpath+fi,dst)