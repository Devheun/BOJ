# N과 M (8)

def dfs():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    for i in input_arr:
        if arr:
            if arr[-1]>i:continue
        
        arr.append(i)
        dfs()
        arr.pop()
    

n,m=map(int,input().split())
input_arr=list(map(int,input().split()))
input_arr.sort()
arr=[]

dfs()