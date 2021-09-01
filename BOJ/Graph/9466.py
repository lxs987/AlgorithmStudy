import sys
def team_check(array,start):
    global team_complete, team_fail, group_num
    pick = start

    while not visited[pick]:
        visited[pick] = group_num
        pick = array[pick]
    while visited[pick] == group_num:
        visited[pick] = -1
        pick = array[pick]
    group_num += 1

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    array = [-1] + list(map(int, sys.stdin.readline().split()))
    team_fail = 0
    group_num = 1
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            team_check(array,i)

    for i in range(1,n+1):
        if visited[i] > 0:
            team_fail += 1
    print(team_fail)
