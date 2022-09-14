# 통계학
import math


n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

print(round(sum(arr)/len(arr))) # 산술평균
arr.sort()
print(arr[math.floor(len(arr)/2)]) # 미디안

cnt=[0 for _ in range(n)]
for i in range(1,n):
    if arr[i-1]==arr[i]: # 여러번 나타나는 경우
        cnt[i]=cnt[i-1]+1
max_value=max(cnt) # 최빈값 구하기

max_cnt=[]
for j in range(n):
    if cnt[j]==max_value: #최빈값이라면
        max_cnt.append(arr[j])
if len(max_cnt)==1: # 최빈값이 한개면
    print(max_cnt[0])
elif len(max_cnt)>=2:
    print(max_cnt[1])
        
print(arr[len(arr)-1]-arr[0]) # 범위