# Z

def func(x,y,n):
    global visited
    if x==r and y==c:
        print(visited)
        exit()
    elif n==1: #최소단위 1X1 짜리
        visited+=1
        return
    elif not (x<=r<x+n and y<=c<y+n): # 지금 찾는 범위에 r과c가 없을 시
        visited+=n*n
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
