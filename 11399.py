# ATM

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
cnt=[0]*2


for i in range(len(arr)):
    cnt[0]+=arr[i]
    cnt[1]=sum(cnt)
print(cnt[1])