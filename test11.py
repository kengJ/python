# -*- coding: utf-8 -*-
# from com import *

# print("中文")
# test1()
# t = Test()
# print (t)
# t.test123()

# c = Code('gbk')
# print c.gbk('中文')
# b = Base()
# codes = b.getCode("test.txt")
text = ''
codes  = open('test.txt','r').readlines()
for code in codes:
	text+="'"+code.replace('      ',"").replace('\n',"")+"',"
	# print(code.replace('\n','')+',')
# print codes
print(text[:-1])