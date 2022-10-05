# 토마토
from collections import deque



dx=[-1,1,0,0,0,0] # 상하좌우 위아래
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

m,n,h=map(int,input().split()) # m은 열, n은 행, h는 높이
arr=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
vis=[[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q=deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if arr[k][i][j]==1 and vis[k][i][j]==-1: # 토마토 있고 방문 X
                q.append((k,i,j))
                vis[k][i][j]=0

while q:
    cur=q.popleft()
    for k in range(6):
        nz=dz[k]+cur[0]
        nx=dx[k]+cur[1]
        ny=dy[k]+cur[2]
        
        if nx<0 or nx>=n or nz<0 or nz>=h or ny<0 or ny>=m:continue
        if arr[nz][nx][ny]!=0 or vis[nz][nx][ny]!=-1:continue
        vis[nz][nx][ny]=vis[cur[0]][cur[1]][cur[2]]+1
        q.append((nz,nx,ny))
day=0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if vis[k][i][j]==-1 and arr[k][i][j]==0:
                print(-1)
                exit()
            day=max(day,vis[k][i][j])
            
print(day)
                
        