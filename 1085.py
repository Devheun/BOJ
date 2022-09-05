# 직사각형에서 탈출

x,y,w,h=map(int,input().split())

north=abs(h-y)
south=y
west=x
east=abs(w-x)

print(min(north,south,west,east))
