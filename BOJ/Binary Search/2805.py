# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:32:23 2021

@author: lxs_9
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = list(map(int, input().split()))
low, high = 0, 1000000000
while low <= high:
    mid = (low + high) // 2
    num = 0
    for i in s:
        num += i - mid if i - mid > 0 else 0
    if num >= m: low = mid + 1
    else: high = mid - 1
print(high)
