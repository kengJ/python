import xlsxwriter
#from tool import excelHelper as excelHelper
from tool import dbHelper as dbHelper

class dbmessage:
	host=''
	username=''
	password=''
	database=''
	
	def __init__(self,host,username,password,database):
		self.host=host
		self.username=username
		self.password=password
		self.database=database
	def getdb(self):
		db = dbHelper(host=self.host,username=self.username,password=self.password,database=self.database,type='mssql')
		return db

def getdb(type='xk'):
	if type=='tx':
		host = '192.168.117.20\\tong'
		username='tx_app'
		password='app#%(app23'
		database='txcard'
	elif type=='xk':
		host='192.168.119.205'
		username='sa'
		password='donlim.com'
		database='XK_LockServer'
	elif type=='zk':
		host='192.168.119.203'
		username='sa'
		password='donlim.com'
		database='zkteco_database'
	return dbmessage(host,username,password,database).getdb()

# 获取文档工号
def getcodes():
	file = open('code.txt','r').readlines()
	subsql = ""
	codes = []
	for code in file:
		codes.append(code.replace('\n',''))
	subsql = "('"+ "','".join(codes) +"')"
	return subsql

# 更新物理卡号
def check_sn():
	sql="""
	select * into #zlemp from [TXCARD].TXCARD.dbo.Zlemployee where code in (select code from Zlemployee)
UPDATE A SET  A.Card_Sn = B.CARD_SN
FROM Zlemployee A
LEFT JOIN #zlemp B ON A.CODE = B.CODE AND A.CARD_SN<>B.CARD_SN
WHERE B.CARD_SN IS NOT NULL
	"""
	room_db.sql(insert_sql)

# 按工号更新物理卡号
def update_cardsn_bycode(subsql):
	sql="""
	select * into #zlemp from [TXCARD].TXCARD.dbo.Zlemployee where code in (select code from Zlemployee)
UPDATE A SET  A.Card_Sn = B.CARD_SN
FROM Zlemployee A
LEFT JOIN #zlemp B ON A.CODE = B.CODE AND A.CARD_SN<>B.CARD_SN
WHERE B.CARD_SN IS NOT NULL AND A.CODE IN %s
	"""% subsql
	room_db.sql(sql)

class xk:
	def __init__(self,db):
		self.db = db
	# 增加门禁系统人员信息
	def addRoom_emp_old(self,subsql):
		sql="""
		insert into zlemployee (Code,Name,Dept,CardNo,Card_Sn,State,Pydate,Getcard)
		select rtrim(code),rtrim(name),dept,rtrim(cardno),card_sn,0,Pydate,1 
		FROM [TXCARD].[TXCARD].[dbo].[zlemployee] 
		where code not in (select code from zlemployee) and card_sn is not null and code in %s
		"""% subsql
		self.db.sql(sql)
	def addRoom_emp(self,subsql):
		#sql="""
		#insert into zlemployee (Code,Name,Dept,CardNo,Card_Sn,State,Pydate,Getcard)
		#select rtrim(code),rtrim(name),dept,rtrim(cardno),card_sn,0,Pydate,1 
		#from FROM [HR140].[HRMS].[dbo].[view_Hrms_TXZlEmployee] 
		#where code not in (select code from zlemployee) and card_sn is not null and code in %s
		#"""% subsql
		sql = """
		SELECT RTRIM(A.CODE),RTRIM(A.NAME),A.DEPT,RTRIM(B.CARDNO),A.CARD_SN,A.CARD_SN,0,A.PYDATE,1 
		FROM [HR140].[HRMS].[dbo].[view_Hrms_TXZlEmployee] A
		JOIN [TXCARD].[TXCARD].[dbo].ZLEMPLOYEE B ON A.CODE= B.CODE
		WHERE A.CODE NOT IN (SELECT CODE FROM ZLEMPLOYEE) AND 
		A.CARD_SN IS NOT NULL AND A.CODE IN %s
		"""% subsql
		self.db.sql(sql)
		
	#增加权限	
	def addRole(self,rooms,subsql):
		for value in rooms:
			insert_sql = """
		insert into ICCO_TaskCard (join_id,card_id,card_sn,clock_id,state,ope_date,user_name,door_val,depart_id) 
		select a.id,a.CardNo,a.card_sn,'%s' ,'0',getdate(),'admin','01020304',a.dept 
		from zlemployee a 
		where a.code in %s
		""" % (value,subsql)
			self.db.sql(insert_sql)
	def get_emp(self,subsql):
		sql = """
		select * from zlemployee where code in %s
		"""% subsql
		data = self.db.select(sql)
		for line in data[1:]:
			print(line)
	def update_emp_sn(self,code,sn):
		sql = """
		update zlemployee set card_sn='%s' where code = '%s'
		""" % (sn,code)
		self.db.sql(sql)
	def getroms(self):
		sql="""
		select Clock_Id from Clocks 
		"""
		data = self.db.select(sql)
		result = []
		for line in data[1:]:
			result.append(line[0])
		return result
	def update_emp_subsql(self,subsql):
		sql="""
			UPDATE A SET A.CARD_SN = B.CARD_SN
			FROM ZLEMPLOYEE A
			JOIN [HR140].[HRMS].[dbo].[view_Hrms_TXZlEmployee] B ON A.CODE = B.CODE
			WHERE A.CODE IN %s AND B.CARD_SN IS NOT NULL AND A.CARD_SN<>B.CARD_SN
		""" % subsql
		self.db.sql(sql)
	def update_emp_subsql_old(self,subsql):	
		sql="""
		UPDATE A SET A.CARD_SN = B.CARD_SN
		FROM ZLEMPLOYEE A
		JOIN [TXCARD].[TXCARD].[dbo].ZLEMPLOYEE B ON A.CODE= B.CODE
		WHERE A.CODE IN %s AND B.CARD_SN IS NOT NULL --AND A.CARD_SN<>B.CARD_SN
		""" % subsql
		self.db.sql(sql)
	def update_emp_subsql_old_all(self):	
		sql="""
		UPDATE A SET A.CARD_SN = B.CARD_SN
		FROM ZLEMPLOYEE A
		JOIN [TXCARD].[TXCARD].[dbo].ZLEMPLOYEE B ON A.CODE= B.CODE
		WHERE B.CARD_SN IS NOT NULL AND A.CARD_SN<>B.CARD_SN
		""" 
		self.db.sql(sql)
class zk:
	def __init__(self,db):
		self.db = db
	def update_dept_to_test(self,subsql):
		sql="""
			insert into emp_sync(pin,name,deptcode,areacode,sync_flag,sync_time,deal_flag,cardno)
			select rtrim(code),name,02,'','1',GETDATE(),0,card_sn
			from [192.168.117.20\\tong].txcard.dbo.zlemployee 
			where code in %s
		"""% subsql
		self.db.sql(sql)
	def update_dept(self,subsql):
		sql="""
			insert into emp_sync(pin,name,deptcode,areacode,sync_flag,sync_time,deal_flag,cardno)
			select rtrim(code),name,dept,'','1',GETDATE(),0,card_sn
			from [192.168.117.20\\tong].txcard.dbo.zlemployee 
			where code in %s
		"""% subsql
		db.sql(sql)
def test():
	rooms = ['9032','9033','9034','9035','9036','9037','9035']		
	subsql = getcodes() #获取工号并集成括号
	xk_obj = xk(db=getdb())
	#rooms = xk_obj.getroms()
	#xk_obj.addRole(rooms,subsql)
	xk_obj.addRoom_emp(subsql)
	xk_obj.update_emp_subsql(subsql)
	#xk_obj.addRole(rooms,subsql)

def test1(db,subsql):
	sql = """
	SELECT A.CODE,A.NAME,A.DEPT,B.LONGNAME FROM [TXCARD].[TXCARD].[dbo].ZLEMPLOYEE A LEFT JOIN [TXCARD].[TXCARD].[dbo].ZLDEPT B ON A.DEPT= B.CODE WHERE A.CODE IN %s AND A.CARD_SN IS NULL
	""" % subsql
	data = db.select(sql)
	
	
	excel =  xlsxwriter.Workbook('demo.xlsx')
	sheet = excel.add_worksheet('sheet1')
	i = 1
	for line in data[1:]:
		sheet.write_row('A'+str(i),line)
		i+=1
	#sheet.write_row('A1',data)
	excel.close()
	
	
#rooms = ['9008']
#file = open('./code.txt').readlines()
#print("','".join(value.replace('\n','') for value in file))	
subsql = getcodes() #获取工号并集成括号
xk_obj = xk(db=getdb())
xk_obj.addRoom_emp_old(subsql)
#xk_obj.update_emp_subsql_old(subsql)
#xk_obj.update_emp_subsql(subsql)
rooms = xk_obj.getroms()
#rooms=['9038']
xk_obj.addRole(rooms,subsql)
#test1(getdb(),subsql)

