# 2xn 타일링 2

d=[0]*1001
n=int(input())
d[1]=1
d[2]=3

for i in range(3,1001):
    d[i]=((d[i-2]*2%10007)+(d[i-1]%10007))%10007
print(d[n])