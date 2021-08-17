# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 05:02:51 2021

@author: lxs_9
"""
# 1. 맨 처음 bfs에 입력한 값은 1로 체크한다

# 2. 그 다음에 이동할 수 있는 지점은 현재 체크한 값에 -1을 곱하면서 이분한다

# 3. 만일 다음에 이동할 지점의 체크값과 현재 체크값이 같으면 이분할 수 없다는 뜻이므로 NO를 출력

from collections import deque
import sys

input = sys.stdin.readline
k = int(input())

def bfs(start):
    bi[start] = 1
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in s[a]:
            if bi[i] == 0:
                bi[i] = -bi[a]
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):
    v, e = map(int, input().split())
    isTrue = True
    s = [[] for i in range(v + 1)]
    bi = [0 for i in range(v + 1)]
    for j in range(e):
        a, b = map(int, input().split())
        s[a].append(b)
        s[b].append(a)
    for k in range(1, v + 1):
        if bi[k] == 0:
            if not bfs(k):
                isTrue = False
                break
    print("YES" if isTrue else "NO")
