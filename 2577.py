# 숫자의 개수

a=int(input())
b=int(input())
c=int(input())

mul=a*b*c
check=[0]*10
mul=str(mul)

for i in mul:
    check[int(i)]+=1

for j in check:
    print(j)

