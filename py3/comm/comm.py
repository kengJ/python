import os

# 文件处理
class FileTool:
    def __init__(self):
        pass
    def readAllFor(self,file):
        text = ''
        with file as f:
            text+=f.read()
        return text
    def readAll(self,fileUrl):
        file = open(fileUrl,'r')
        return self.readAllFor(file)
    def readLines(self,file):
        return file.readlines()
    def writeFile(self,fileUrl,message):
        with open(fileUrl,'w') as file:
            file.write(message)


class osTool:
    def __init__(self):
        pass
    def getSysName(self):
        osname = os.name
        if osname == 'nt':
            print('windows')
        elif osname == 'posix':
            print('linux')
    # linux生效
    def getSysDetialMessage(self):
        print(os.uname())
    # 获取系统变量 path
    def getPath(self):
        return os.environ
    #
    def getSysVal(self,name):
        return os.getenv(name)
