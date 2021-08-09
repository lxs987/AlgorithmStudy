# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 22:56:01 2021

@author: lxs_9
"""
# import sys
# n = int(sys.stdin.readline())
# nlist = [0]*100000
# for i in range(n):
#     nlist[int(sys.stdin.readline())]+=1
# result = sorted(nlist.items(), key=lambda x: (-x[1], x[0]))
# print(result[0][0])

import sys
n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(dic[0][0])
