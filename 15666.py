# N과 M (12)
def dfs():
    
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    tmp=0
    
    for i in range(len(input_arr)):
        if arr:
            if arr[-1]<=input_arr[i] and tmp!=input_arr[i]:
                arr.append(input_arr[i])
                tmp=input_arr[i]
                dfs()
                arr.pop()
        elif not arr:
            arr.append(input_arr[i])
            tmp=input_arr[i]
            dfs()
            arr.pop()
            

n,m=map(int,input().split())
input_arr=list(set(map(int,input().split())))
input_arr.sort()
arr=[]
dfs()
