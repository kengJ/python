# -*- coding: utf-8 -*-
import urllib,re,json

def checkSelfIp():
    html = urllib.urlopen("http://1212.ip138.com/ic.asp").read().decode('gbk')
    return u"你当前的公网ip:"+(re.findall('([1-9]{1,}[\.]{1}[1-9]{1,}[\.]{1}[1-9]{1,}[\.]{1}[1-9]{1,})',html))[0]+"\n"

def GetHtmlIp(url):
    if not url.split():return u"url不能为空"
    html = json.loads(urllib.urlopen("http://site.ip138.com/domain/read.do?domain="+url).read().decode('gbk'))
    str = u"域名:" + url + u"解析\n"
    for d in html['data']:
        address = json.loads(urllib.urlopen("http://api.ip138.com/query/?ip="+d['ip']+"&oid=50&mid=65575&datatype=jsonp&sign="+d['sign']).read())
        add = d['ip']+"  "
        for a in address["data"]:
            if a.strip():add += a + ","
        str+=add+"\n"
    return str

print checkSelfIp()+GetHtmlIp("baidu.com")