# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:28:58 2021

@author: lxs_9
"""
import sys
read = lambda : sys.stdin.readline().strip()

a, p = map(int, read().split())
d = []
while a not in d:
    d.append(a)
    a=sum([int(i)**p for i in str(a)])
print(d.index(a))
