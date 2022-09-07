# 소수 찾기 (1000 이하의 자연수)

n=int(input())
array=list(map(int,input().split()))
numbers=[]

for i in array:
    if i==1:continue # 1은 예외처리
    elif i==2:numbers.append(2) #2도 예외
    elif i==3:numbers.append(3) # 3도 예외처리
    tmp=int(i**(1/2))
    for j in range(2,tmp+1):
        if i%j==0:break # 소수가 아닐때
        if (j==tmp) and (i%j!=0):
            numbers.append(i) # 소수일 때

print(len(numbers))
    
        
                   