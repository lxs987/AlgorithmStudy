# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:34:39 2021

@author: lxs_9
"""
s1 = input()
for i in range(len(s1)):
    if((i!=0) and (i%10==0)):
        print('')
    print(s1[i], end='')