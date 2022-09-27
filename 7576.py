# 토마토
from collections import deque

m,n=map(int,input().split()) # n이 행, m이 열
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[-1]*m for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
q=deque()

for i in range(n):
    for j in range(m):
        if visited[i][j]==-1 and board[i][j]==1: #처음부터 익은 토마토 찾기
            q.append((i,j))
            visited[i][j]=0
        

min_day=0

while q:
    cur=q.popleft()
    for k in range(4):
        nx=cur[0]+dx[k]
        ny=cur[1]+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m:continue
        if board[nx][ny]!=0 or visited[nx][ny]!=-1:continue
        visited[nx][ny]=visited[cur[0]][cur[1]]+1
        q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if visited[i][j]==-1 and board[i][j]==0: # 모두 익지 못하는 상황
            print(-1)
            exit()
        else:
            min_day=max(min_day,visited[i][j])

print(min_day)