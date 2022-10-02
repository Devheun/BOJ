# DFS와 BFS
from collections import deque

def dfs(i):
    visited[i]=True
    
    for j in arr[i]:
        if not visited[j]:
            print(j,end=" ")
            dfs(j)
def bfs(i):
    visited[i]=True
    q=deque()
    q.append(i)
    
    while q:
        cur=q.popleft()
        for k in arr[cur]:
            if not visited[k]:
                visited[k]=True
                q.append(k)
                print(k,end=" ")

arr=[[] for _ in range(1001)]
visited=[False]*1001
n,m,v=map(int,input().split())
for _ in range(m):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

for i in range(1,1001):
    if arr[i]:
        arr[i].sort()

print(v,end=" ")
dfs(v)
print()

visited=[False]*1001
print(v,end=" ")
bfs(v)

