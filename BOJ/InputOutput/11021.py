# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:07:14 2021

@author: lxs_9
"""
T = int(input())
for i in range(T):
    n1, n2 = map(int, input().split())
    print('Case #{0}: {1}'.format(i+1, n1+n2))