from prettytable import PrettyTable
# 格式化 输出
# setting['float']=='left' 字体向左对齐
def formatTable(data,title,setting={}):
	x = PrettyTable(title)
	x.padding_width = 1
	if len(setting)>0:
		if setting['float'] == 'left':
			x.align = 'l'
	if len(title) == len(data[0]):
		for line in data:
			x.add_row(line)
	else:
		for line in data:
			lineData = []
			for index in range(0,int(len(title))-1):
				lineData.append(line[index])
			x.add_row(lineData)
	print(x)