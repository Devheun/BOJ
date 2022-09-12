# 덩치

n=int(input())
arr=[]

for _ in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))


cnt=1
order=[]

for i in range(n):
    for j in range(n):
        if i==j:continue
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            cnt+=1
    order.append(cnt)
    cnt=1

for k in order:
    print(k,end=' ')
