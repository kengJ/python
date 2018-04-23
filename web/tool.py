import socket
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