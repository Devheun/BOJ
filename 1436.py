# 영화감독 숌

n=int(input())

arr=[]

for i in range(666,10000000): #어림잡아 젤 큰 크기
    string=str(i)
    
    index=string.find("666")
    if index!=-1:
        arr.append(string)


print(arr[n-1])

    