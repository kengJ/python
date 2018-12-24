import xlwt,xlrd # excel 写入
import openpyxl # excel 2007
import XlsxWriter # excel 2007解决方案

class excel:
	def __init__(self,uri,):
		self.uri = uri
		self.__checkFile()
		self.type = None
	# 检查文件
	def __checkFile(self):
		#检查文件类型
		if '.xlsx' in self.uri:
			self.fileType = 'excel2007'
		elif '.xls' in self.uri:
			self.fileType = 'excel2003'
		else:
			self.fileType = 'other'
		#检查文件是否存在
		self.fileActive = os.path.exists(self.uri)
	# 设置模式
	def __setModel(self,type):
		self.type = type
	# 判断是否阅读模式
	def __checkReadFile(self):
		if self.type is None or self.type=='read':
			self.__setModel('read')
		else:
			raise RuntimeError("对象正在进行写入操作,无法读取")

# excel 读取使用xlrd完成
# excel 阅读类
# 只负责读取工作
class excelReader:
	def __init__(self,uri):
		if os.path.exists(self.uri):
			self.file = xlrd.open_workbook(self.uri)
		else:
			raise RuntimeError('无法找到该文件: %s' % fileUri)
	
	# 返回所有工作表的名称
	def getAllSheets(self):
		return self.file.sheet_names()
	
	# 根据表格名称或编号获取表格，优先根据名称，
	# 当名称为空时再使用编号进行获取，编号默认是第一个表格的编号
	def setTable(self,tableName='',tableNo=0):
		if not tableName == '':
			table = self.file.sheet_by_name(tableName)
		else:
			table = sheet_by_index(tableNo)
		self.table = table
	def getMaxRow(self):
		return self.table.nrows
	def getData(self):
		data = []
		for i in range(0,getMaxRow()):
			line = table.row_values(i)
			data.append(line)
		return data
	def close(self):
		self.file.close()

class excelReader2007:
	def __init__(self,uri):
		if os.path.exists(self.uri):
			self.file = openpyxl.Workbook()
		else:
			raise RuntimeError('无法找到该文件: %s' % fileUri)
			
	def close(self):
		self.file.save(self.uri)	
			
			
			
			