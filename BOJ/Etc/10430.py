# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 01:12:19 2021

@author: lxs_9
"""
import sys
A, B, C = map(int, sys.stdin.readline().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)
