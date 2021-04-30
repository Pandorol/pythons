# -*- coding: UTF-8 -*-
"""
Created on Fri Apr 30 07:47:06 2021

@author: Pandora ELF
"""
import os
import cv2
path = "D:/eclipse-workspace/v3/public/videos" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        s.append(file)
        vidcap = cv2.VideoCapture(path+"/"+file)
        success,image = vidcap.read()
        #imag = cv2.imwrite("D:/eclipse-workspace/v3/public/1.jpg",image)
        
        #imag = cv2.imwrite(str1,image)
        
        img_write = cv2.imencode(".jpg",image)[1].tofile(file[0:-4]+".jpg")
