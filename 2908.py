# 상수

a,b=input().split()
reverse_a=int(a[2]+a[1]+a[0])
reverse_b=int(b[2]+b[1]+b[0])
if reverse_a>reverse_b:
    print(reverse_a)
else:print(reverse_b)