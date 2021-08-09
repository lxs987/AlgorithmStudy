# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:49:27 2021

@author: lxs_9
"""
n = int(input())
lst2 = []
for i in range(n):
    n1, n2 = map(int, input().split())
    lst=[n1, n2]
    lst2.append(lst)
lst2 = sorted(lst2, key=lambda x : x[0])
lst2 = sorted(lst2, key=lambda x : x[1])
for i in range(n):
    print(*lst2[i], sep = ' ')