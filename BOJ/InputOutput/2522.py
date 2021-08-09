# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:04:27 2021

@author: lxs_9
"""
n = int(input())
for i in range(1, n+1):
    answer = ' '*(n-i) + '*'*i
    print(answer)
for i in range(n-1, 0, -1):
    answer = ' '*(n-i) + '*'*i
    print(answer)