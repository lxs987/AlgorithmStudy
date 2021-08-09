# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:36:46 2021

@author: lxs_9
"""
n = int(input())
for i in range(1,n+1):
     print(" " * (n-i) + "* " * (i-1) + "*")