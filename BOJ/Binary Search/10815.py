import sys

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
m = int(input())
s_ = list(map(int, input().split()))

# 정렬한 후
s.sort()

# 이분탐색 진행하며 숫자를 찾는다
for i in s_:
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if 0 <= mid < n:
            if s[mid] < i: low = mid + 1
            else: high = mid - 1
        else: break
    if 0 <= high + 1 < n:
        if s[high + 1] == i: print(1, end=" ")
        else: print(0, end=" ")
    else: print(0, end=" ")
