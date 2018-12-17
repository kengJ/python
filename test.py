import tool.base as basic


host='192.168.119.203'
username='sa'
password='donlim.com'
database='zkteco_database'

(conn,cur) = basic.conndb(host,username,password,database)
file =open('./input.txt','r').readlines()
codes = []
for code in file:
	codes.append(code.replace('\n',''))
subsql = "('"+"','".join(codes)+"')"

sql = """
	select rtrim(code),name,dept,'QS',0,getdate(),0 from [192.168.117.20\\tong].txcard.dbo.zlemployee a        
	where  a.state='0'         
	and a.cardno<>''  	
	and a.code in %s      
	and not exists(select RIGHT(code,6) from emp_sync c where  a.code=RIGHT(c.pin,6) and c.sync_flag=0 and c.deal_flag=0)     
	and not exists(select RIGHT(code,6) from userinfo d where  a.code=RIGHT(d.badgenumber,6))
	""" % subsql
data = basic.select(cur,sql)
if data == 	None:
	print("人员已同步")
else:
	basic.formatTable(data,['工号','姓名','部门编码','区域','指纹数','同步时间','待下载标记'])
	check = input('是否进行插入:')
	if check == 'y':
		basic.insert(cur,'insert into emp_sync (pin,name,deptcode,areacode,sync_flag,sync_time,deal_flag) ',data)

basic.connClose(conn)
input('输入任意键结束')