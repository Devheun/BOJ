# 파도반 수열

d=[0]*101
d[1],d[2],d[3],d[4],d[5]=1,1,1,2,2
for i in range(6,101):
    d[i]=d[i-1]+d[i-5]

t=int(input())
for _ in range(t):
    n=int(input())
    print(d[n])
    
    