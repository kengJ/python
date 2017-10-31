import py3.comm.comm as comm

# print(open('E:/python/py3/test.txt','r').read())
#
# filetool = comm.FileTool()
# print(filetool.readAll('E:/python/py3/test.txt'))
# comm.getSysName()
# comm.getSysDetialMessage()
path=comm.getPath()
# print(path.keys())
for key in path.keys():
    print(key+":"+str(path[key]))
