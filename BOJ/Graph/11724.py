# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 04:56:22 2021

@author: lxs_9
"""
import sys

# 재귀 한계
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
cnt = 0

# DFS를 이용하여 하나 하나 방문하며 탐색
def dfs(i):
    visit[i] = 1
    for k in range(1, n + 1):
        if s[i][k] == 1 and visit[k] == 0:
            dfs(k)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a][b] = 1
    s[b][a] = 1
for i in range(1, n + 1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
