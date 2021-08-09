# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:21:17 2021

@author: lxs_9
"""
# Dynamic Programming
# 9465. 스티커

T = int(input())
for _ in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))
    
# The number of Testcase
# T = int(input())

# for i in T:
#     n = int(input())
#     lst = []
#     sum = 0
#     for j in n*2:
#         lst.append(int(input()))
#     while max(lst)!=-1:
#         sum+=max(lst)
#         lst[lst.index(max(lst))-1] = -1
#         lst[lst.index(max(lst))+1] = -1
#         if(lst.index(max(lst))<n):
#             lst[lst.index(max(lst))+n] = -1
#         else:
#             lst[lst.index(max(lst))-n] = -1
            
#         lst[lst.index(max(lst))] = -1
        
#     print(sum)