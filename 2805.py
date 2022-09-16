# 나무 자르기

def binary_search(arr):
    left,right=0,max(arr) # left는 0이 될 수도 있음
    
    while left<=right:
        mid=(left+right)//2
        cnt=0
        for i in arr:
            if i-mid>0:
                cnt+=i-mid
        if cnt<m:
            right=mid-1
        elif cnt>=m:
            left=mid+1
    return right

n,m=map(int,input().split())
trees=list(map(int,input().split()))

trees.sort()
print(binary_search(trees))