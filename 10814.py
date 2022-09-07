# 나이 순 정렬
n=int(input())
array=[]
for i in range(n):
    x,y=input().split()
    x=int(x)
    array.append(tuple([x,y,i]))

array.sort(key=lambda k: (k[0],k[2]))
#print(array)
for i in array:
    print(i[0],i[1])