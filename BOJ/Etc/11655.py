# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 02:46:50 2021

@author: lxs_9
"""
import sys

line = list(sys.stdin.readline().rstrip())

for i in range(len(line)):

    # 대문자: 65~90
    if line[i].isupper():
        if ord(line[i])+13 <= 90:
            line[i] = chr(ord(line[i])+13)
        else:
            line[i] = chr(ord(line[i])-13)

    # 소문자: 97~122
    elif line[i].islower():
        if ord(line[i])+13 <= 122:
            line[i] = chr(ord(line[i])+13)
        else:
            line[i] = chr(ord(line[i])-13)

for each in line:
    print(each, end="")
