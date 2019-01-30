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

def test(xk,code):
	clocks = []	
	sql = """
	select distinct clock_id from ICCO_TaskCard where state=0 and down_flag = 1 and card_sn <> '' and join_id='%s' 
	"""
	clock_data = xk.select(sql % code)
	for line in clock_data[1:]:
		clocks.append((code,line[0]))
	sql = """
	insert into role (empid,clockid,state,createdate,updatedate) values (%s,%s,0,getdate(),getdate())
	"""
	xk.insertMany(sql,clocks)
	
	
	
xk = getdb()
sql = """
select distinct join_id from ICCO_TaskCard where state=0 and down_flag = 1 and card_sn <> '' order by join_id
"""
emp_data = xk.select(sql)
emps = list()
for line in emp_data[1:]:
	#emps.append(line[0])
	test(xk,line[0])


	