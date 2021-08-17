# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:07:23 2021

@author: lxs_9
"""

import sys
sys.setrecursionlimit(2000)

def dfs(x):
    visited[x] = True # 방문 체크
    number = numbers[x] # 다음 방문 장소
    if not visited[number]: # 방문하지 않았다면
        dfs(number) #재귀
        
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n # 방문여부확인
    result = 0
    
    for i in range(1, n+1):
        if not visited[i]: # 방문하지 않았다면
            dfs(i) # DFS 실행
            result += 1 # 결과값에 +1
    print(result)
