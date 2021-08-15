# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 01:00:28 2021

@author: lxs_9
"""
# 미통과 코드
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
# 처음에 앉아있는 모든 사람
dq = deque([i for i in range(1, n+1)])
# 제거된 사람
result = []

while dq:
    #rotate() 메서드의 경우에는 인자가 음수일 경우에 왼쪽으로 회전하며 양수가 주어지면 오른쪽으로 회전한다.
    #table = deque([a, b, c])가 있을 때 table.rotate(1)의 결과는 [c, a, b]이며, table.rotate(-1)의 결과는 [b, c, a]이다.
    # 출처: https://suri78.tistory.com/113 [공부노트]
    dq.rotate(-k+1)
    result.append(str(dq.popleft()))
    
sys.stdout.write("<"+", ".join(result)+">")
