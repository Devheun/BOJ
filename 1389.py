# 케빈 베이컨의 6단계 법칙

n,m=map(int,input().split())

vis=[[12345678]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    vis[a][b]=1
    vis[b][a]=1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i==j:continue
            else:
                vis[i][j]=min(vis[i][j],vis[i][k]+vis[k][j])

result=[]
cnt=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if vis[i][j]!=12345678:
            cnt+=vis[i][j]
    result.append((cnt,i))
    cnt=0
result.sort()
print(result[0][1])
    