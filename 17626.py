# Four Squares

n=int(input())
d=[0,1,2,3] # d[1]=1 d[2]=2 d[3]=3

for i in range(4,n+1):
    tmp=1e9
    j=1
    
    while (j**2)<=i:
        tmp=min(tmp,d[i-j**2])
        j+=1
    d.append(tmp+1)
print(d[n])
    
    
