# 최소 힙
import sys
import heapq # 파이썬은 최소 힙 지원

n=int(input())
arr=[]
for _ in range(n):
    num=int(sys.stdin.readline().rstrip())
    if arr and num==0:
        print(heapq.heappop(arr))
    elif num:heapq.heappush(arr,num)
    else:print(0)
        