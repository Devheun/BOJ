# 듣보잡
import sys
n,m=map(int,input().split())
not_hear=set()
not_see=set()
for _ in range(n):
    not_hear.add(sys.stdin.readline().rstrip())
for _ in range(m):
    not_see.add(sys.stdin.readline().rstrip())

not_hear_see=not_hear&not_see
not_hear_see=list(not_hear_see)
not_hear_see.sort()
print(len(not_hear_see))
for i in not_hear_see:
    print(i)