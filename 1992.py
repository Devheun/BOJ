# 쿼드트리 (4개의 정사각형으로 분할정복)

def func(x,y,ran):
    if ran==1: # 최소 조건
        print(arr[x][y],end='')
        return
    else:
        start2=arr[x][y] # 가장 최상단 좌측 점 기준
        flag2=False
        for i in range(x,x+ran):
            for j in range(y,y+ran):
                if arr[i][j]==start2:
                    continue
                else:
                    flag2=True
                    break
            if flag2:
                break
        if flag2:
            print("(",end='')
            func(x,y,ran//2)
            func(x,y+ran//2,ran//2)
            func(x+ran//2,y,ran//2)
            func(x+ran//2,y+ran//2,ran//2)
            print(")",end='')
            return
        else:
            print(start2,end='')
            return
                

n=int(input())
arr=[list(map(int,input())) for _ in range(n)]

start=arr[0][0] # 처음에 start랑 다 같으면 그냥 0 또는 1, 아니면 분할정복 시행
cnt=0
flag=False

for i in range(n):
    for j in range(n):
        if arr[i][j]==start:continue
        else:
            flag=True
            break
    if flag:
        break

if flag:
    print("(",end='')
    func(0,0,n//2)
    func(0,n//2,n//2)
    func(n//2,0,n//2)
    func(n//2,n//2,n//2)
    print(")",end='')
else:
    print(start,end='')