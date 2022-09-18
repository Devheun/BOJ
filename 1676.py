# 팩토리얼 0의 개수
import math

n=int(input())
number=math.factorial(n)
number=str(number)
cnt=0

for i in range(len(number)-1,-1,-1):
    if number[i]=='0':cnt+=1
    else:break
print(cnt)
