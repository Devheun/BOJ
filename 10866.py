# 덱
import sys
from collections import deque

n=int(input())
arr=deque()
for _ in range(n):
    order=sys.stdin.readline().rstrip()
    if len(order)>10: # push들
        a,b=order.split()
        b=int(b)
        if a=="push_back":
            arr.append(b)
        elif a=="push_front":
            arr.appendleft(b)
    elif len(order)<10 and len(order)>7: #pop들
        if order=="pop_back":
            if len(arr)==0:print(-1)
            else:print(arr.pop())
        elif order=="pop_front":
            if len(arr)==0:print(-1)
            else:print(arr.popleft())
    elif order[1]=="i":# size
        print(len(arr))
        
    elif order[1]=="m": # empty
        if len(arr)==0:print(1)
        else:print(0)
            
    elif order[1]=="r": #front
        if len(arr)==0:print(-1)
        else:print(arr[0])
            
    else:	#back
        if len(arr)==0:print(-1)
        else:print(arr[len(arr)-1])
    
        
    