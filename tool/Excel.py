import xlwt,xlrd # excel 写入
import openpyxl # excel 2007


# excel 读取使用xlrd完成
# excel 阅读类
# 只负责读取工作
class excelread:
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


		