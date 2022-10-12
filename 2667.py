# 단지번호 붙이기
from collections import deque

def bfs(x,y):
    global max_value
    q=deque()
    q.append((x,y))
    
    while q:
        cur=q.popleft()
        for k in range(4):
            nx=dx[k]+cur[0]
            ny=dy[k]+cur[1]
            
            if nx<0 or nx>=n or ny<0 or ny>=n:continue
            if arr[nx][ny]!=1 or visited[nx][ny]!=0:continue
            visited[nx][ny]=visited[cur[0]][cur[1]]+1
            q.append((nx,ny))
            max_value+=1
    
    max_list.append(max_value)
    max_value=0


dx=[1,0,-1,0]
dy=[0,1,0,-1]

n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]
cnt=0 # 총 단지수
max_list=[]
max_value=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and visited[i][j]==0:
            visited[i][j]=1
            bfs(i,j)
            cnt+=1
print(cnt)
max_list.sort()
for i in max_list:
    print(i+1)
