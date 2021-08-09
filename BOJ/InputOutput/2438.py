# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:31:27 2021

@author: lxs_9
"""
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print('*',end='')
    print()