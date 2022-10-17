# 잃어버린 괄호

s=input()
s=s.replace('+',',').replace('-',',-')
s=list(map(int,s.split(',')))


result=0
tmp=0
i=0
flag=False
while i<=len(s)-1:
    if s[i]==0:
        i+=1
        continue
    elif flag==False and s[i]>0:
        result+=s[i]
        i+=1
    elif flag==True and s[i]>0:
        tmp+=s[i]
        i+=1
    elif flag==False and s[i]<0:
        flag=True
        tmp+=(-s[i])
        i+=1
    else:
        tmp+=(-s[i])
        i+=1

result-=tmp
print(result)