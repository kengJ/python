import os,pymssql,xlrd

def getValue(sheetBook,row,index):
    return str(int(sheetBook.cell(row,index).value)) if  type(sheetBook.cell(row,index).value)==type(1) else str(sheetBook.cell(row,index).value)

# 读取文档
datas = xlrd.open_workbook('datas.xls')
file = open('sql.txt','w',encoding='utf-8')
file.write("--插入宿舍信息 E_Room\n")
file.write('insert into E_Room \n(Code,BedCount,FType,D_Home,UsableBed)\n')
# 读取
names,i,namelist = '',1,datas.sheet_names()
for name in namelist:
    names+=str(i)+'.'+name+'\n'
    i+=1
sheetIndex = input(names)
try:
    sheetName = namelist[int(sheetIndex)-1]
except Exception as e:
    print('输入值:'+sheetIndex+'错误')
    exit()
sheetBook = datas.sheet_by_name(sheetName)
row,col,rows = 1,2,sheetBook.nrows
print('总行数:'+str(rows))
for rowvalues in range(1,rows):
    No = getValue(sheetBook,row,1)#str(sheetBook.cell(row,1).value)
    Code  = getValue(sheetBook,row,2)#str(sheetBook.cell(row,2).value)
    Bed = getValue(sheetBook,row,3)#str(int(sheetBook.cell(row,3).value))
    FType = getValue(sheetBook,row,4)#str(int(sheetBook.cell(row,4).value))
    if rowvalues==rows-1:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','0')\n")
    else:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','0'),\n")
    row+=1
file.write()
file.close()
