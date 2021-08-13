# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 00:59:13 2021

@author: lxs_9
"""
import sys
s = sys.stdin.readline().strip()
lst = [0]*26
for i in s:
    lst[ord(i)-97]+=1
for i in lst:
    print(i, end = ' ')
