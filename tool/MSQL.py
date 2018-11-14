import pymssql
import xlwt

def createConn(ip,username,password,dbname):
    conn = pymssql.connect(host="192.168.117.35",user="conn",password="nnoc",database="adirectory",charset="utf8")
    cur = conn.cursor()
    if not cur:
        raise (NameError,"数据库连接失败")
        return cur
    else:
        return None
    
def query(cur,sql):
    cur.execute(sql)
    return cur.fetchall()

def formatData(data):
    result = {}
    for line in data:
        index = 0
        dataArray = []
        for value in line:
            dataArray[index] = value
            index += 1
        result[dataArray[0]] = dataArray
    return result


