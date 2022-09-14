# 소수 구하기

import math

m,n=map(int,input().split())
arr=[]

for i in range(m,n+1):
    if i==2 or i==3:
        arr.append(i)
    scope=int(math.sqrt(i))
    for j in range(2,scope+1):
        if i%j==0: # 소수가 아닐 때
            break
        elif j==scope and i%j!=0: #소수면 리스트에 추가
            arr.append(i)
        
for k in arr:
    print(k)