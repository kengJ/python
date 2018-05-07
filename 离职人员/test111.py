import xlrd
import pymssql
import xlwt
import os

def createExcel():
    workbook = xlrd.open_workbook('C:\\Users\\heyanzhu\\Desktop\\互联网权限在用人员（工号）.xls')
    booksheet = workbook.sheet_by_index(0)
    #print(booksheet.col_values(0))
    codes = ''
    error = ''
    for code in booksheet.col_values(0):
        code = code.replace(' ','')
        if len(code)==6:
            codes = "%s'%s'," % (codes,code)
        else:
            error = "%s'%s'," % (error,code) 
    #print('codes:'+codes[:-1])
    if len(error)>0:
        print('error:部分值错误'+error[:-1])
    sql = 'select rtrim(a.code),a.name,b.longname,CONVERT(varchar(12),lzdate,111) from zlemployee a left join zldept b on a.dept = b.code where a.code in (%s) and a.state <> 0' % codes[:-1]
    #print(sql)

    conn=pymssql.connect(host='192.168.117.20',user='tx_app',password='app#%(app23',database='TxCard')
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    #print(result)
    #workbook = xlrd.open_workbook('C:\\Users\\heyanzhu\\Desktop\\互联网权限在用人员（工号）.xls')
    workbook = xlwt.Workbook(encoding='utf-8')  
    booksheet = workbook.add_sheet('lzdata', cell_overwrite_ok=True)
    row = 0
    col = 0
    for line in result:
        for value in line:
           booksheet.write(row,col,value)
           col = col + 1
        col = 0
        row = row + 1
    workbook.save(os.getcwd()+'\\离职人员信息.xls')
print('当前目录:%s' % os.getcwd())
#print(os.listdir(os.getcwd()))
files = list()
index = 0
for filename in os.listdir(os.getcwd()):
    if not filename in ('test111.py','start.bat'):
        #print('%d.%s' % (index,filename))
        #index = index + 1
        files.append(filename)
if len(files)==0:
    print('找不到数据源文件')
    input('输入回车结束')
    exit()
for f in files:
    index = index + 1
    print('%d.%s' % (index,f))
    
fileindex = int(input('请选择文件序号:'))
if fileindex-index>0:
    print('输入错误，程序结束')
    input('输入回车结束')
    exit()
print('选择文件:%s' % files[fileindex-1])
print('正在导出数据 文件名:离职人员信息.xls')
createExcel()
print('导出完成')
input('请输入回车结束')
