import pymssql
from prettytable import PrettyTable
import os
import xlwt # excel 写入

# 处理pyinstaller 和 pymssql 闪退问题
import uuid
import _mssql
import decimal
import pypyodbc
decimal.__version__
uuid.ctypes.__version__
_mssql.__version__

# 处理pyinstaller 和 pymssql 闪退问题

##############################################公共工具函数#####################################################################
# 链接数据库
def conndb(host,username,password,database):
	conn = pymssql.connect(host=host,user=username,password=password,database=database,charset='utf8')
	cur = conn.cursor()
	return (conn,cur)
# 关闭数据库链接
def connClose(conn):
	conn.close()
	
# 数据库查询操作
def select(cur,sql):
	cur.execute(sql)
	data = cur.fetchall()
	if len(data)>0:
		return data
	else:
		return None

# 数据库增删改操作
def commit(sql):
	cur.execute(sql)
	conn.commit()

#批量插入
def insert(cur,sql,data):
	cur.executemany(sql,data)
	conn.commit()

# 格式化 输出
def formatTable(data,title,setting={}):
	x = PrettyTable(title)
	x.padding_width = 1
	if len(setting)>0:
		for key in sorted(setting):	
			if setting[key] == 'left':
				x.align[key] = 'l'
	if len(title) == len(data[0]):
		for line in data:
			x.add_row(line)
	else:
		for line in data:
			lineData = []
			for index in range(0,int(len(title))-1):
				lineData.append(line[index])
			x.add_row(lineData)
	print(x)

# 递归
def callbackFunc(message,func):
	check = input(message)
	if check == 'y':
		func()

# 遍历文件目录
def listDri(url,setting={}):
	files = os.listdir(url)
	if not ('print' in setting and setting['print'] == 'off'):
		for index in range(0,len(files)):
			print('%d.%s' % (index+1,files[index]))
	return files

# excel 写入
def excelWrite(data,uri,title=[]):
	# 判断是否有标题存在
	# 判断是否有数据
	if len(data)>0:
		book = xlwt.Workbook(encoding='utf-8', style_compression=0)
		for key in sorted(data):
			row = 0
			col = 0
			sheet = book.add_sheet(key, cell_overwrite_ok=True)
			if len(title) > 0:
				for value in title:
					sheet .write(row,col,value)
					col += 1
				row += 1
			for line in data[key]:
				col = 0
				for value in line:
					sheet .write(row,col,value)
					col += 1
				row += 1
		book.save(uri)	
				
##################################################################################################################################		
