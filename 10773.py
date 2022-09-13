# 제로
import sys

arr=[]

k=int(input())
for _ in range(k):
    number=int(sys.stdin.readline().rstrip())
    if number!=0:arr.append(number)
    elif number==0:arr.pop()
    
print(sum(arr))