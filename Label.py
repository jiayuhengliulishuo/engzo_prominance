#encoding=utf-8
import csv
import os
import sys
import pickle
def csv2list(filename):
	listout=[]
	with open(filename) as f:
		reader=csv.reader(f)
		for row in reader:
			listout.append(row)
	return listout
rootdir='./engVotingJIA/'
FileList=[]
iter=0
for root,SubFloders,files in os.walk(rootdir):
	for f in files:
		if f.find('.csv')!=-1:
			FileList.append(os.path.join(root,f))
listZong=[]
for item in FileList:
	lists=[]
	lists=csv2list(item)
	listZong.append(lists)
	#print(len(lists))
	#for item1 in lists:
	#	print len(item1)
#print(FileList)
print len(listZong)
for item in listZong:
	print len(item)
	#for item1 in item:
		#print len(item1)
#把结果载入pkl文件
pkl_file=file('Label.pkl','wb')
pickle.dump(listZong,pkl_file)
pkl_file.close()
def list2csv(eng1,filename):#write eng1 in a csv file
	csvfile=file(filename,'wb')
	writer=csv.writer(csvfile)
	iter=0
	listn=[]
	for item in eng1:
		iter+=1
		if iter%2==0:
                        #这部分把文件转化成 1   0 格式

#                       for i in range(len(item)):
#                               if item[i]==3:
#                                       item[i]=1
#                               else :
#                                       item[i]=0

                        # or 1 2 3 4    
			for i in range(len(item)):
				if item[i]==0:
					listn.append(' ')
				else:
					listn.append(str(item[i]))
		else:
			listn=item
		writer.writerow(listn)
	listn=[]
	csvfile.close()
	iter=0
	return csvfile

#for item in FileList:
#	if 
#print iter
