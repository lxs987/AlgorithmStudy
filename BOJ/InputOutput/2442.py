# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:45:35 2021

@author: lxs_9
"""
n = int(input())

for i in range(1, n+1):
    answer = ' '*(n-i) + '*'*((2*i)-1)
    print(answer)