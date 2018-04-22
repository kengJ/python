import zipfile
'''
linux 压缩命令 zip -q -r -P password zipname filename

kail 字典
/usr/share/wordlist
/usr/share/wfuzz/wordlist
/usr/share/seclists
'''

zFile = zipfile.ZipFile("test.zip")
try:
    zFile.extractall(pwd="1234561")
except Exception as e:
    print(e)