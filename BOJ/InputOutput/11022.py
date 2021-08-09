# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:15:59 2021

@author: lxs_9
"""
T = int(input())
for i in range(T):
    n1, n2 = map(int, input().split())
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, n1, n2, n1+n2))