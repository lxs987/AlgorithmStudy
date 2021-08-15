# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 17:41:52 2021

@author: lxs_9
"""

n, k = map(int, input().split())
# 맨 처음 앉아있는 모든 사람들
lst = [i for i in range(1, n+1)]
# 제거된 사람들
answer = []
# 제거될 사람의 인덱스 번호
num = k-1

for _ in range(n):
    if len(lst) <= num:
        num = num % len(lst)
    answer.append(lst.pop(num))
    num += k-1

print("<", ', '.join(str(i) for i in answer), ">", sep = '')
