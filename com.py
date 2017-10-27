# -*- coding: utf-8 -*-
import os
import xlwt,xlrd,pymssql
import random,string
'''
from com import *

xlwt:写入excel文件
xlrd:读取excel文件
pymssql:sqlserver驱动
'''

#字节转换类
class Code:
	__character =''#字节码

	#构造时指定字节码
	def __init__(self,character):
		self.__character = character

	#转换字节码
	def gbk(self,str):
		return str.decode('utf-8').encode(self.getCharacter())

	#获取当前设置的字节码
	def getCharacter(self):
		return self.__character

#用于转换Excel
class Excel:
	def __init__(self):
		pass

	#创建excel
	def createExcel(self):
		return xlwt.Workbook(encoding = 'utf-8')
	#创建工作表
	def AddWorkSheel(self,workbook,SheetName):
		return workbook.add_sheet(SheetName)
	#保存excel
	def Save(self,workbook,FileName):
		try:
			workbook.save(FileName)
		except Exception as e:
			return False
		else:
			return True
	#打开excel
	def OpenExcel(self,FileName):
		return xlrd.open_workbook(FileName)
	#读取一个工作表
	def ReadSheet(self,key,value,workbook):
		if key=='Num' or key == 'num':
			return workbook.sheets()[value]
		elif key == 'Name' or key == 'name':
			return workbook.sheet_by_name(value)
		else:
			return None
	#读取一行记录
	def getRows(self,sheet):
		sheet.nrows()
	#读取一列记录
	def getCols(self,sheet):
		sheet.ncols()

	def getColByNo(self,No,sheet,startNo=None,endNo=None):
		return formatData(sheet.col_values(No),startNo,endNo)

	def getRowByNo(self,No,sheet,startNo=None,endNo=None):
		return formatData(sheet.row_values(No),startNo,endNo)

	def getValue(self,sheet,row,col):
		return sheet.cell_value(row,col)

	def formatData(self,data,startNo,endNo):
		if startNo is None and endNo is None:
			return data
		elif not startNo is None and not endNo is None:
			return data[startNo:endNo]
		elif not startNo is None:
			return data[startNo:]
		elif not endNo is None:
			return data[:endNo]
		else:
			return None 

#基础处理
class Base:

	def __init__(self):
		pass

	#in ()
	def getCode(self,FileName):
		file = open(FileName,'r').readlines()
		codes = ''
		for f in file:
			codes+="'"+f.lstrip().replace('\n','')+"',"
		return codes[:-1]

	#,
	def getCode1(self,FileName):
		file = open(FileName,'r').readlines()
		codes = ''
		for f in file:
			codes+=f.replace('\n','')+","
		print codes[:-1]

	def getCode2(self,FileName,key='y'):
		file = open(FileName,'r').readlines()
		codes = list()
		for f in file:
			codes.append(f.lstrip().replace('\n',''))
		code_list={}.fromkeys(codes).keys()
		code_str = ''
		if key=='y':
			print len(code_list)
		for code in code_list:
			code_str+="'"+code+"',"
		return code_str[:-1]

	def getCode3(self,FileName,key='y'):
		file = open(FileName,'r').readlines()
		codes = list()
		for f in file:
			code=f.lstrip().replace('\n','')
			index = 6-len(code)
			addtext=''
			if index==1:
				addtext='0'
			elif index==2:
				addtext='00'
			elif index == 3:
				addtext='000'
			elif index==4:
				addtext='0000'
			elif index==5:
				addtext='00000'
			code = addtext+str(code)+'\n'
			codes.append(code)
		return codes
	#{}.fromkeys(l1).keys()

	#返回txt 所有行 并包装成数组
	def getTxt(self,FileName):
		return open(FileName).readlines()

	def getTxtByNo(self,FileName,No):
		return self.getTxt(FileName)[No]


#sqlserver管理
class MssqlServer:
	
	__host = ''
	__user = ''
	__password = ''
	__database = ''
	__character = ''
	__conn = None

	def __init__(self,FileName=None,SqlModel=None):
		if FileName==None:
			__host = SqlModel.host
			__user = SqlModel.user
			__password = SqlModel.password
			__database = SqlModel.database
			__character = SqlModel.character 
			self.Conn()
		else:
			b= Base()
			__host = b.getTxtByNo(FileName,0)
			__user = b.getTxtByNo(FileName,1)
			__password = b.getTxtByNo(FileName,2)
			__database = b.getTxtByNo(FileName,3)
			__character = b.getTxtByNo(FileName,4)
			self.Conn()

	#创建连接
	def Conn(self):
		self.__conn = pymssql.connect(
			host=self.__host,
			user=self.__user,
			password=self.__password,
			database=self.__database,
			charset=self.__character
			)

	#执行sql 输出数据
	def Sql(self,sql):
		cur = __conn.cursor()
		cur.execute(sql)
		data = cur.fetchall()
		return data

class SqlModel:
	host = ''
	user = ''
	password = ''
	database = ''
	character = ''

#生成随机数
class randomHelper:
	def setlistNumber(self):
		return ['0','1','2','3','4','5','6','7','8','9']

	def getrandom(self,list):
		return string.join(random.sample(list, 8)).replace(" ","")