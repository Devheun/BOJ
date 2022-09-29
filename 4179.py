# 불 !
from collections import deque

def bfs2(x,y):
    vis_ji[x][y]=0
    q=deque()
    q.append((x,y))
    
    while q:
        cur=q.popleft()
        for i in range(4):
            nx=cur[0]+dx[i]
            ny=cur[1]+dy[i]
            if nx<0 or nx>=r or ny<0 or ny>=c: # 범위 넘어선 건 탈출했다는 말
                print(vis_ji[cur[0]][cur[1]]+1)
                exit(0)
            if vis_ji[nx][ny]!=-1 or board[nx][ny]=='#':continue
            if vis_ji[cur[0]][cur[1]]+1>=vis_fire[nx][ny] and vis_fire[nx][ny]!=-1:continue
            vis_ji[nx][ny]=vis_ji[cur[0]][cur[1]]+1
            q.append((nx,ny))

    

r,c=map(int,input().split()) # r이 행, c가 열
board=[list(input()) for _ in range(r)]
vis_fire=[[-1]*c for _ in range(r)] # 불 방문처리
vis_ji=[[-1]*c for _ in range(r)] # 지훈 방문처리
dx=[1,0,-1,0]
dy=[0,1,0,-1]

q1=deque()
for i in range(r):
    for j in range(c):
        if board[i][j]=='F': # 불 먼저 bfs 돌려놓기
            vis_fire[i][j]=0 # 처음 불 난 곳
            q1.append((i,j))
while q1:
    cur=q1.popleft()
    for i in range(4):
        nx=cur[0]+dx[i]
        ny=cur[1]+dy[i]
        if nx<0 or nx>=r or ny<0 or ny>=c:continue
        if vis_fire[nx][ny]!=-1 or board[nx][ny]=='#':continue
        vis_fire[nx][ny]=vis_fire[cur[0]][cur[1]]+1
        q1.append((nx,ny))
    
for i in range(r):
    for j in range(c):
        if board[i][j]=='J':
            bfs2(i,j)

print("IMPOSSIBLE")