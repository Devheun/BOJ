# 미로 탐색
from collections import deque



def bfs(x,y):
    q=deque()
    visited[x][y]=0 # 처음 방문하는 칸이므로 0으로 초기화
    q.append((x,y))
    
    while q:
        cur=q.popleft()
        for k in range(4):
            nx=cur[0]+dx[k]
            ny=cur[1]+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=m:continue
            if visited[nx][ny]>=0 or board[nx][ny]!=1:continue
            visited[nx][ny]=visited[cur[0]][cur[1]]+1
            q.append((nx,ny))
            
n,m=map(int,input().split())
board=[list(map(int,input())) for _ in range(n)]
visited=[[-1]*m for _ in range(n)] # 처음 방문하는 칸 0으로
dx=[1,0,-1,0]
dy=[0,1,0,-1]

bfs(0,0)


print(visited[n-1][m-1]+1)
