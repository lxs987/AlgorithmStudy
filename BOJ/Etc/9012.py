# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:53:17 2021

@author: lxs_9
"""
import sys
n = int(sys.stdin.readline())

for i in range(n):
    lst = []
    lst.append(sys.stdin.readline().rstrip().split())
    
    if lst[0]==')':
            print('NO')
            return 0
        
    for i in range(len(lst)):
        