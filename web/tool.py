import socket
import platform#获取系统底层信息
import configparser#处理配置文件
from flask import request
#返回当前用户IP
def getUserIp(request):
    return request.remote_addr
def isPost(request):
    return request.method == 'POST'
#获取本机IP
def getHostIpAndHostName():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print('hostname is %s ip is %s' % (hostname,ip))

#获取系统信息
def getSystemMessage():
    Framework = platform.architecture()[0]#架构类型
    System = platform.system()#系统名称
    System = 'Mac' if System == 'Darwin' else System
    Details = platform.version()#系统版本
    CPU = platform.machine()#CPU平台
    LinuxVersion = platform.dist()#linux版本
    LinuxVersion = '' if 'Linux' not in System else '%s %s' % (LinuxVersion[0],LinuxVersion[1])
    ComputerName = platform.node()#主机名
    return {'Framework':Framework,'System':System,'Details':Details,'CPU':CPU,'LinuxVersion':LinuxVersion,'ComputerName':ComputerName}

#获取请求
def getPath():
    return request.path

#处理请求
def runAction(path):
    if '/' in path[1:]:
        className = path[1:path.find('/',1)]
        funcName = path[path.find('/',1)+1:]
        return className+'().'+funcName+'()'
    elif len(path)==1:
        return 'index()'
    else:
        return path[1:]+'()'

#处理配置文件

#整域读取配置
def getConf(fileurl,sectionname):
    conf = configparser.ConfigParser()
    conf.read(fileurl)
    return conf.items(sectionname)

#整域写入配置
def setConf(fileurl,sectionname,data):
    conf = configparser.ConfigParser()
    conf.add_section(sectionname)
    for key in data.keys():
        conf.set(key,data[key])
    with open(fileurl, 'w') as fw:
        conf.write(fw)

class RequestTool:
    request = None
    def __init__(self,request):
        self.request = request
    #获取客户端Ip
    def getClineIp(self):
        return request.remote_addr
    #获取请求信息
    def getMessage(self,type):
        result = None
        type = type.lower() 
        if type == 'method':
            result = self.request.method
        elif type == 'host':
            request = self.request.host
        elif type == 'path':
            result = self.request.path
        elif type == 'headers':
            result = self.request.headers
        return result