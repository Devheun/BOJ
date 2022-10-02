# 동전 0

n,k=map(int,input().split())
arr=[]

for _ in range(n):
    num=int(input())
    arr.append(num)

i=len(arr)-1
tmp=k
cnt=0
while tmp>0:
    if tmp<arr[i]:
        i=i-1
    else:
        cnt+=tmp//arr[i]
        tmp=tmp%arr[i]
        i=i-1
print(cnt)