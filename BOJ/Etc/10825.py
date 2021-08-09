# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:42:58 2021

@author: lxs_9
"""
import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(member[i][0])