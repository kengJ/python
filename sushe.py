import os,xlrd

def getValue(sheetBook,row,index):
    return str(int(sheetBook.cell(row,index).value)) if  type(sheetBook.cell(row,index).value)==type(1) else str(sheetBook.cell(row,index).value)

# 读取文档
datas,file = xlrd.open_workbook('datas.xls'),open('sql.txt','w',encoding='utf-8')
file.write("--插入宿舍信息 E_Room\ninsert into E_Room \n(Code,BedCount,FType,D_Home,UsableBed) values\n")
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
    No = getValue(sheetBook,row,1)
    Code  = getValue(sheetBook,row,2)
<<<<<<< HEAD
    Bed = getValue(sheetBook,row,3)[0:1]
    FType = str(getValue(sheetBook,row,4))[0:1]
=======
    Bed = getValue(sheetBook,row,3)
    FType = getValue(sheetBook,row,4)
>>>>>>> 401fad2cda96d748ce47eee8fd928d7e0257cd8d
    if rowvalues==rows-1:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','0')\n")
    else:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','"+Bed+"'),\n")
    row+=1
<<<<<<< HEAD
#file.write()
=======
file.write('--插入宿舍信息 E_Room 完成\n--插入煤气表数据\ninsert into D_Gas\n(Code,name,notes) values\n')
row=0
for rowvalues in range(1,rows):
    No = getValue(sheetBook,row,1)
    Code  = getValue(sheetBook,row,2)
    if rowvalues==rows-1:file.write("('"+Code+"','"+No+"','宿舍热水表')\n")
    else:file.write("('"+Code+"','"+No+"','宿舍热水表'),\n")
    row+=1
file.write('--插入煤气表数据 完成\n')
No = input('请输入宿舍楼编号\n')
Name = input('请输入宿舍楼名称')
if No==None:
    print('宿舍楼编号不能为空\n')
    exit()
if Name==None:
    print('宿舍楼名称不能为空\n')
    exit()
file.write("--插入水表\ninsert into D_Gas (Code,name) values ('"+No+"','"+Name+"公用水表')\n")
file.write("--插入电表\ninsert into D_Meter (Code,name) values ('"+No+"','"+Name+"公用电表')")
>>>>>>> 401fad2cda96d748ce47eee8fd928d7e0257cd8d
file.close()
