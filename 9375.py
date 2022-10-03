# 패션왕 신해빈


t=int(input())
cnt=1
for _ in range(t):
    n=int(input())
    clothes=dict()
    for i in range(n):
        name,kind=input().split()
        if kind in clothes:
            clothes[kind]+=1
        else:
            clothes[kind]=1
 
    for j in list(clothes.values()):
        cnt*=(j+1)
    print(cnt-1)
    cnt=1