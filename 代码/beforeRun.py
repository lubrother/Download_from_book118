# -*- coding: UTF-8 -*-

#运行正式程序run之前跑该程序，获取int(x[21:-4])中的21在当前文件应该为何值
#该程序是将book118获取的图片排序输出，获取适当值将img中的程序改成适当值

import os
path ='./图片/'#当前目录
filenames=os.listdir(path)
filenames.sort(key=lambda x:int(x[21:-4]))

for filename in filenames:
	print(os.path.join(path,filename))
print(filenames[1])
print(filenames[3])
print(type(filenames))
