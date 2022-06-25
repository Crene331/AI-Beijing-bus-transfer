#-*- encoding=utf-8 -*-

def loadData():
	files=['1.txt','13.txt','2.txt','5.txt','6.txt','8t.txt','cp.txt','fs.txt','yz.txt','10.txt','15.txt','4.txt','8.txt','9.txt','dx.txt','jc.txt','19.txt']
	lines_data={}
	weights={}	
	for filename in files:
		with open('data/%s' % filename,'r',encoding='utf-8') as file:
			line_name=file.readline()[:-1]#读取第一行，去掉换行符，得到线路名称
			lines_data[line_name]=[]#对该线路名创建列表
			for line in file:
				line = line.strip()#格式化
				lineAttr = line.split('\t')#制定字符tab隔开，隔开站名和距离（这里第一版没用上实际上，因为默认用不上）
				station_name, station_time = lineAttr[0],int(lineAttr[1])
				if station_name not in weights:
					weights[station_name] = station_time
				lines_data[line_name].append(station_name)
	return lines_data,weights #返回了一个记录站点的多维列表、每个站点用时