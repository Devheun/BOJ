# 색종이 만들기



    
        

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

cnt_b=0
cnt_w=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1: # 파랑
            cnt_b+=1
        elif arr[i][j]==0: #하양
            cnt_w+=1
            
if cnt_b==n*n: # 전부 다 파랑
    print(0)
    print(1)
    exit()
elif cnt_b==0: # 전부 다 하양
    print(1)
    print(0)
    exit()
    
cnt_w=0
cnt_b=0

def func(x,y,n):
    global cnt_w,cnt_b
    tmp=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp!=arr[i][j]: # 한개라도 색깔이 다르면
                func(x,y,n//2)
                func(x,y+n//2,n//2)
                func(x+n//2,y,n//2)
                func(x+n//2,y+n//2,n//2)
                return
    if tmp==0: # 하양색일때
        cnt_w+=1
    else:
        cnt_b+=1
    

func(0,0,n)
print(cnt_w)
print(cnt_b)
        
            
        