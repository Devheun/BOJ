# 그림
from collections import deque

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

dx=[1,0,-1,0] #남동북서
dy=[0,1,0,-1]
cnt=0 # 그림 수
max_num=0 # 가장 큰 그림 크기


for i in range(n):
    for j in range(m):
        if board[i][j]==1 and visited[i][j]==0:# 그림있고 방문 X
            cnt+=1
            visited[i][j]=1
            q=deque()
            q.append((i,j))
            
            tmp=0
            while q:
                now=q.popleft()
                tmp+=1
                for k in range(4):
                    nx=now[0]+dx[k]
                    ny=now[1]+dy[k]
                    if nx<0 or nx>=n or ny<0 or ny>=m:continue
                    if visited[nx][ny] or not board[nx][ny]:continue
                    visited[nx][ny]=1
                    q.append((nx,ny))
            max_num=max(max_num,tmp)
print(cnt)
print(max_num)