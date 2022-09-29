# 회의실 배정

n=int(input())
arr=[]
for _ in range(n):
    start,end=map(int,input().split())
    arr.append((start,end))

arr=sorted(arr,key=lambda x:(x[1],x[0]))

result=[]
for i in range(len(arr)):
    if i==0:
        result.append(arr[i])
    elif arr[i][0]<result[-1][1]:
        continue
    else:
        result.append((arr[i]))
print(len(result))