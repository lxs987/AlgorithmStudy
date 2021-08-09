# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:47:41 2021

@author: lxs_9
"""
import sys
n = int(sys.stdin.readline())
nlist = [0] * 10001
for i in range(n):
    nlist[int(sys.stdin.readline())] += 1
for i in range(10001):
    if nlist[i] != 0:
        for j in range(nlist[i]):
            print(i)
            