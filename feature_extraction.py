#encoding=utf-8
import json
import os
import sys
import csv
import pickle
import numpy
def list2mean(list1):
	N=len(list1)
	#listn=float(list1)
	listn=list1
	narray=numpy.array(listn)
	sum1=narray.sum()
	mean=sum1/float(N)
	return mean
def list2var(list1):
	N=len(list1)
	#listn=float(list1)
	listn=list1
	narray=numpy.array(listn)
        sum1=narray.sum()
	mean=float(sum1/N)
	narray2=narray*narray
	sum2=narray2.sum()
	var=float(sum2/N-mean**2)
	return var
def list2max(list1):
	#listn=float(list1)
	listn=list1
	return max(listn)
def list2min(list1):
	listn=list1
	#listn=float(list1)
	return min(listn)
def getvalfeature(position,vals,start,end,low,high):
	startp=low
	endp=high
	for iter in range(len(position)):
		if position[iter]==start:
			startp=iter
			break
	for iter in range(len(position)):
		if position[iter]==end:
			endp=iter
			break
	return vals[startp:endp]

def intonation_feature(feature_dict):
	f_outdict=dict()
	station=[]
	position=range(feature_dict["intonation_curve"]["start"],feature_dict["intonation_curve"]["end"]+1)
	vals=feature_dict["intonation_curve"]["vals"]
	for item in feature_dict["words"]:
#		print item["word"]["stats"]["start"]
#		print type(item["word"]["stats"]["start"])
		station.append(item["stats"]["start"])
		station.append(item["stats"]["end"])
	high=max(station)
	low=min(station)
	for item in feature_dict["words"]:
		if item["stats"]["start"]<low or item["stats"]["end"]>high:
			#lsit=list2mean(vals)
			list=[list2mean(vals),list2var(vals),list2min(vals),list2max(vals),len(item["syllables"])]
			f_outdict[item["word"]]=list
			#f_outdict[item["word"]]=[]
			#f_outdict[item["word"]].append(list2mean(vals))
			#f_outdice[item["word"]].append(list2var(vals))
			#f_outdice[item["word"]].append(list2min(vals))
			#f_outdice[item["word"]].append(list2max(vals))
		else:
			start=item["stats"]["start"]
			end=item["stats"]["end"]
			nvals=getvalfeature(position,vals,start,end,low,high)
			#list=list2mean(nvals)
			list=[list2mean(nvals),list2var(nvals),list2min(nvals),list2max(nvals),len(item["syllables"])]
			f_outdict[item["word"]]=list
			#f_outdict[item["word"]]=[]
			#f_outdict[item["word"]].append(list2mean(nvals))
			#f_outdice[item["word"]].append(list2var(nvals))
			#f_outdice[item["word"]].append(list2min(nvals))
			#f_outdice[item["word"]].append(list2max(nvals))
	return f_outdict
	
def json2feature(filename):
	json_data=open(filename)
	data=json.load(json_data)
#	print type(data["intonation_curve"]["start"])
#	print data["intonation_curve"]["start"]
	feature=dict()
	f_outdict=intonation_feature(data)
#	print data["intonation_curve"]	
	
	for item in data["words"]:#下面那句决定提取的特征
		#feature[item["word"]]=[item["stats"]["start"],item["stats"]["end"],item["stats"]["energy"]]
		#基本特征＋句子长度特征
		#feature[item["word"]]=[item["stats"]["start"],item["stats"]["end"],item["stats"]["energy"],len(data["words"])]
        	#所有的特征
		feature[item["word"]]=[item["stats"]["start"],item["stats"]["end"],item["stats"]["energy"],len(data["words"]),f_outdict[item["word"]]]
	return feature
rootdir='./json2'
FileList=[]# 将被处理文件的目录
for root,SubFloders,files in os.walk(rootdir):
	for f in files:
		if f.find('.json')!=-1:
		#	FileList.append(os.path.join(root,f))
			FileList.append(f)
			#print(os.path.join(root,f))
	errormessage=[]
count_IC=0
for item in FileList:#特征提取
	#print(type(item))
	#print len(item)
	count_IC+=1
	filename='./json/'+item
	#print item
	#feature=json2feature(filename)
	#print count_IC
	try:
		feature=json2feature(filename)
		pkl_file = file('./feature/'+item[:len(item)-5]+'.pkl','wb')     #文件保存在item.pkl中
		pickle.dump(feature, pkl_file)     #通过dump函数进行序列化处理
		pkl_file.close()
	except:
		
		#print item[:len(item)-5]
		errormessage.append(item[:len(item)-5])
	
	#print('./json/'+ item)
	#os.system(str)
print(len(FileList))
#print(os.getcwd())
print("出错文件数目")
print(len(errormessage))
print errormessage[0]
#print errormessage
pkl=file('error2.pkl','wb')
pickle.dump(errormessage,pkl)
pkl.close()
'''
filename='test.json'
json_data=open(filename)
data=json.load(json_data)
feature=dict()
for item in data["words"]:
	feature[item["word"]]=[item["stats"]["start"],item["stats"]["end"],item["stats"]["energy"]]
	print item["word"]
	#print item["stats"]["start"]
	#print item["stats"]["end"]
	#print type(item["stats"]["energy"])#float 类型  
print feature#经过实验验证engery是经过归一化的
#文件写入:
outname=filename[:len(filename)-5]+'.json'
print outname'''
'''output=open(outname,'w')
for key in feature:
	output.write(key)
output.write(feature)
output.close()
encodejson=json.dumps(feature)
print encodejson
#out=open(outname,'w')
	#out.write(encodejson)
#out.close()
pkl_file = file(filename[:len(filename)-5]+'.pkl','wb')     #文件保存在account.pkl中
pickle.dump(feature, pkl_file)     #通过dump函数进行序列化处理
pkl_file.close()'''
#解析pkl文件
'''
pkl_file = file(filename[:len(filename)-5]+'.pkl','rb')         #打开刚才存储的文件
account_dic = pickle.load(pkl_file)         #通过load转换回来
print account_dic
print type(account_dic)
pkl_file.close()'''
