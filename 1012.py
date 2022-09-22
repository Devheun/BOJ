# 유기농 배추

from collections import deque

dx=[-1, 1, 0, 0] 
dy=[0, 0, -1, 1]

def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    dist[x][y] = cnt

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1 and dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = cnt


t = int(input())
for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]

    for _ in range(k):
        i, j = map(int, input().split())
        board[i][j] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and dist[i][j] == -1:
                cnt += 1
                bfs(i, j, cnt)

    print(cnt)