# 구간 합 구하기 4
n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum_arr=[]
sum_arr.append(arr[0])
for i in range(n-1):
    sum_arr.append(sum_arr[i]+arr[i+1])
for _ in range(m):
    i,j=map(int,input().split())
    if i==1:
        print(sum_arr[j-1])
    else:
        print(sum_arr[j-1]-sum_arr[i-2])