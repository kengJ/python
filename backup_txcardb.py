from tool import dbHelper as dbHelper

def backup(dbname):
	host='192.168.117.85'
	username='sa'
	password='Csr.Donlim.Com'
	database=dbname
	try:
		db = dbHelper(host=host,username=username,password=password,database=database,type='mssql')
		print('%s 开始备份' % dbname)
		db.sql("select * into zlemployee_bak20190122 from zlemployee")
		db.sql("select * into Kq_Result_bak20190122 from Kq_Result")
		db.sql("select * into Kq_Source_bak2018 from Kq_Source where FDateTime > '2018-01-01'")
		db.sql("select * into Kq_Source_bak20190122 from Kq_Source")
		print('%s 备份完成' % dbname)
		db.close()
	except Exception as e:
		print('%s 链接失败' % dbname)

host='192.168.117.85'
username='sa'
password='Csr.Donlim.Com'
database='master'

db = dbHelper(host=host,username=username,password=password,database=database,type='mssql')

data = db.select("SELECT name FROM  master..sysdatabases where name like 'txcardb%'")

dbnames = list()
for name in data[1:]:
	dbnames.append(name[0])
for name in dbnames:
	backup(name)

# print(dbnames)


	