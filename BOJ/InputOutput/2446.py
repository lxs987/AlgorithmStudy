# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:10:33 2021

@author: lxs_9
"""
n = int(input())
for i in range(n, 0, -1):
    answer = ' '*(n-i) + '*'*(i*2-1)
    print(answer)
for i in range(2, n+1):
    answer = ' '*(n-i) + '*'*(i*2-1)
    print(answer)