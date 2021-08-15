# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 03:30:08 2021

@author: lxs_9
"""
# 최대공약수와 최소공배수를 구하는 문제
# 유클리드 호제법을 알고 있으면 쉽게 풀 수 있음

# 유클리드 호제법은 GCD를 쉽게 구할 수 있는 알고리즘
# 두 수 a와 b (a > b)가 있다고 할 때, a와 b의 최대공약수 G는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 G'과 서로 같다

# 출처: https://suri78.tistory.com/36 [공부노트]

import sys
A, B = map(int, sys.stdin.readline().split())
a, b = A, B
while b!=0:
    a = a%b
    a, b = b, a

# gcd
print(a)

# lcm
print(A*B//a)
