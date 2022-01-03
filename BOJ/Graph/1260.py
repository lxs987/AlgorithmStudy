# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 04:51:15 2021

@author: lxs_9
"""
import sys
# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for __ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

# 오름차순으로 node를 방문하기 위해 인접 리스트를 사전에 내림차순으로 정렬
for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    
    # 1)stack에 첫 번째 노드 넣으면서 시작
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    # 2) stack이 비어있는지 확인(비어있지 않다면 아래 코드 진행)
    while stack:
        # 3) stack에서 맨 위의 노드를 pop
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
    return d_visit

def bfs():
    b_visit = []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
    return b_visit

print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
