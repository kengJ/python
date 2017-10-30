# 文件处理
class FileTool:
    fileUrl = None
    def __init__(self,fileUrl):
        self.fileUrl = fileUrl
    def openFile(self,fileUrl,model):
        self.file =  open(fileUrl,model)
    def readAll(self,fileUrl,model,isSetFile=True):
        # if isSetFile==False:
        return self.openFile(fileUrl,model).read()