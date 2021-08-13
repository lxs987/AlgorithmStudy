# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:53:17 2021

@author: lxs_9
"""

n = int(input())
for i in range(n):
    string = input()
    lst = list(string)
    sum=0
    
    for j in lst:
        if j == '(':
            sum+=1
        elif j ==')':
            sum-=1
        if sum<0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')

