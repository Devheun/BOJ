# 블랙잭

n,m=map(int,input().split())
numbers=list(map(int,input().split()))
check=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            tmp=numbers[i]+numbers[j]+numbers[k]
            if tmp<=m:check.append(tmp)
            tmp=0
    
print(max(check))