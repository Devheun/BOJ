# 숨바꼭질

from collections import deque

n,k=map(int,input().split())
dx=[-1,1,2]
q=deque()

visited=[0 for _ in range(100001)]
visited[n]=0
q.append(n)

while q:
    x=q.popleft()
    if x==k: # 동생 위치와 현 위치가 같으면
        print(visited[k])
        exit(0)
    for i in range(3):
        if i==2:
            if 0<=x*2<=100000 and not visited[2*x]:
                q.append(x*2)
                visited[x*2]=visited[x]+1
        else:
            if 0<=x+dx[i]<=100000 and not visited[x+dx[i]]:
                q.append(x+dx[i])
                visited[x+dx[i]]=visited[x]+1
