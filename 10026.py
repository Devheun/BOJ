# 적록색약
from collections import deque
import copy

def bfs(x,y,color):
    q=deque()
    q.append((x,y,color))
    
    while q:
        cur=q.popleft()
        for k in range(4):
            nx=dx[k]+cur[0]
            ny=dy[k]+cur[1]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:continue
            if vis_basic[nx][ny]!=0 or basic[nx][ny]!=color:continue
            vis_basic[nx][ny]=1
            q.append((nx,ny,color))
            
def bfs2(x,y,color):
    q=deque()
    q.append((x,y,color))
    
    while q:
        cur=q.popleft()
        for k in range(4):
            nx=dx[k]+cur[0]
            ny=dy[k]+cur[1]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:continue
            if vis_error[nx][ny]!=0 or error[nx][ny]!=color:continue
            vis_error[nx][ny]=1
            q.append((nx,ny,color))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
basic=[list(map(str,input())) for _ in range(n)] # 기본
error=copy.deepcopy(basic) # 적록색약 버전
vis_basic=[[0]*n for _ in range(n)] #방문 여부 체크
vis_error=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if error[i][j]=="G":
            error[i][j]="R"

cnt_basic=0
for i in range(n):
    for j in range(n):
        if vis_basic[i][j]==0:
            vis_basic[i][j]=1
            cnt_basic+=1
            bfs(i,j,basic[i][j])
            
cnt_error=0
for i in range(n):
    for j in range(n):
        if vis_error[i][j]==0:
            vis_error[i][j]=1
            cnt_error+=1
            bfs2(i,j,error[i][j])
print(cnt_basic,cnt_error)
            
