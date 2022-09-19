# 1로 만들기
import sys
n=int(input())
d=[0]*1000001
d[2]=1
d[3]=1
cnt3=0
cnt2=0
cnt1=0
d[0]=1234567890
if n==1:
    print(0)
    exit()
elif n==2 or n==3:
    print(1)
    exit()

for i in range(4,n+1):
    if i%3==0:cnt3=i//3
    if i%2==0:cnt2=i//2
    cnt1=i-1
    d[i]=min(d[cnt3],d[cnt2],d[cnt1])+1
    cnt3,cnt2,cnt1=0,0,0
print(d[n])