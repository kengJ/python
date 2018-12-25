import sqlite3 as sq# sqlite
import pymssql as ms # mssql
import pymysql as my # mysql

# 处理pyinstaller 和 pymssql 闪退问题

import uuid
import _mssql
import decimal
import pypyodbc
decimal.__version__
uuid.ctypes.__version__
_mssql.__version__

class db:
	def __init__(self,type='',file='',host='',username='',password='',database=''):
		dbType = ['sqlite','mssql','mysql']
		# 判断系统类型
		if not type in dbType:
			raise RuntimeError('数据库类型错误，类型必须为:'+','.join(dbType))
			return 
		self.type = type
		if type == 'sqlite':
			self.conn = sq.connect(file)
		elif type == 'mssql':
			self.conn = ms.connect(host=host,user=username,password=password,database=database,charset='utf8')
		elif type == 'mysql':
			self.conn = my.connect(host=host,user=username,password=password,database=database,charset='utf8')
		self.cur = self.conn.cursor()
		
	def __execute(self,sql):
		try:
			self.cur.execute(sql)
			self.conn.commit()
			return True
		except Exception as e:
			self.conn.rollback()
			print(e)
			return False
	def select(self,sql):
		try:
			self.cur.execute(sql)
			data = self.cur.fetchall()
			return data
		except Exception as e:
			print(e)
	def sql(self,sql):
		return self.__execute(sql)
	def insertMany(self,sql,data):
		if self.type =='sqlite':
			sql = sql.replace('%s','?')
		try:
			self.cur.executemany(sql,data)
			self.conn.commit()
			return True
		except Exception as e:
			self.conn.rollback()
			print(e)
			return False
	def close():
		self.cur.close()
		self.conn.close()
	def getcur(self):
		return self.cur
"""	
class sqlite:
	def __init__(self,file):
		self.file = file
		self.__connect()
	def __connect(self):
		self.conn = sq.connect(self.file)
		self.cur = self.conn.cursor()
		
class mssql:
	def __init__(self,host,username,password,database):
		self.host = host
		self.username = username
		self.password = password
		self.database = database
		self.__connect()
	def __connect(self):
		self.conn = ms.connect(host=self.host,user=self.username,password=self.password,database=self.database,charset='utf8')
		self.cur = self.conn.cursor()

class mysql:
	def __init__(self,host,username,password,database):
		self.host = host
		self.username = username
		self.password = password
		self.database = database
		self.__connect()
	def __connect(self):
		self.conn = my.connect(host=self.host,user=self.username,password=self.password,database=self.database,charset='utf8')
		self.cur = self.conn.cursor()
"""		