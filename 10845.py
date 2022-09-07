# 큐
from collections import deque
import sys

arr=deque([])
n=int(input())
for _ in range(n):
    order=sys.stdin.readline().rstrip()
    if order[1]=="u": # push의 경우
        a,b=order.split()
        b=int(b)
        arr.append(b)
        
    elif order[1]=="o": # pop의 경우
        if len(arr)==0:print(-1)
        else:print(arr.popleft())
    
    elif order[1]=="i": # size의 경우
        print(len(arr))
        
    elif order[1]=="m": # empty의 경우
        if len(arr)==0:
            print(1)
        else: print(0)
            
    elif order[1]=="r": # front의 경우
        if len(arr)==0:print(-1)
        else:print(arr[0])
    else:# back의 경우
        if len(arr)==0:print(-1)
        else:print(arr[len(arr)-1])