from tool import dbHelper as dbHelper
from tool import dataHelper as dataHelper
from getpass import getpass as getpass

def test():
	db = dbHelper(type='sqlite',file='./db/system.db')
	# 获取表名
	data = db.select('SELECT name FROM sqlite_master WHERE type=\'table\'')
	for line in data:
		tbl_name = line[0]
	data = db.select("PRAGMA table_info({})".format(tbl_name))
	dataHelper.formatTable(data[1:],data[0],setting={'float':'left'})

def checkUser(username,password):
	db = dbHelper(type='sqlite',file='./db/system.db')
	tables = db.select('SELECT name FROM sqlite_master WHERE type=\'table\'') #获取所有的表名
	tablenames = []
	for line in tables[1:]:
		for value in line:
			tablenames.append(value)
	#print(tablenames)
	# 如果没有用户表创建用户表
	if not 'USER' in tablenames:
		print('创建user表')
		db.sql("""
		CREATE TABLE USER(
		ID INTEGER PRIMARY KEY AUTOINCREMENT,
		USERCODE VARCHAR(20) NOT NULL,
		USERNAME VARCHAR(50) NOT NULL,
		PASSWORD VARCHAR(100) NOT NULL,
		MEMO TEXT
		)
		""")
		print('写入管理员')
		db.sql("INSERT INTO USER (USERCODE,USERNAME,PASSWORD) VALUES ('admin','ADMIN','admin')")
	# 进行身份验证
	data = db.select("SELECT 1 FROM USER WHERE USERCODE='%s' and PASSWORD='%s'" % (username,password))[1:]
	#print(data)
	if data[0][0]==1:
		print('LOGIN SUCCESS')
	else:
		print('LOGIN FLAST')
def main():
	username = input('输入账号名:')
	password = getpass('请输入密码:')
	#print(password)
	checkUser(username,password)
if __name__ == '__main__':
	main()




