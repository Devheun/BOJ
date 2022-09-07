# 수 찾기

def binary_search(array,num):
    left,right=0,len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]>num:
            right=mid-1
        if array[mid]<num:
            left=mid+1
        if array[mid]==num:
            return mid
    return -1

n=int(input())
numbers=list(map(int,input().split()))
numbers.sort() # 이분 탐색을 위해 정렬

m=int(input())
numbers2=list(map(int,input().split()))
for i in numbers2:
    result=binary_search(numbers,i)
    if result!=-1:print(1)
    else:print(0)