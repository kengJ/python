import os,xlwt,time,xlsxwriter,pymssql
#用于写入数据

def createXls(data,filename):
    workbook = xlwt.Workbook(encoding='utf-8') 
    for key in data.keys():
        worksheet = workbook.add_sheet(key, cell_overwrite_ok=True) 
        worksheet = writeSheet(data[key],worksheet)
    workbook.save(checkFile(filename,'.xlsx'))
    return workbook

def createXlsx(data,filename):
    workbook = xlsxwriter.Workbook(checkFile(filename,'.xls'))
    for key in data.keys():
        worksheet = workbook.add_worksheet(key)
        worksheet = writeSheet(data[key],worksheet)
    workbook.close()
    return workbook

def checkFile(filename,fileType):
    #判断文件名是否存在
    if os.path.exists(filename):
        filename = filename[:filename.rfind('.')] + time.strftime("%Y%m%d%H%M%S", time.localtime())+fileType
    return filename

def writeSheet(data,worksheet):
    row,col = 0,0
    for line in data:
        for value in line:
            worksheet.write(row,col,value)
            col = col + 1
        row = row + 1
        col = 0
    return worksheet

def main(data,filename):
    #获取工作表最大数据行数
    maxLine = 0
    for sheet in data:
        if len(sheet) > maxLine:
            maxLine = len(sheet)
    #判断数据最大行数是否超过6000
    workbook = None
    if maxLine < 6000:
        workbook = createXls(data,filename)
    else:
        workbook = createXlsx(data,filename)

def createComputer():
    file = open('./computer.txt','w')
    codes = ''
    for code in range(0,8000):
        if len(str(code))<4:
            for index in range(0,4-len(str(code))):
                code = '%s%s' % ('0',str(code))
        else:
            code = str(code)
        codes = codes + '\np0'+str(code) 
    file.write(codes)    
    file.close()

def checkData(starttime,endtime):
    sql = '''select IC.Clock_id,IC.Clock_name,ZE.CODE,KC.CardNo,ZE.NAME,CONVERT(varchar(50),FS.brushdt,20) from fk_shuaka FS
LEFT JOIN ICCO_Clockskq IC ON FS.machineno = IC.Clock_id
LEFT JOIN Kq_Card KC ON KC.Date0<'%s 00:00:00.000' AND Date1 >'%s 23:59:59.000' AND KC.CardNo = FS.cardno
LEFT JOIN ZlEmployee ZE ON KC.EmpID = ZE.ID
where FS.brushdt BETWEEN '%s' AND '%s 23:59:59.000' 
AND IC.Clock_id in('6469','6470','6471','6472') AND KC.CardNo <>'' AND KC.CardNo <> '000000      ' ''' %(starttime,endtime,starttime,endtime)
    conn=pymssql.connect(host='192.168.117.20',user='tx_app',password='app#%(app23',database='TxCard')
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    return result

def test():
    starttime = input('请输入时间\n')
    #endtime = input('请输入结束时间\n')
    result = checkData(starttime,starttime)
    data = {starttime:result}
    main(data,starttime+'.xls')
test()
