# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:59:16 2021

@author: lxs_9
"""
n = int(input())
for i in range(1, n+1):
    answer = '*'*i + ' '*((n-i)*2) + '*'*i
    print(answer)
for i in range(n-1, 0, -1):
    answer = '*'*i + ' '*((n-i)*2) + '*'*i
    print(answer)