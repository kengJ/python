import win_unicode_console

win_unicode_console.enable()#win10 bug

def getData(filename):
    file1 = open(filename,'r')
    data = {}
    for x in file1.read().split(":"):
        x = x.replace('\n','')
        if '(' in x and len(x)>3:
            data[x[1:x.find(')')]] = x[x.find(')')+1:]
    return data

filename1 = 'test.txt'
filename2 = 'test1.txt'
data1 = getData(filename1)
data2 = getData(filename2)
for key in data1.keys():
    if not data1[key] == data2[key]:
        print('[+] key => '+ key + ' data1 => ' + data1[key] + ' data2 => ' + data2[key])
        