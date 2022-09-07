# 수 정렬하기2

n=int(input())
array=[]
for _ in range(n):
    number=int(input())
    array.append(number)

array.sort()
for i in array:
    print(i)