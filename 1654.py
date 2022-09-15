# 랜선 자르기

def binary_search(arr,target,n):

    left,right=1,target
    
    while left<=right:
        mid=(left+right)//2
        cnt=0
        for i in arr:
            cnt+=i//mid
        if cnt<n:
            right=mid-1
        elif cnt>=n:
            left=mid+1
    return right

k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))

max_value=max(arr)
arr.sort()

result=binary_search(arr,max_value,n)
print(result)
