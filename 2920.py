# 음계

cnt=0

numbers=list(map(int,input().split()))
for i in range(len(numbers)-1):
    if numbers[i]<numbers[i+1]:
        cnt+=1
    elif numbers[i]>numbers[i+1]:
        cnt-=1
    

if cnt==7:
    print("ascending")
elif cnt==-7:
    print("descending")
else:print("mixed")