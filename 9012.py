# 괄호
from collections import deque
import sys

t=int(input())
cnt=0
queue=deque()

for _ in range(t):
    string=sys.stdin.readline().rstrip()
    
    for i in string:
        if i=='(':
            queue.append(i)
        elif len(queue)==0 and i==')':
            print("NO")
            cnt=1
            break
        elif len(queue)>0 and i==')':
            queue.pop()
    if cnt==1:
        cnt=0
        continue
    elif len(queue)==0:
        print("YES")
    elif len(queue)>0:
        print("NO")
    queue.clear()