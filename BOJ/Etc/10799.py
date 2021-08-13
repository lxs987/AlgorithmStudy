# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:27:55 2021

@author: lxs_9
"""
import sys
lst = sys.stdin.readline().strip()
stack = []
result = 0

for i in range(len(lst)):
    # '('이 나올 경우, stack에 push
    if lst[i] == '(':
        stack.append('(')
    
    # ')'이 나올 경우
    else:
        # 전 문자열이 '('이라면 레이저이므로
        # stack에서 1개를 pop하고, 스택의 크기만큼 result에 더함
        if lst[i-1] == '(':
            stack.pop()
            result += len(stack)
        # ')'일 경우 막대기가 있는 것이므로
        # 1개를 result에 증가시킴
        else:
            stack.pop()
            result += 1
            
print(result)
