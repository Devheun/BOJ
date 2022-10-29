# IOIOI

n=int(input())
m=int(input())
s=list(map(str,input()))

i=1
tmp=0
cnt=0

while i<len(s)-1:
    
    if s[i-1]=='I' and s[i]=='O' and s[i+1]=='I':
        tmp+=1
        if tmp==n:
            cnt+=1
            tmp-=1
        i+=1
    else:
        tmp=0
    i+=1

print(cnt)
        
        
    