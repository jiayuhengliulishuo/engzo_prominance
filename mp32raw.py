# encoding=utf-8
import os
import csv
import sys
#这段程序的目标是把mp3文件转换成raw格式的文件
rootdir='./mp3'
FileList=[]
for root,SubFloders,files in os.walk(rootdir):
	for f in files:
		if f.find('mp3')!=-1:
			FileList.append(os.path.join(root,f))
			print(os.path.join(root,f))
#print(FileList)
for item in FileList:
	#print(type(item))
	#print len(item)
	str='ffmpeg -i '+item+' -ar 16000 -ac 1 -f s16le ./raw/'+item[6:30]+'.raw'
	os.system(str)
print(os.getcwd())
