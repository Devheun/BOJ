# N과 M (5)

def dfs(num):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    for i in input_arr:
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()

n,m=map(int,input().split())
input_arr=list(map(int,input().split()))
input_arr.sort()
arr=[]

dfs(input_arr[0])
