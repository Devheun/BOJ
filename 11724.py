# 연결 요소의 개수

import sys

def dfs(num):
    visited[num]=True
    for j in arr[num]:
        if not visited[j]:
            dfs(j)

n,m=map(int,sys.stdin.readline().rstrip().split())
arr=[[] for i in range(n+1)]
visited=[False]*(n+1)
cnt=0

for _ in range(m):
    u,v=map(int,sys.stdin.readline().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1
print(cnt)