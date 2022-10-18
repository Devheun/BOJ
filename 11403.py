# 경로 찾기 (플로이드-와샬 이용)

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:d[i][j]=arr[i][j]
        else:d[i][j]=1010 # 임의의 값

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j]=min(d[i][k]+d[k][j],d[i][j])


for i in range(n):
    for j in range(n):
        if d[i][j]==1010:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()