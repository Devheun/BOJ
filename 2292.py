# 벌집

n=int(input())

if n==1:
    print(1)
    exit()

n-=1
cnt=1
i=1
while n>0:
    cnt+=1
    n-=6*i
    i+=1

print(cnt)
  