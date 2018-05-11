import os,pymssql,shutil,time,datetime

#获取数据库链接
def getConn():
    return pymssql.connect(host='192.168.117.20',user='tx_app',password='app#%(app23',database='TxCard')

#写入数据库
def updateSql(conn,data):
    #6006+695304+0+2018-05-06 21:22:28
    subsql = ''
    for line in data:
        MACHINENO = line[0:4]
        CARDNO = line[5:11]
        FRUSHDT = '%s-%s-%s %s:%s:%s.000' % (line[12:16],line[16:18],line[18:20],line[20:22],line[22:24],line[24:26])
        subsql = "%s('%s','%s','%s')," % (subsql,CARDNO,MACHINENO,FRUSHDT)
    sql = '''INSERT INTO fk_shuaka (CARDNO,MACHINENO,FRUSHDT) VALUES %s''' % subsql
    sql = sql[:-1]
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

def getFileList(uri):
    filelist = list()
    for filename in os.listdir(uri):
        if '.txt' in filename:
            filelist.append(filename)
    return filelist

def checkDri(uri):
    if not os.path.exists(uri):
        os.makedirs(uri)

def removeFile(datadir,logdir,filename,date,log):
    LogDataDir = os.path.join(logdir,date)#数据备份文件夹
    #判断日志相关文件夹是否存在
    checkDri(logdir)
    checkDri(LogDataDir)
    #读取文件编号
    fileIndex = len(os.listdir(LogDataDir))+1
    oldfile = os.path.join(datadir,filename)#移动前的文件地址
    newfile = os.path.join(LogDataDir,'%s %d.txt' % (date,fileIndex))#移动后的文件地址
    log += getlog(log,'文件备份:把%s文件移动至%s' % (oldfile,newfile))
    #移动文件
    shutil.move(oldfile,newfile)
    return log

#获取当前日期 
def gettime(type="%Y%m%d"):
    return time.strftime(type, time.localtime())

#删除半年前的文件并写入日志
def delFile(log,logdir,date):
    flist = os.listdir(logdir)
    for name in flist:
        if not '.txt' in name:
            ftime = datetime.datetime.strptime(name, '%Y%m%d')
            now = datetime.datetime.strptime(date, '%Y%m%d')
            if (now-ftime).days > 183:
                message = '删除%s数据文件夹' % name
                log += getlog(log,message)
                shutil.rmtree(os.path.join(logdir,name))
    return log

#日志处理
def getlog(log,message):
    return '%s => %s\n' %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),message)
    #return log
    

#主程序
def main():
    #1.把文档移动到日志文件
    #2.数据写入数据库
    #3.写入当月日志文件
    #4.删除三个月前的数据文件
    log = ''
    rootdir = 'D:\Progra~1\通用接口软件\TextData'
    logdir = os.path.join(rootdir,'LogData')
    conn = getConn()
    date = gettime()#当前日期
    filenames = getFileList(rootdir)#数据文件列表
    #移动文件
    for filename in filenames:
        removeFile(rootdir,logdir,filename,date)
    #删除3个月前的文件夹
    delFile(log,logdir,date)
    
def test():
    log = ''
    rootdir = 'D:\Progra~1\通用接口软件\TextData'
    logdir = os.path.join(rootdir,'LogData')
    date = gettime()#当前日期
    filenames = getFileList(rootdir)#数据文件列表
    #移动文件
    for filename in filenames:
        log = removeFile(rootdir,logdir,filename,date)
    #写入数据
    #for filename in os.listdir(os.path.join(logdir,date)):
    #   file = open(os.path.join(os.path.join(logdir,date),filename),'r')
    #   data = file.readlines()
    #    updateSql(conn,data)  
    #删除超过半年的备份数据
    log = delFile(log,logdir,date)
    #写入日志
    if len(log)>0:
        logfile = open(os.path.join(logdir,gettime(type="%Y%m")+'_log.txt'),'a')
        logfile.write(log)
        logfile.close()
#main()
test()
