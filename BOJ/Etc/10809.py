# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:09:22 2021

@author: lxs_9
"""
# 아니 ㅅㅂ 왜안됨
# import sys
# s = sys.stdin.readline().split()
s = "baekjoon"
lst = [-1] * 26
for i in range(len(s)):
    if lst[ord(s[i])-97] == -1:
        print(i, ord(s[i])-97)
        lst[ord(s[i])-97] += int(1+i)
for i in lst:
    print(lst[i], end=' ')
