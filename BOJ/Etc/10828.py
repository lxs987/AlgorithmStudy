# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:18:25 2021

@author: lxs_9
"""
import sys

def push(x):
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    input = sys.stdin.readline().rstrip().split()
    sample = input[0]
    
    if sample == 'push':
        push(input[1])
    elif sample == 'pop':
        print(pop())
    elif sample == 'size':
        print(size())
    elif sample == 'empty':
        print(empty())
    elif sample == 'top':
        print(top())

