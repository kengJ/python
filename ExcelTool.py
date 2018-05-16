import os,xlwt,time,xlsxwriter
#用于写入数据

def createXls(data,filename):
    workbook = xlwt.Workbook(encoding='utf-8') 
    for key in data.keys():
        worksheet = workbook.add_sheet(key, cell_overwrite_ok=True) 
        worksheet = writeSheet(data[key],worksheet)
    workbook.save(checkFile(filename))
    return workbook

def createXlsx(data,filename):
    workbook = xlsxwriter.Workbook(checkFile(filename))
    for key in data.keys():
        worksheet = workbook.add_worksheet(key)
        worksheet = writeSheet(data[key],worksheet)
    workbook.close()
    return workbook

def checkFile(filename):
    #判断文件名是否存在
    if os.path.exists(filename):
        filename = filename[:filename.rfind('.')] + time.strftime("%Y%m%d%H%M%S", time.localtime())+filename[filename.rfind('.',0):]
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