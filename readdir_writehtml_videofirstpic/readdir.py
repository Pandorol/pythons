# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:44:01 2021

@author: Pandora ELF
"""

import os
path = "D:/eclipse-workspace/v3/public/videopics" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        s.append(file)
html =""
#print(s[0])
#html+="<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>KuBrain_video</title>\n</head>\n<style> \n li{ display:inline} \n.div-a{ float:top;width:220px;} \n.div-b{ float:down;width:220px;} \n.div-c{float:left;width:220px;}\n.div-d{float:left;width:20px;}\n<//style>\n<body>\n<ul >\n		<li ><a href="index.html">首页<//a><//li>\n		<li ><a href="index.html">视频<//a><//li>\n		<li ><a href="_blank">数据集<//a><//li>\n		<li ><a href="_blank">XXX<//a><//li>\n		<li ><a href="_blank">XXX<//a><//li>\n		<//ul>\n								\n<div class="div-c">\n<div class="div-a">"
html+="""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>KuBrain_video</title>
</head>

<style> 
li{ display:inline} 
.div-a{ float:top;width:220px;} 

.div-b{ float:down;width:220px;} 
.div-c{float:left;width:220px;}
.div-d{float:left;width:20px;}
</style>

<body>

<ul >
		<li ><a href="index.html">首页</a></li>
		<li ><a href="index.html">视频</a></li>
		<li ><a href="_blank">数据集</a></li>
		<li ><a href="_blank">XXX</a></li>
		<li ><a href="_blank">XXX</a></li>
		</ul>

		
			
			
"""
for file in s:
    html+="""
    <div class="div-c">
    <div class="div-a">
    <a href="vdemo2.html?video_src=videos/"""
    html+=file[0:-3]+"mp4";
    html+="""">
    <img id="video"  src="videopics/"""
    html+=file;
    html+="""" width=220px /> 
    </a>
    </div>
    <div class="div-b">"""
    html+=file[0:-4];
    html+="""</div>
    </div>
    <div class="div-d">
    &nbsp
    </div>"""
    
html+="""</body>

</html>"""
f=open('index.html','w',encoding='utf-8')
f.write(html)
f.close()
print(html)