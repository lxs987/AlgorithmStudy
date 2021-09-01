# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:21:24 2021

@author: lxs_9
"""
import sys, bisect
op_lst = list(map(int, sys.stdin.readline().split())) # 집 개수, 공유기 개수 리스트
coord_lst = sorted([int(sys.stdin.readline()) for i in range(op_lst[0])]) # 좌표 리스트

start = 1 #최소 간격
end = max(coord_lst) - min(coord_lst) #최대 간격

while True:
    median = (start+end)//2
    # 단위 거리로 배치할 수 있는 공유기 수 구하기
    starter = coord_lst[0]
    starter_index = 0
    router_count = 0
    while starter_index<len(coord_lst):
        router_count+=1
        starter_index = bisect.bisect_left(coord_lst,coord_lst[starter_index]+median)

    if router_count < op_lst[1]:
        end = median - 1
    elif router_count >= op_lst[1]:
        start = median +1
    if median == end: # 더 이상 큰 단위 거리를 구할 수 없을 때
        print(median)
        break
