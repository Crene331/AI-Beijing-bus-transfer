# -*- encoding=utf-8 -*-


from All.Heap import MinHeap, emptyHeap, initHeap, topHeap, decHeap, Member
from All.Var import MAX


def dijkstra(station_dict, start, end):
    heapsize = len(station_dict)
    minheap = MinHeap(heapsize)
    members = []
    ans = {}
    for station_name in station_dict:
        station = station_dict[station_name]
        member = Member(station_name, MAX)
        if station_name == start:
            member.cost = 0
        members.append(member)
    minheap.setData(members)
    initHeap(minheap)

    while not emptyHeap(minheap):
        mem = topHeap(minheap)
        if mem.station_name == end:
            ans,mincost = mem.displayPath(mem.cost)
            continue
        station = station_dict[mem.station_name]
        for neibor in station.getNeibors():
            newcost = mem.cost + station.getNeiborWeight(neibor)
            decHeap(minheap, neibor, newcost, mem)

    return ans,mincost
