# 유기농 배추

from collections import deque

dx=[0,0,-1,1] #동서남북
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    vis[x][y]=True # 방문처리
    q.append((x,y))
    
    while q:
        cur_x,cur_y=q.popleft()
        for k in range(4):
            nx=cur_x+dx[k]
            ny=cur_y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if not vis[nx][ny] and a[nx][ny]:
                    q.append((nx,ny))
                    vis[nx][ny]=True
    

t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split()) # m이 열, n이 행
    a=[[0]*m for _ in range(n)]
    vis=[[False]*m for _ in range(n)]
    
    for _ in range(k):
        y,x=map(int,input().split())
        a[x][y]=1
    
    cnt=0
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and a[i][j]:
                cnt+=1
                bfs(i,j)
    print(cnt)