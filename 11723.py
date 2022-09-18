# 집합
import sys
m=int(input())
s=[0]*21

for _ in range(m):
    a=sys.stdin.readline().rstrip()
    if ' ' in a:
        a,b=a.split()
        
    if a=="add" and not s[int(b)]:
        s[int(b)]=1
    elif a=="remove" and s[int(b)]:
        s[int(b)]=0
    elif a=="check" and s[int(b)]:
        sys.stdout.write('1\n')
    elif a=="check" and not s[int(b)]:
        sys.stdout.write('0\n')
    elif a=="toggle" and s[int(b)]:
        s[int(b)]=0
    elif a=="toggle" and not s[int(b)]:
        s[int(b)]=1
    elif a=="all":
        s=[1]*21
    else:
        s=[0]*21
    
 