from flask import Flask
from flask import jsonify
import pymssql
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def GetConn(code):
    FuncName = {
        'ZK':pymssql.connect(host='192.168.117.85', user='sa', password='Csr.Donlim.Com', database='zkeco_db'),
        'WK':pymssql.connect(host='192.168.117.21', user='pdfadmin', password='123456789', database='PdfControl'),
        'TX':pymssql.connect(host='192.168.117.20\\tong', user='tx_app', password='app#%(app23', database='TxCard'),
        'BG':pymssql.connect(host='192.168.117.223', user='Reader', password='Reader123', database='EipMail')
    }
    return FuncName.get(code)

def SelectZK(type,value):
    conn = GetConn('ZK')
    cur = conn.cursor()
    sql='''
    select a.code,a.name,a.deptname,a.ip,a.mac,a.supplier,
    case when (a.buydate is null or a.buydate='') then CONVERT(varchar(100),b.create_time, 25) 
    else CONVERT(varchar(100),a.buydate, 25) end,
    a.guarantee,a.installation,a.ysbill,a.rdbill,CONVERT(varchar(100), b.last_activity, 25)
    from iclockmessage a
    left join iclock b on a.name = b.alias
    '''
    if len(str(value))>0:
        if type =='code':
            print(type)
            sql= sql+"where a.code ='"+value+"'"
        elif type is 'name':
            sql = sql + "where a.name ='" + value + "'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def SelectWK(value):
    conn = GetConn('WK')
    cur = conn.cursor()
    sql = '''
        SELECT CASE WHEN A.PERSON_NO IS NULL THEN B.USERNO END,
        PERSON_NAME,USERPWD,USERADMIN,CONVERT(varchar(100), MODIFYDATE, 25),CATALOGname,
        CASE WHEN RW_LEVEL=0 THEN '查看' ELSE CASE WHEN RW_LEVEL=1 THEN '保存/打印' ELSE '' END END
        FROM UserInfo B
        LEFT JOIN ControlByPerson A  ON A.PERSON_NO = B.USERNO

       '''
    if len(str(value)) > 0:
        sql = sql + "WHERE B.USERNO='"+value+"'"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

@app.route('/')
def index():
    return 'index'

@app.route('/getzkdata/<type>/<value>')
def hello_world(type,value=None):
    resp = jsonify({'error': False})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    data = list()
    indexkey = 0
    for message in SelectZK(type,value):
        data.append({'key':indexkey,'code':message[0],'name':message[1],'dept':message[2],'ip':message[3],
                     'mac':message[4],'supplier':message[5],'buydate':message[6],'guarantee':message[7],
                     'installation':message[8],'ysbill':message[9],'rdbill':message[10],'synctime':message[11]})
        indexkey = indexkey+1
    return jsonify(data)
@app.route('/getzkdata')
def getzkdata():
    resp = jsonify({'error': False})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    data = list()
    indexkey = 0
    for message in SelectZK(None, None):
        data.append({'key': indexkey, 'code': message[0], 'name': message[1], 'dept': message[2], 'ip': message[3],
                     'mac': message[4], 'supplier': message[5], 'buydate': message[6], 'guarantee': message[7],
                     'installation': message[8], 'ysbill': message[9], 'rdbill': message[10], 'synctime': message[11]})
        indexkey = indexkey + 1
    return jsonify(data)
@app.route('/getwkdata/<value>')
def GetWKData(value):
    resp = jsonify({'error': False})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    data = list()
    indexkey = 0
    for message in SelectWK(value):
        data.append({'key': indexkey, 'code': message[0], 'name': message[1], 'password': message[2], 'useradmin': message[3],
                     'modifydate': message[4],'filename':message[5],'filelevel':message[6]})
        indexkey = indexkey + 1
    return jsonify(data)

@app.route('/AddWKUser/<value>')
def AddWKUser(value):
    conn = GetConn('WK')
    cur = conn.cursor()
    sql = "SELECT * FROM UserInfo WHERE USERNO= '"+value+"'"
    cur.execute(sql)
    data = cur.fetchall()

    if len(data)>0:
        return jsonify([{'message':'已存在账号'}])
        cur.close()
        conn.close()
    else:
        sql = "insert into UserInfo (UserNo,UserPWD,modifydate,ifmodify)values ('"+value+"','"+value+"',getdate(),1)"
        cur.execute(sql)
        conn.commit()
        cur.execute("SELECT * FROM UserInfo WHERE USERNO= '" + value + "'")
        data = cur.fetchall()
        if len(data)>0:
            return jsonify([{'message': '新增成功'}])
        else:
            return jsonify([{'message': '插入数据失败'}])

@app.route('/DelWKUser/<value>')
def DelWKUser(value):
    conn = GetConn('WK')
    cur = conn.cursor()
    sql = "SELECT * FROM UserInfo WHERE USERNO= '"+value+"'"
    cur.execute(sql)
    data = cur.fetchall()

    if len(data)>0:
        if(len(data)>1):
            return jsonify([{'message':'存在超过一个账号'}])
        cur.execute("DELETE FROM UserInfo WHERE USERNO='"+value+"'")
        conn.commit()
        cur.close()
        conn.close()
        return jsonify([{'message':'账号'+value+'已删除'}])
    else:
        cur.close()
        conn.close()
        return jsonify([{'message': '不存在此账号'}])

@app.route('/ChangeWKUserPassword/<userno>/<newpassword>')
def ChangeWKUserPassword(userno,newpassword):
    conn = GetConn('WK')
    cur = conn.cursor()
    sql = "SELECT * FROM UserInfo WHERE USERNO= '"+userno+"'"
    cur.execute(sql)
    data = cur.fetchall()

    if len(data)>0:
        if(len(data)>1):
            return jsonify([{'message':'存在超过一个账号'}])
        cur.execute("UPDATE UserInfo SET userpwd ='"+newpassword+"' WHERE USERNO='"+userno+"'")
        conn.commit()
        cur.close()
        conn.close()
        return jsonify([{'message':'账号'+userno+'密码已更新为'+newpassword}])
    else:
        cur.close()
        conn.close()
        return jsonify([{'message': '不存在此账号'}])

@app.route('/GetXF')
def GetXF():
    conn = GetConn('TX')
    cur = conn.cursor()
    sql = '''
    select jh,ip,bz,zt,CONVERT(varchar(50),datetime,25),
    sd1,sd2,sd3,sd4,sd5,sd6,sd7,sd8,
    je1,je2,je3,je4,je5,je6,je7,je8 
    from jocat_jhsz
    '''
    cur.execute(sql)
    data = cur.fetchall()
    indexkey = 0
    results = list()
    if len(data)>0:
        for line in data:
            results.append({'key':indexkey,'code':line[0],'ip':line[1],'name':line[2],'zt':line[3],'datetime':line[4]})
            indexkey = indexkey+1
        cur.close()
        conn.close()
        return jsonify(results)
    else:
        return jsonify([])
#GetXFByJh
@app.route('/GetXFByJh/<code>')
def GetXFByJh(code):
    conn = GetConn('TX')
    cur = conn.cursor()
    sql = '''
    select jh,ip,bz,zt,CONVERT(varchar(50),datetime,25),
    sd1,sd2,sd3,sd4,sd5,sd6,sd7,sd8,
    je1,je2,je3,je4,je5,je6,je7,je8 
    from jocat_jhsz
    '''
    if len(code)>0:
        sql = sql + "where jh = '"+ code +"'"
    cur.execute(sql)
    data = cur.fetchall()
    indexkey = 0
    results = list()
    if len(data)>0:
        for line in data:
            results.append({'key':indexkey,'code':line[0],'ip':line[1],'name':line[2],'zt':line[3],'datetime':line[4]})
            indexkey = indexkey+1
        cur.close()
        conn.close()
        return jsonify(results)
    else:
        return jsonify([])

#根据工号查询催办
@app.route('/GetCBByCode/<code>')
def GetCBByCode(code):

    conn = GetConn('TX')
    cur = conn.cursor()
    sql = "select name from ZlEmployee where code = '"+code +"'"
    cur.execute(sql)
    data = cur.fetchall()
    name = data[0][0]
    cur.close()
    conn.close()

    conn = GetConn('BG')
    cur = conn.cursor()
    sql = '''
    select account,address,systemname,mailsubject,mailbody,url from V_EipMail 
    '''
    if len(code)>0:
        sql = sql + "where Account = '"+ code +"'"
    cur.execute(sql)
    data = cur.fetchall()
    indexkey = 0
    results = list()
    if len(data)>0:
        for line in data:
            system = ''
            if '/' in line[2]:
                system = line[2][0:line[2].find('/')-1]
            else:
                system = line[2]
            title = ''
            if "待办" in line[3]:
                results.append({'key':indexkey,'code':line[0],'name':name,'system':system,'title':line[3],'body':line[4],'url':line[5]})
                indexkey = indexkey+1
        cur.close()
        conn.close()
        return jsonify(results)
    else:
        return jsonify([])

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run()
