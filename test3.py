from tool import osHelper as osHelper
from tool import dbHelper as dbHelper
import pymssql
#print(dir(osHelper))

files = osHelper.listDri('C:\\Users\\heyanzhu\\Desktop\\产品目录',setting={'print':'off'})

db = dbHelper(host='192.168.117.95',username='sa',password='aps2015..',database='IMS',type='mssql')
#cur = conn.cursor()
# ReportExport20181224

fileData = []
no = 1
for file in files:
	if len(str(no))==1:
		textno='00'+str(no)
	elif len(str(no))==2:
		textno='0'+str(no)
	else:
		textno=str(no)
	fileData.append(('R20181224'+textno,'R20171109010',file.split('.')[0],'|/updateload/all/20181224/产品目录/'+file))
	no+=1

#cur = db.getcur()
db.insertMany("insert into ReportExport20181224 (reportid,reporttypeid,reporttitle,test2) values (%s,%s,%s,%s)",fileData)
#conn.commit()