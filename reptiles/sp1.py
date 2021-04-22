# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:30:20 2021

@author: Pandora ELF
"""

  
import requests
import re

f=open('fulidatas.txt','a')
num=21000

while num<21042:
    val1 = "https://kaijiang.500.com/shtml/ssq/"
    num=num+1
    val2 = ".shtml"
    url = val1+"%05d" %num+val2
    #print(url)
    response = requests.get(url)  # 请求网站
    #print(response) 
    #print(response.text)
    datas_1 = re.findall('<li class="ball_red">(.*?)</li>', response.text)
    datas_2 = re.findall('<li class="ball_blue">(.*?)</li>', response.text)
    #print(datas_1)
    #print(datas_2)
    f.write("%05d " %num)
    for data in datas_1:
        f.write(str(data)+' ')
    for data in datas_2:
        f.write(str(data)+'\n')


f.close()
