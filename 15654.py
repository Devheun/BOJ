# N과 M (5)

def dfs():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    for i in input_arr:
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

n,m=map(int,input().split())
input_arr=list(map(int,input().split()))
input_arr.sort()
arr=[]

dfs()
