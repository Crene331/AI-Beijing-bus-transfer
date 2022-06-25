#-*- encoding=utf-8 -*-

from All.Station import Station
from All.Line import Line
from All.Getdata import loadData

import All.Dijk as DIJKSTRA
import All.Mintransfer as TRANSFER
import All.new as new

def create_subway_map(lines_data,weights):
	station_dict={}
	line_dict={}
	for line_name in lines_data:#初始化创建线路类和车站类
		line = lines_data[line_name]
		subline = Line(line_name)
		for station_name in line:
			subline.addStation(station_name)
			if station_name not in station_dict:			
				station_dict[station_name]=Station(station_name)
		line_dict[line_name] = subline
	for line_name in lines_data:#记录邻站
		line = lines_data[line_name]
		line_length=len(line)
		for i in range(line_length-1):
			mainstation,neiborstation=line[i:i+2]
			station_dict[mainstation].addNeibor(neiborstation,timecost=weights[neiborstation])#weights[neiborstation])
		for i in range(line_length-1,0,-1):
			mainstation,neiborstation=line[i],line[i-1]
			station_dict[mainstation].addNeibor(neiborstation,timecost=weights[neiborstation])#weights[neiborstation])
	return station_dict,line_dict


if __name__ == '__main__':
	lines_data,weights = loadData()

	station_dict,line_dict=create_subway_map(lines_data,weights)
	


	start = input('出发点>>')#起点，数据类型string
	end = input('目的地>>')#终点，数据类型 string
	print ('******最少换乘******')
	intersectionMatrix=TRANSFER.create_Intersection_Matrix(line_dict)
	ans1,jilu,min_time1 = TRANSFER.leastexchange(intersectionMatrix,line_dict,station_dict,start,end)
	x = "=>".join(ans1)#这个是路径1的字符串
	time1 = str(min_time1)#这个是最短用时（如果你要加其他字符可以用‘balabala’+ str(min_time2)这样）
	transferJilu = "".join(jilu)#这个是换乘经过的交通路线字符串
	print ('******最少用时******')
	ans2,min_time2 = DIJKSTRA.dijkstra(station_dict,start,end)#一个字典
	y = "=>".join(ans2)#这个是路径2的字符串
	time2 = str(min_time2)#这是第二个路径最短用时（如果你要加其他字符可以用‘balabala’+ str(min_time2)这样）
'''	print(x)
	print(ans2)
	print ('******最少用时2******')
	BFS.breadfs(station_dict ,start ,end)
'''