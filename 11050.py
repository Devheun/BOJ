# 이항 계수 1
tmp1=1
tmp2=1
tmp3=1
n,k=map(int,input().split())
for i in range(1,n+1):
    tmp1*=i
for j in range(1,n-k+1):
    tmp2*=j

for q in range(1,k+1):
    tmp3*=q
print(int(int(tmp1/tmp2)/tmp3))
