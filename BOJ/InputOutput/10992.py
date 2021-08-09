# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:18:53 2021

@author: lxs_9
"""
n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print(" " * (n-i) + "*" * (2*i-1))
    else:
        print(" " * (n-i) + "*" + " " * (2*(i-1)-1) + "*")