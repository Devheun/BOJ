n=int(input())
arr=[]
result=[]
cnt=1

for i in range(n):
    num=int(input())
    while cnt<=num:
        arr.append(cnt)
        cnt+=1
        result.append('+')
    if arr[-1]==num:
        arr.pop()
        result.append('-')
    else:
        print('NO')
        exit()

for j in result:
    print(j)