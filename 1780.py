# 종이의 개수

def func(x,y,ran): # ran is range
    global cnt,cnt_0,cnt_1
    tmp=arr[x][y]
    if ran==1:
        if tmp==-1:
            cnt+=1
        elif tmp==0:
            cnt_0+=1
        elif tmp==1:
            cnt_1+=1
        return
    
    flag=False
    for i in range(x,x+ran):
        for j in range(y,y+ran):
            if arr[i][j]==tmp:continue
            else:
                flag=True
                break
        if flag:
            break
    if not flag:
        if tmp==-1:
            cnt+=1
        elif tmp==0:
            cnt_0+=1
        elif tmp==1:
            cnt_1+=1
        return
    else:
        func(x,y,ran//3)
        func(x,y+ran//3,ran//3)
        func(x,y+ran//3*2,ran//3)
        func(x+ran//3,y,ran//3)
        func(x+ran//3,y+ran//3,ran//3)
        func(x+ran//3,y+ran//3*2,ran//3)
        func(x+ran//3*2,y,ran//3)
        func(x+ran//3*2,y+ran//3,ran//3)
        func(x+ran//3*2,y+ran//3*2,ran//3)
        return

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

cnt=0
cnt_0=0
cnt_1=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==-1:
            cnt+=1
        elif arr[i][j]==0:
            cnt_0+=1
        elif arr[i][j]==1:
            cnt_1+=1

if cnt and not cnt_0 and not cnt_1:
    print(1)
    print(0)
    print(0)
elif cnt_0 and not cnt and not cnt_1:
    print(0)
    print(1)
    print(0)
elif cnt_1 and not cnt and not cnt_0:
    print(0)
    print(0)
    print(1)
else:
    cnt,cnt_0,cnt_1=0,0,0
    func(0,0,n//3)
    func(0,n//3,n//3)
    func(0,n//3*2,n//3)
    func(n//3,0,n//3)
    func(n//3,n//3,n//3)
    func(n//3,n//3*2,n//3)
    func(n//3*2,0,n//3)
    func(n//3*2,n//3,n//3)
    func(n//3*2,n//3*2,n//3)
    print(cnt)
    print(cnt_0)
    print(cnt_1)