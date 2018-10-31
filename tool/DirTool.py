import os

# 1.根据filepath遍历文件，输出文件列表
# 2.选择文件,返回文件的路径
def getFile(filepath):
    pathDir =  os.listdir(filepath)
    index = 1
    files = {}
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        if os.path.isfile(child):
            if index < 10:
                print('0%d. %s' % (index,allDir))
                files['0'+str(index)] = child
                index+=1
            else:
                print('%d. %s' % (index,allDir))
                files[str(index)] = child
                index+=1
    check = True
    fileIndex = input('请输入文件编号:')
    while check:
        if fileIndex in files:
            print('文件编号为:%s' % fileIndex)
            print('文件路径:%s' % files[fileIndex])
            check = False
        else:
            fileIndex = input('输入文件编号错误,请重新输入文件编号')
    return files[fileIndex]
