# 바이러스 

def dfs(num):
    global cnt
    visited[num]=True #방문처리
    cnt+=1
    for j in arr[num]:
        if visited[j]==False:
            dfs(j)
    

n=int(input())
pair=int(input())
arr=[[] for _ in range(n+1)]
cnt=0
visited=[False] * (n+1)

for _ in range(pair):
    x,y=map(int,input().split())
    arr[x].append(y) # x -> y로 연결되어있다.
    arr[y].append(x) # y -> x로 연결되어있다.

visited[1]=True
for i in arr[1]:
    if visited[i]==False:
        dfs(i)

print(cnt)

