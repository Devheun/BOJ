# 숫자 카드 2
import sys
import bisect

def binary_search(arr,num):
    
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<num:
            left=mid+1
        elif arr[mid]>num:
            right=mid-1
        elif arr[mid]==num:
            return mid
    return -1

n=int(input())
have=list(map(int,sys.stdin.readline().rstrip().split()))

m=int(input())
not_have=list(map(int,sys.stdin.readline().rstrip().split()))

have.sort()

result=[]
cnt=0

for i in not_have:
    if binary_search(have,i)!=-1:
        result.append(bisect.bisect_right(have,i)-bisect.bisect_left(have,i))
    else:
        result.append(0)
    

for j in result:
    print(j,end=' ')
        