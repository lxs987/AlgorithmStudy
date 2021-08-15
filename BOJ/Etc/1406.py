# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 03:09:11 2021

@author: lxs_9
"""
import sys

stack_l = list(sys.stdin.readline().strip())
stack_r = []

n = int(input())

for _ in range(n):
    data = sys.stdin.readline()
    if data[0] == 'L':
        if stack_l:
            stack_r.append(stack_l.pop())
    elif data[0] == 'D':
        if stack_r:
            stack_l.append(stack_r.pop())
    elif data[0] == 'B':
        if stack_l:
            stack_l.pop()
    elif data[0] == 'P':
        stack_l.append(data[2])

print(''.join(stack_l+stack_r[::-1]))
