#返回当前用户IP
def getUserIp(request):
    return request.remote_addr
def isPost(request):
    return request.method == 'POST'