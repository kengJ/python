import tool.basic as basic
from tool import dbHelper as dbHelper
import time,datetime

def getdata(start,end):
	host='192.168.117.20\\tong'
	username='tx_app'
	password='app#%(app23'
	database='txcard'
	mssql = dbHelper(host=host,username=username,password=password,database=database,type='mssql')
	#mssql = basic.db(host,username,password,database)

	sql = """
	select id,workno,workid,name,data_datetime,dept,longname,zhiji,zwname,入职日期 ,tt from(  
		SELECT *,ROW_NUMBER() OVER(partition by WORKNO,Convert(char(11),DATA_DATETIME,120) ORDER BY Convert(char(11),DATA_DATETIME,120))tt  
		FROM (  SELECT AT.ID,DE.DEVNAME,WORKNO,WORKID,ZE.NAME,AT.Data_datetime,  ZE.Dept,ZD.LongName,ZE.ZHIJI,ZW.NAME AS ZWNAME,ze.PyDate as 入职日期  
			FROM Attend_Data AT  LEFT JOIN ZlEmployee ze (NOLOCK) ON AT.WorkNo=ZE.CODE   
			LEFT JOIN ZlDept zd ON ZE.Dept=ZD.Code   
			LEFT JOIN E_ZHIWU ZW ON ZE.ZHIWU=ZW.CODE   
			LEFT JOIN (SELECT ID ,DEVNAME FROM Attend_Devices UNION SELECT clock_id,CLOCK_NAME  FROM ICCO_Clockskq   UNION selEct 62,'总部车库'  UNION selEct 10,'轴加工厂'  UNION selEct 12,'一分公司'    ) DE ON AT.ID=DE.ID  
			WHERE Data_datetime BETWEEN DATEADD(mi,1180, CONVERT(VARCHAR(11),Data_datetime,120)) AND DATEADD(mi,1439, CONVERT(VARCHAR(11),Data_datetime,120))  
			AND ISNULL(WORKNO,'')<>'' AND AT.ID NOT IN (SELECT ID FROM Attend_Devices (nolock) 
			WHERE isnull(DormCode,'')<>'' OR STATE=0 UNION SELECT clock_id FROM ICCO_Clockskq  where isnull(dept,'') <>''  
			UNION SELECT '6050')  AND STATE=0  UNION  SELECT MACHNO,devname,ZE.Code,ZE.CardNo,ZE.[Name],KQ.FDateTime,ZE.Dept,ZD.LongName,ZE.ZHIJI,ZW.NAME,ze.PyDate as 入职日期    FROM KQ_SOURCE KQ LEFT JOIN ZlEmployee ze (NOLOCK)ON KQ.EmpID=ZE.ID LEFT JOIN ZlDept zd ON ZE.DEPT=ZD.Code   LEFT JOIN E_ZHIWU ZW ON ZE.ZHIWU=ZW.CODE LEFT JOIN (SELECT ID ,DEVNAME FROM Attend_Devices UNION SELECT clock_id,CLOCK_NAME  FROM ICCO_Clockskq     UNION selEct 62,'总部车库'  UNION selEct 10,'轴加工厂'  UNION selEct 12,'一分公司'  ) DE ON kq.MachNo=DE.ID   WHERE FDateTime BETWEEN  DATEADD(mi,1180, CONVERT(VARCHAR(11),FDateTime,120)) AND    DATEADD(mi,1439, CONVERT(VARCHAR(11),FDateTime,120))   AND STATE=0  ) a WHERE CONVERT(VARCHAR(11),Data_datetime,120) BETWEEN '"""+start+"""' AND '"""+end+"""' and a.ID not in(select Clock_id  from ICCO_Clockskq  where (departstext=1) or (Clock_name  like '%闸%' or Clock_name like '%培训%' or Clock_name like '%门禁%') ) and a.Dept like '0106'+'%'  ) a where tt=1 ORDER BY dept,Data_datetime 
	"""

	data = mssql.select(sql)
	outputData = []
	for line in data[1:]:
		clock = line[0].rstrip()
		code = line[1].rstrip()
		if line[2]==None:
			cardno = ''
		else:
			cardno = line[2].rstrip()
		name = line[3].rstrip()
		checktime = line[4].strftime("%Y-%m-%d %H:%M:%S")
		deptid = line[5]
		dept = line[6]
		zhiji = line[7].rstrip()
		if line[8]==None:
			zhiwu = ''
		else:
			zhiwu = line[8].rstrip()
		pydate = line[9].strftime("%Y-%m-%d")
		outputData.append([clock,code,cardno,name,checktime,deptid,dept,zhiji,zhiwu,pydate])
	return outputData

try:
	# data = [[1,2,3],[4,5,6]]
	excel = basic.excel2007('./test123.xlsx')
	excel.addSheet('12')
	outputData = getdata('2018-12-21','2018-12-31 23:59:59')
	excel.writeData(outputData)
	excel.save()
except Exception as e:
	print(e)
