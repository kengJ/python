from tool import excelHelper as excelHelper
from tool import dbHelper as dbHelper

excel = excelHelper('./test.xlsx','r')
excel.file.setTable()
#excel.setTable()
data = excel.file.getData()
sql = """
insert into clocks (clock_id,clock_name,clock_model,outintype,usetype,clocksn,tcpip_address,tcpip_port,call_kind,clock_type)
values (%s,%s,'S301系列',0,2,%s,%s,4001,1,1)
"""
insertData = []
for line in data:
	lineData = (str(line[3]).split('.')[0],line[0],line[2],line[1])
	insertData.append(lineData)

host='192.168.119.205'
username='sa'
password='donlim.com'
database='XK_lockserver'
mssql = dbHelper(host=host,username=username,password=password,database=database,type='mssql')
mssql.insertMany(sql,insertData)