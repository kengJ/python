import tool
from flask import request
class Test:
    def Index(self):
        return 'path is %s' % 'test index'
    def TestRequest(self):
        return 'headers data is %s' % type(tool.RequestTool(request).getMessage('headers'))

def index():
    return 'index'

def main(path):
    return eval(tool.runAction(path))
    #return tool.runAction(this,path)