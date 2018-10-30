import os,xlrd

def getValue(sheetBook,row,index):
    try:
        value = str(int(sheetBook.cell(row,index).value)) if type(sheetBook.cell(row,index).value)==type(1) else str(sheetBook.cell(row,index).value)    
        if value.find('.')>=0:
            #print(value)
            value = value[0:value.find('.')]
    except Exception as e:
        print('getValue()错误:',e)
        print('row:'+str(row)+",index:"+str(index))
        exit()
    return value

# 读取文档
datas,file = xlrd.open_workbook('宿舍导入模板20181029.xls'),open('sql.txt','w',encoding='utf-8')
file.write("--插入宿舍信息 E_Room\ninsert into E_Room \n(Code,BedCount,FType,D_Home,UsableBed) values\n")
# 读取
# 遍历工作薄中的工作表名，并进行输出
names,i,namelist = '',1,datas.sheet_names()
for name in namelist:
    names+=str(i)+'.'+name+'\n'
    i+=1
# 遍历完成，进行输出，选择需要的工作表
sheetIndex = input(names)
# 对选择的工作表进行检测
try:
    sheetName = namelist[int(sheetIndex)-1]
except Exception as e:
    print('输入值:'+sheetIndex+'错误')
    exit()
# 检测完成,获取到选择的工作表
sheetBook = datas.sheet_by_name(sheetName)
# 定义行、列的默认值和最大行数
row,col,rows = 1,2,sheetBook.nrows
print('总行数:'+str(rows))
for rowvalues in range(1,rows):
    Code  = getValue(sheetBook,row,0)
    Bed = getValue(sheetBook,row,1)
    FType = getValue(sheetBook,row,2)
    No = getValue(sheetBook,row,3)
    #if rowvalues==rows-1:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','0')\n")
    #else:file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','"+Bed+"'),\n")
    file.write("('"+Code+"','"+Bed+"','"+FType+"','"+No+"','"+Bed+"'),\n")
    row+=1
file.write('总行数:'+str(rows))
file.close()
