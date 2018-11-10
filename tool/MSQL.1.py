import pymssql
import xlwt

conn = pymssql.connect(host="192.168.117.35",user="conn",password="nnoc",database="adirectory",charset="utf8")
cur = conn.cursor()
if not cur:
    raise (NameError,"数据库连接失败")
cur.execute("select rtrim(code),name from zlemployee where name in ('郭建刚','郭建强','曾展晖','温焯东','杨芳欣','王伟','李亚平','邓庆晖','张宁和','谭本乡','欧华钊','张以飞','陈龙辉','卢玉妹','周荣生','谢小华','蒋演彪','潘卫东','梁锐昌','辜芳磊','马见丹','伍彩颜','李永东','曾洁云') and (name <> '王伟' or (name = '王伟' and zhiwu like '%总裁%'))")
resList = cur.fetchall()#fetchall()是接收全部的返回结果行
# conn.close()
# print(resList)
zlemployeeList = {}
# print(zlemployeeList)
codes = ""
for person in resList:
    zlemployeeList[person[0]] = [person[0],person[1]]
    codes = codes + "'" + person[0] + "',"
# print(zlemployeeList)
cur.execute("select employeeid0,username0 from Employee_System_DATA  where employeeid0 in ("+codes[:-1]+')')
resList = cur.fetchall()
# print(resList)
message = {}
for computer in resList:
    data = zlemployeeList[computer[0]]
    zlemployeeList[computer[0]] = [data[0],data[1],computer[1]]
    #name = zlemployeeList[computer[0]]
    #message[computer[0]] = [computer[0],name,computer[1]]
# print(zlemployeeList)

book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
row = 0
for line in zlemployeeList:
    #print(line)
    col = 0
    for value in zlemployeeList[line]:
        sheet.write(row,col,value)
        col+=1
    row+=1
book.save('stu_1.xls')