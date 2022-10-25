# N과 M(2)

def dfs(num):
    global arr
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in range(num,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()
    
n,m=map(int,input().split())
arr=[]

dfs(1)