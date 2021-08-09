# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 11:31:32 2021

@author: lxs_9
"""
n = int(input())
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
    
lst = sorted(lst)
for i in range(n):
    print(lst[i])