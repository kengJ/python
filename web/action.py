import tool

class Test:
    def Index(self):
        return 'path is %s' % 'test index'

def main(path):
    return eval(tool.runAction(path))
    #return tool.runAction(this,path)