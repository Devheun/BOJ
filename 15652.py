# N과 M (4)

def dfs(num):
    global arr
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(num,n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
        


n,m=map(int,input().split())
arr=[]
dfs(1)