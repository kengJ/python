import os,shutil
import time
import pymssql

rootdir = "D:\IccoServer_new\TextData" #主文件夹
LogDir = 'LogData'

#判断文件是否存在
def checkExists(uri):
	return os.path.exists(getFileName(uri))
	
#获取文件名
def getFileName(uri):
	return os.path.join(rootdir,uri)
	
#'%Y%m%d'
def getdatetime(text):
	return time.strftime(text,time.localtime(time.time()))
	
def upLog(message):
    try:
        LogUri = '\%s\%s.txt' % (LogDir,getdatetime('%Y%m')) 
        LogFile = open(LoggetFileName(LogUri)File,'a')
        LogFile.write(message)
        LogFile.close()
    except Exception as e:
        print('ERROR:%s' % e)
    else:
        print('Log write success')

#检查文件夹
def checkFolder():	
    if not checkExists("\%s" % LogDir):
        print('Create Folder %s' % LogDir)
        os.makedirs(getFileName('\%s' % LogDir))

def uploadData(data):
    for i in range(0,len(list)):
		if os.path.isfile(getFileName(list[i])):
            num = open(path,'r').readlines()
            data.extend(num)
            maxnum = maxnum+len(num)
			#Log=Log+path+" 共"+str(len(num))+"条\n"
			#shutil.move(path,rootdir+"\\LogData\\"+str(datetime))

def main():
    list = os.listdir(rootdir)



# def main():
# 	list = os.listdir(rootdir)#
# 	datetime = time.strftime('%Y%m%d',time.localtime(time.time()))#文件名
# 	data = [] #汇总数据
# 	maxnum = 0 #记录条数汇总
# 	Log = str(datetime)+'\n' #日志

# 	wfile = open(os.path.join(rootdir,str(datetime)+".txt"),'a') #汇总文件
# 	LogFile = open(os.path.join(rootdir+"\\LogData\\"+str(datetime)+"_Log.txt"),'a') #日志文件


# 	#判断文件夹是否存在，不存在创建文件夹
# 	if not os.path.exists(rootdir+"\\LogData\\"+str(datetime)):
# 			print("create dir:"+rootdir+"\\LogData\\"+str(datetime))
# 			os.makedirs(rootdir+"\\LogData\\"+str(datetime))

# 	#遍历 文件
# 	for i in range(0,len(list)):
# 		path = os.path.join(rootdir,list[i])
# 		if os.path.isfile(path):
# 					num = open(path,'r').readlines()
# 					data.extend(num)
# 					maxnum = maxnum+len(num)
# 			#Log=Log+path+" 共"+str(len(num))+"条\n"
# 			shutil.move(path,rootdir+"\\LogData\\"+str(datetime))

# 	#输出文件条数和写入条数
# 	Log=Log+"汇总条数:"+str(maxnum)+"\n"+"写入条数:"+str(len(data))+"\n"

# 	#写入文件
# 	#wfile.writelines(data)
# 	# print(os.path.join(rootdir+"\\bak",str(datetime)+".txt"))

# 	#写入日志信息
# 	#LogFile.write(Log)

# 	#关闭文件
# 	LogFile.close()
# 	wfile.close()

# 	print("success")
upLog()
