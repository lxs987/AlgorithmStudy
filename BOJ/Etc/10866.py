# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:11:59 2021

@author: lxs_9
"""
from collections import deque
import sys

def size():
    return len(deq)

def empty():
    if size()==0:
        return 1
    else:
        return 0
n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0]=='push_front':
        deq.appendleft(cmd[1])
        
    elif cmd[0]=='push_back':
        deq.append(cmd[1])
        
    elif cmd[0]=='pop_front':
        if empty()==1:
            print("-1")
        else:
            tmp = deq.popleft()
            print(tmp)
        
    elif cmd[0]=='pop_back':
        if empty()==1:
            print("-1")
        else:
            tmp = deq.pop()
            print(tmp)
        
    elif cmd[0]=='size':
        print(size())
        
    elif cmd[0]=='empty':
        print(empty())
        
    elif cmd[0]=='front':
        if empty()==1:
            print(-1)
        else:
            print(deq[0])
            
    elif cmd[0]=='back':
        if empty()==1:
            print(-1)
        else:
            print(deq[-1])
