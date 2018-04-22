import os
root = 'D:\\TextData\\'
list  = os.listdir(root)
# print(list)
# path = os.path.join(rootdir,list[i])
datafile = open(os.path.join(root,'data.txt'),'a+')
for file in list:
	if os.path.isfile(os.path.join(root,file)):
		print(os.path.join(root,file))
		datafile.write(open(os.path.join(root,file),'r').read())
datafile.close()
input('输入任何关键字结束')
exit()