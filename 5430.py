# AC
from collections import deque


t=int(input())

for _ in range(t):
    p=input() # 수행할 함수 p
    n=int(input()) # 배열에 들어있는 수의 개수
    arr=input() # 배열에 들어있는 정수
    
    arr=arr.replace('[','') # 입력받기 위한 전처리 과정
    arr=arr.replace(']','')
    arr=arr.replace(',',' ')
    arr=deque(map(int,arr.split()))
    
    err_flag=False
    reverse_flag=False
    cnt=0

    for i in range(len(p)):
        if p[i]=='R':
            cnt+=1 # R이 연달아 몇번 나오는지 체크
            if cnt%2==1:
                reverse_flag=True # 뒤집을 게 남았다.
            else:reverse_flag=False    
        elif p[i]=='D': 
            if arr and not reverse_flag:
                arr.popleft()
            elif arr and reverse_flag:
                arr.pop()
            else:
                print("error")
                err_flag=True
                break
                
    if not err_flag and not reverse_flag:
        arr=list(arr)
        print('['+','.join(map(str,arr))+']')
    elif not err_flag and reverse_flag:
        arr=list(arr)
        arr.reverse()
        print('['+','.join(map(str,arr))+']')
        
            