# 나는야 포켓몬 마스터 이다솜
import sys
arr=[]
n,m=map(int,input().split())
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())
for _ in range(m):
    s=sys.stdin.readline().rstrip()
    if s.isdigit():
        print(arr[int(s)-1])
    else:
        print(arr.index(s)+1)