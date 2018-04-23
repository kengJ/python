import socket
import platform#获取系统底层信息
import configparser#处理配置文件
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
