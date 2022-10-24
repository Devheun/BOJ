# 조합

n,m=map(int,input().split())
result=1
result2=1
tmp1=n-m

for i in range(n,tmp1,-1):
    result*=i

for j in range(1,m+1):
    result2*=j

print(result//result2)