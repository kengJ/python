# -*- coding: utf-8 -*-
import os

file = open('readData.txt','r').readlines()
data = ''
for f in file:
	data+=f[0:4]+"+"+f[5:11]+"+0+"+f[12:16]+"-"+f[16:18]+"-"+f[18:20]+" "+f[20:22]+":"+f[22:24]+":"+f[24:26]+"\n"

open("writeData.txt",'w').write(data)