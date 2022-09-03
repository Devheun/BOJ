# 알파벳 찾기

s=input()
check=[-1]*26

for i in range(len(s)):
    if(check[ord(s[i])-97]==-1):
    	check[ord(s[i])-97]=i

for j in check:
    print(j,end=' ')
    
