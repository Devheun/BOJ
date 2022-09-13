# 설탕 배달

n=int(input())
d=[0 for _ in range(5001)]

for i in range(3,5001):
    if i%5==0:
        d[i]=i//5
    elif i%3==0:
        d[i]=i//3

cnt=n
i=cnt//5 # 5로 나눈 몫

while True:
    cnt=cnt-5*i
    if i==-1:
        print(-1)
        exit()
    if cnt%3==0:
        d[n]=d[5*i]+d[cnt]
        break
    else:
        i-=1
        cnt=n

print(d[n])
        