# 좌표 정렬하기

array=[]
n=int(input())
for _ in range(n):
    tmp=tuple(map(int,input().split()))
    array.append(tmp)

array.sort()
for i in array:
    print(i[0],i[1])