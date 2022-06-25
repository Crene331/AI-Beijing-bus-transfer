#-*- encoding=utf-8 -*-


from All.Station import Station
from All.Line import Line
from All.Selection import Selection
from All.Var import MAX,min_total_cost,best_exchange_way

def create_Intersection_Matrix(line_dict):#判断两个线路有无交集，线路矩阵
	lineSize = len(line_dict)
	lineNames = sorted(line_dict.keys())
	#matrix dict
	intersectionMatrix={}.fromkeys(lineNames,None)
	for linename in intersectionMatrix:
		intersectionMatrix[linename]={}.fromkeys(lineNames,0)

	for linename_i in lineNames:
		for linename_j in intersectionMatrix[linename_i]:			
			mainline,otherline = line_dict[linename_i],line_dict[linename_j]
			if linename_i!=linename_j and mainline.intersectWith(otherline):
				intersectionMatrix[linename_i][linename_j]=1

	return intersectionMatrix

def printerAnswer(answer,step,mayex,line_dict,station_dict):
	global min_total_cost,best_exchange_way
	global ans1,jilu
	ans1 = []
	jilu= []
	total_cost = 0
	retString = ''
	for i,linename in enumerate(mayex):
		source_st,dest_st = answer[i:i+2]
		line = line_dict[linename]
		subcost,subString,ans,lineString = line.getRouteinLine(source_st,dest_st,station_dict)
		total_cost += subcost
		retString += subString
		ans1 =ans1 + ans
		jilu = jilu + list(lineString)
		jilu = jilu + list(' ')
	if min_total_cost > total_cost:
		best_exchange_way = retString[:-1]
		min_total_cost = total_cost

def arrangeAll(solutions,answer,step,bestExNum,mayex,line_dict,station_dict):
	global ans1,jilu
	if step==bestExNum:
		printerAnswer(answer,step,mayex,line_dict,station_dict)
		return
	for next in solutions[step]:
		answer[step]=next
		arrangeAll(solutions,answer,step+1,bestExNum,mayex,line_dict,station_dict)



def bestExchange(mayExchanges,line_dict,bestExNum,start,end,station_dict):
	global min_total_cost,best_exchange_way,ans1,jilu
	min_total_cost,best_exchange_way = MAX,None
	for mayex in mayExchanges:
		mySolutions = [[start]]
		exSize = len(mayex)
		for i in range(exSize-1):
			curlineName,nextlineName = mayex[i:i+2]
			curLine = line_dict[curlineName]
			nextLine = line_dict[nextlineName]
			mySolutions.append(curLine.getExstations(nextLine))
		mySolutions.append([end])
		answer = [None for x in range(bestExNum+2)]
		arrangeAll(mySolutions,answer,0,bestExNum+2,mayex,line_dict,station_dict)
	print(best_exchange_way)
	print ('用时%d分钟' % min_total_cost)
	return ans1,jilu,min_total_cost

def leastexchange(intersectionMatrix,line_dict,station_dict,start,end):
	starts_line = []
	lineNames = sorted(line_dict.keys())
	line_size = len(intersectionMatrix)
	for line_name in lineNames:#记录该站点在多少条线路上
		line = line_dict[line_name]
		if line.inLine(start):
			sel = Selection(line_name,0)
			starts_line.append(sel)
	queue = []
	queue.extend(starts_line)

	minExchange = MAX
	mayExchanges=[]
	num = 0

	while queue:
		cur = queue.pop(0)#可选的路
		line_name = cur.station_name
		if cur.height > minExchange:
			break
		if line_dict[line_name].inLine(end) and cur.height <= minExchange:#终点线路是否存在
			minExchange = cur.height
			mayExchanges.append(cur.displayPath())#存的线路
			continue
		for neibor in lineNames:
			if intersectionMatrix[cur.station_name][neibor] and not cur.inPath(neibor):
				sel = Selection(neibor,cur.height+1,parent=cur)
				queue.append(sel)
	bestExNum = minExchange
	ans1,jilu,min_total_cost = bestExchange(mayExchanges,line_dict,bestExNum,start,end,station_dict)
	return ans1,jilu,min_total_cost
