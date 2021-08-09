# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:36:04 2021

@author: lxs_9
"""
n = int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()