# -*- coding: utf-8 -*-
import urllib,re,json

def checkSelfIp():
    url = "http://1212.ip138.com/ic.asp"
    html = urllib.urlopen(url).read().decode('gbk')
    # print html
    ip = re.findall('([1-9]{1,}[\.]{1}[1-9]{1,}[\.]{1}[1-9]{1,}[\.]{1}[1-9]{1,})',html)
    print u"你当前的公网ip:"+ip[0]

def GetHtmlIp(url):
    checkSelfIp()
    if url!=None:
        host = "http://site.ip138.com/domain/read.do?domain="+url
        html = json.loads(urllib.urlopen(host).read().decode('gbk'))
        print"域名:"+url+"解析"
        for d in html['data']:
            ip = d['ip']
            sign = d['sign']
            address = urllib.urlopen("http://api.ip138.com/query/?ip="+ip+"&oid=50&mid=65575&datatype=jsonp&sign="+d['sign']).read()
            address = json.loads(address)
            str = ""
            for a in address["data"]:
                if a.strip():
                    str += a + ","
            print ip+"  "+str
    else:
        print u"url不能为空"

GetHtmlIp("baidu.com")