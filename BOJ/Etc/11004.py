# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:48:22 2021

@author: lxs_9
"""
import sys
n, k = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))
nlist.sort()
print(nlist[k-1])
