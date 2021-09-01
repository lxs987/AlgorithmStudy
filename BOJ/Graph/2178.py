# -*- coding: utf-8 -*-
"""

@author: lxs_9
"""
from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    if x + 1 < N and visited[x+1][y] == 0 and matrix[x+1][y] == '1':
        visited[x+1][y] = visited[x][y] + 1
        queue.append((x+1, y))
    if 0 <= x - 1  and visited[x-1][y] == 0 and matrix[x-1][y] == '1':
        visited[x-1][y] = visited[x][y] + 1
        queue.append((x-1, y))
    if y + 1 < M and visited[x][y + 1] == 0 and matrix[x][y + 1] == '1':
        visited[x][y + 1] = visited[x][y] + 1
        queue.append((x, y + 1))
    if 0 <= y - 1 and visited[x][y - 1] == 0 and matrix[x][y - 1] == '1':
        visited[x][y - 1] = visited[x][y] + 1
        queue.append((x, y - 1))
