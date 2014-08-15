#encoding=utf-8
import sys
import os
import csv 
import pickle
import numpy
def csv2list(filename): #csv文件转换成list数据
	listout=[]
	with open(filename) as f:
		reader=csv.reader(f)
		for row in reader:
			listout.append(row)
	return listout
pkl_file=file('./Label.pkl','rb')#打开类标文件
LabelRaw=pickle.load(pkl_file)
print len(LabelRaw)
#for item in LabelRaw:
#	print len(item)
#	for item1 in item:
#		print len(item1)
csvFile=csv2list('filename_trans.csv')
wenjianming=[]#所有文件
juzi=[]#内容
for item in csvFile:
	wenjianming.append(item[0])
	juzi.append(item[1])
#print wenjianming
# 6701改错
LabelRaw[13][200][1]='mp3/510d38d4fcfff2fc6d000543.mp3'
matchCount=0
erroriter=0
for item in LabelRaw:
	iter=0
	for item1 in item:
		erroriter+=1
		iter+=1
		if iter%2 != 0:
			#print item1[1]
			specalCount=0
			for item2 in wenjianming:
				specalCount+=1
				if item1[1]==item2:
					matchCount+=1
					break
				if specalCount>=5000:
					print item1[1]
					print erroriter
#print LabelRaw[13][200][1]
#应该如何找到那个无法匹配的文件呢？
#print matchCount
'''go on '''
#下面根据合理的特征文件匹配标签，之后就可以开始做分类了，so happy
rootdir='./feature/'
FileList=[]
iter=0
for root,SubFloders,files in os.walk(rootdir):
	for f in files:
		if f.find('.pkl')!=-1:
			FileList.append(f)
print len(FileList)
featureName=[]
for item in FileList:
	#print item[:len(item)-4]	
	featureName.append(item[:len(item)-4])
#匹配featureName和Lable文件	
matchCount=0
for item in LabelRaw:
	iter=0
	for item1 in item:
		iter+=1
		if iter%2 != 0:
			for item2 in featureName:
				if item1[1][4:28]==item2:
					matchCount+=1
					break
print ("featureName和Lable文件匹配数")
print matchCount
#解析特征pkl文件
pkl_file=file('./feature/'+FileList[0],'rb')
data=pickle.load(pkl_file)
print("json的解析")
print len(data)
print data["those"]
Nsample=0
for item in FileList:
	pkl_file=file('./feature/'+item,'rb')
	data=pickle.load(pkl_file)
	Nsample+=len(data)
print Nsample#样本数为52083
#标签与样本的匹配，最关键的一步，加油，加油：
#找到之后存储到DataAndLabel
def trans3210(str):
	if str=='' or str=='1' or str=='2' or str==' ' or str=='13' or str=='12' or str=='4' or str=='11':
		return 0
	elif str=='3':
		return 1
	else :
		return str
DataAndLabel=[]
count=0
SampleCount=0
for item in LabelRaw:
	iter=0
	for item1 in item:
		iter+=1
		if iter%2==1:
			for itemFileList in featureName:
				if item1[1][4:28]==itemFileList:
					count+=1
					flag=0
					pkl_file=file('./feature/'+itemFileList+'.pkl','rb')
					data=pickle.load(pkl_file)
					#print type(data)
					#data1={"a":"apple","b":"banana"}
					for key in data:
						flag=0
						for iterN in range(len(item1)):
							#print item1(2)
							#itemWord=trans3210(item(iterN))
							if key==item1[iterN]:
								dataList=data[key]
								#print len(dataList)
								dataList.append(trans3210(item[iter][iterN]))
								DataAndLabel.append(dataList)
								SampleCount+=1
								flag=1
								break
						#flag=0
					#	if flag==0:
#							print key
						#	print data[key]
					#		print item1
					#		flag=0
							 

print count
print SampleCount
#print featureName
#print len(DataAndLabel)
# 把DataAndLabel写入文件
#file =open('./feature_result/feature','w')
#for item in DataAndLabel:
#	file.write(str(item[3])+'\t')
#	file.write(str(item[1]-item[0])+'\t')
#	file.write(str(item[2])+'\t')
#	file.write('\n')
#file.close()
'''
print DataAndLabel[1]
print(len(DataAndLabel))
for item in DataAndLabel:
	if len(item)!=5:
		print item
		print len(item)
'''

file5=open('./feature_result/trainDataBL','w')
file6=open('./feature_result/testDataBL','w')
for iter in range(len(DataAndLabel)):
	if len(DataAndLabel[iter])==6:
#	file1=open('./feature_result/trainData','w')
#	file2=open('./feature_result/testData','w')
		if iter <15000:
			file5.write(str(DataAndLabel[iter][5])+'\t')
			file5.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')
			file5.write('2:'+str(DataAndLabel[iter][2])+'\t')
			file5.write('\n')
		else:
			file6.write(str(DataAndLabel[iter][5])+'\t')
			file6.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')
			file6.write('2:'+str(DataAndLabel[iter][2])+'\t')
			file6.write('\n')
file5.close()
file6.close()

file1=open('./feature_result/trainData','w')
file2=open('./feature_result/testData','w')
file3=open('./feature_result/trainLabel','w')
file4=open('./feature_result/testLabel','w')
for iter in range(len(DataAndLabel)):
	if len(DataAndLabel[iter])==6:
#	file1=open('./feature_result/trainData','w')
#	file2=open('./feature_result/testData','w')
		if iter <15000:
			if DataAndLabel[iter][5]==1:
				for iter1 in range(2):
					file1.write(str(DataAndLabel[iter][5])+'\t')
					file1.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')#duration
					file1.write('2:'+str(DataAndLabel[iter][2])+'\t')#能量
					file1.write('3:'+str(DataAndLabel[iter][3])+'\t')#句子长度
					file1.write('4:'+str(DataAndLabel[iter][4][0])+'\t')#pitch mean
					file1.write('5:'+str(DataAndLabel[iter][4][1])+'\t')#pitch var
					file1.write('6:'+str(DataAndLabel[iter][4][2])+'\t')#pitch max
					file1.write('7:'+str(DataAndLabel[iter][4][3])+'\t')#pitch min
					file1.write('8:'+str(DataAndLabel[iter][4][4])+'\t')#pitch syllables
			#file1.write('4:'+str(DataAndLabel[iter][3]*DataAndLabel[iter][2])+'\t')
					file1.write('\n')
					file3.write(str(DataAndLabel[iter][5]))
					file3.write('\n')
			if DataAndLabel[iter][5]==0:
				file1.write(str(DataAndLabel[iter][5])+'\t')
				file1.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')#duration
				file1.write('2:'+str(DataAndLabel[iter][2])+'\t')#能量
				file1.write('3:'+str(DataAndLabel[iter][3])+'\t')#句子长度
				file1.write('4:'+str(DataAndLabel[iter][4][0])+'\t')#pitch mean
				file1.write('5:'+str(DataAndLabel[iter][4][1])+'\t')#pitch var
				file1.write('6:'+str(DataAndLabel[iter][4][2])+'\t')#pitch max
				file1.write('7:'+str(DataAndLabel[iter][4][3])+'\t')#pitch min
				file1.write('8:'+str(DataAndLabel[iter][4][4])+'\t')#pitch syllables
				file1.write('\n')
				file3.write(str(DataAndLabel[iter][5]))
				file3.write('\n')
		else:
			if DataAndLabel[iter][5]==1:
				for iter1 in range(2):
					file2.write(str(DataAndLabel[iter][5])+'\t')
					file2.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')
					file2.write('2:'+str(DataAndLabel[iter][2])+'\t')
					file2.write('3:'+str(DataAndLabel[iter][3])+'\t')
					file2.write('4:'+str(DataAndLabel[iter][4][0])+'\t')
					file2.write('5:'+str(DataAndLabel[iter][4][1])+'\t')
					file2.write('6:'+str(DataAndLabel[iter][4][2])+'\t')
					file2.write('7:'+str(DataAndLabel[iter][4][3])+'\t')
					file2.write('8:'+str(DataAndLabel[iter][4][4])+'\t')
			#file2.write('4:'+str(DataAndLabel[iter][3]*DataAndLabel[iter][2])+'\t')
					file2.write('\n')
					file4.write(str(DataAndLabel[iter][5]))
					file4.write('\n')
			if DataAndLabel[iter][5]==0:
				file2.write(str(DataAndLabel[iter][5])+'\t')
				file2.write('1:'+str(DataAndLabel[iter][1]-DataAndLabel[iter][0])+'\t')
				file2.write('2:'+str(DataAndLabel[iter][2])+'\t')
				file2.write('3:'+str(DataAndLabel[iter][3])+'\t')
				file2.write('4:'+str(DataAndLabel[iter][4][0])+'\t')
				file2.write('5:'+str(DataAndLabel[iter][4][1])+'\t')
				file2.write('6:'+str(DataAndLabel[iter][4][2])+'\t')
				file2.write('7:'+str(DataAndLabel[iter][4][3])+'\t')
				file2.write('8:'+str(DataAndLabel[iter][4][4])+'\t')
			#file2.write('4:'+str(DataAndLabel[iter][3]*DataAndLabel[iter][2])+'\t')
				file2.write('\n')
				file4.write(str(DataAndLabel[iter][5]))
				file4.write('\n')

					
file1.close()
file2.close()
file3.close()
file4.close()



# 样本的统计特征
#LabelTJ=[]
#for item in DataAndLabel:
#	LabelTJ.append(item[3])
#print("样本的统计特征：")
#myset=set(LabelTJ)
#for item in myset:
#	print LabelTJ.count(item), "of" ,item ,"in list"
	
