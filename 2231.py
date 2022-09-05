n=int(input())
cnt=0
check=[]

for i in range(1,n):
    tmp=i
    while tmp>0:
        cnt+=tmp%10
        tmp=int(tmp/10)
    cnt+=i
    if cnt==n:
        check.append(i)
    cnt=0

if check:print(min(check))
else:print(0)
