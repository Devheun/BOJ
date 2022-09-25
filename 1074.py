# Z

def func(x,y,n):
    global visited
    if n==2: # 2*2 정사각형 모양일때
        for i in range(2):
            for j in range(2):
                if x+i==r and x+j==c:
                    print(visited+i+j)
                    exit()
                else:visited+=1
        return
    else:
        func(x,y,n//2)
        func(x,y+n//2,n//2)
        func(x+n//2,y,n//2)
        func(x+n//2,y+n//2,n//2)
        return

visited=0
n,r,c=map(int,input().split()) # r,c는 0행부터 시작
func(0,0,2**n) # 시작점,범위
