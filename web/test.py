from flask import Flask
from flask import request
import platform
import tool
import beforeAction as BAction
import afterAction as AAction
import win_unicode_console

#show version
app = Flask(__name__)
homeIp = '192.168.1.107'
workIp = '127.0.0.1'
win_unicode_console.enable()#win10 bug

@app.route('/')
def index():
    #user_agent = request.headers.get('User-Agent')
    print(tool.getUserIp(request))
    return 'hello word'

#首次请求会触发     
# @app.before_first_request
# def before_first_request():
#     print('before_first_request')

@app.before_request
def before_request():
    BAction.main(request.path,None)

#@after_request 如果有异常抛出将不会被运行
#@teardown_request 即使有异常抛出也会被执行
#@app.after_request
# def after_request():
#     AAction.main(request.path,None)

@app.route('/test/bbb')
def test():
    return 'test'

@app.route('/test1')
def test1():
    tool.getHostIpAndHostName()
    return 'test1'

if __name__ == '__main__':
    app.run(host=workIp,port=8080,debug=True) 
    print("python version: %s" % platform.python_version())





