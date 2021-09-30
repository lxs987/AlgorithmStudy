def dfs(depth):
    if depth == N:
        res.append(sum(abs(li[i+1]-li[i]) for i in range(N-1)))
        return ;
    for i in range(N):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        li.pop()
        check[i] = 0

N = int(input())
nums = list(map(int, input().split()))
li, res = [], []
check = [0]*N
dfs(0)
print(max(res))
