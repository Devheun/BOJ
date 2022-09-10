# 수 정렬하기 3
import sys

n=int(input())
arr=[0]*10001

for _ in range(n):
    number=sys.stdin.readline().rstrip()
    arr[int(number)]+=1

for i in range(1,len(arr)):
    if arr[i]==0:continue
    else:
        for j in range(arr[i]):
            print(i)
            
            