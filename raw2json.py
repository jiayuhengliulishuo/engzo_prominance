#encoding=utf-8
#利用字典和语音模型来训练json特征文件
import os
import sys
import csv
csv_name='filename_trans.csv'
def csv2list(filename):
	listout=[]
	with open(filename) as f:
		reader=csv.reader(f)
		for row in reader:
			listout.append(row)
	return listout
listout=csv2list(csv_name)
#for 
#print(listout[0:10])
print(len(listout))
iter=0
for item in listout:
	iter+=1
	juzi=item[1]
	wenjianming=item[0]
	#print(juzi)
	#print(wenjianming[4:28])
	if iter>=0:
	#	print(juzi)
		#print(juzi)
		#print("juzi")
		cmd='/home/yxf/engzo-scorer/src/programs/engzo_input_generator --trans \"'+ juzi+'\" --dict cmu07_20140625.sdic --raw raw/'+wenjianming[4:28]+'.raw --am /data/yxf/ACMOD/voxpop_all.cd_semi_6000/ --out out/'+wenjianming[4:28]+'.out --json jsonNEW/'+wenjianming[4:28]+'.json'
		#print(cmd)
		os.system(cmd)

#/home/yxf/engzo-scorer/src/programs/engzo_input_generator --trans "i bet your parents will love that" --dict cmu07_20130715.sdic --raw raw/51dd47e7fcfff201870011c8.raw --am /data/yxf/ACMOD/voxpop_all.cd_semi_6000/ --out testl.out --json testl.json
