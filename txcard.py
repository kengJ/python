import tool
#from tool import *
#import tool.basic as basic
tool.dbHelper(type='sqlite',file='./db/demo.db')
print(dir(tool))
#sqlitedb = db(type='sqlite',file='./db/demo.db')
#db1 = Db.db(type='sqlite',file='./db/demo.db')
#print('connect success')
# import sqlite3
#conn = sqlite3.connect('./db/demo.db')
#print('connect success')
#cur = conn.cursor()
