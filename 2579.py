# 계단 오르기

n=int(input())
stair=[0]*(n+1)
d=[[0]*3 for _ in range(301)]

for i in range(1,n+1):
    score=int(input())
    stair[i]=score

d[1][1]=stair[1] # 첫번째 계단

for i in range(2,n+1):
    d[i][2]=d[i-1][1]+stair[i] #이전 계단 밟고 2칸 연속 밟은것
    d[i][1]=max(d[i-2][1],d[i-2][2])+stair[i]
    
print(max(d[n][1],d[n][2]))
    