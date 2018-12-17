import os
import zipfile

def backupToZip(folder):
	folder = os.path.abspath(folder)
	number = 1
	while True:
		zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'
		if not os.path.exists(zipFileName):
			break
		number+=1
	print('创建文件%s' % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName,'w')
	
	for foldername ,subfolders,filenames in os.walk(folder):
		print('添加文件 %s' % (foldername))
		backupZip.write(foldername)
		for filename in filenames:
			if filename.startswith(os.path.basename(folder)+'_') and filename.endswith('.zip'):
				continue 
			backupZip.write(os.path.join(foldername,filename))
	backupZip.close()
	print('结束')