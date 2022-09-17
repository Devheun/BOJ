# 마인크래프트

n,m,b=map(int,input().split()) # b는 인벤토리의 블럭개수
arr=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    arr.append(tmp)


floor=0
ans=1234567890 # 시간 처음 값 크게!

for i in range(257):
    cnt_large,cnt_small=0,0 #large는 제거하기, small은 놓기
    for j in range(n):
        for k in range(m):
            if arr[j][k]>=i: # 블록이 층수보다 더 크면
                cnt_large+=arr[j][k]-i
            else: # 블록이 층수보다 더 작으면
                cnt_small+=i-arr[j][k]
    
    if cnt_large+b>=cnt_small: # 블럭을 뺀 값 + 원래 가지고 있는 값 >= 블럭을 더한 값
        if ans>=cnt_large*2 + cnt_small: # 최저 시간과 비교
            ans=cnt_large*2 + cnt_small # 시간 갱신
            floor=i
    
print(ans,floor)
                
                
    
    
            
            
            