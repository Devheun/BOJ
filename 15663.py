# N과 M (9)

n,m=map(int,input().split())
input_arr=list(map(int,input().split()))
input_arr.sort()
visited=[False]*n
arr=[]

def dfs():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    tmp=0
    
    for i in range(n):
        if not visited[i] and tmp!=input_arr[i]:
            visited[i]=True
            arr.append(input_arr[i])
            tmp=input_arr[i]
            dfs()
            visited[i]=False
            arr.pop()

dfs()
