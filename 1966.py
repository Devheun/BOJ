# 프린터 큐

from collections import deque

t=int(input())
arr=deque()
cnt=1

for _ in range(t):
    n,wonder=map(int,input().split()) # n은 문서의 개수, wonder는 궁금한 문서가 큐에 몇번째에 놓여있는지
    tmp=list(map(int,input().split()))
    for i in range(n):
    	arr.append((i,tmp[i])) # 처음 놓은 순서와 중요도를 튜플로 저장
    
    while arr:
        if arr[0][0]==wonder and arr[0][1]==max(arr,key=lambda i:i[1])[1]:
        	print(cnt);break
        elif arr[0][1]!=max(arr,key=lambda i:i[1])[1]:
        	arr.append(arr.popleft()) # 중요도가 높은게 있을 때는 뒤로 재배치
        elif arr[0][1]==max(arr,key=lambda i:i[1])[1]: # 맨 앞에 문서가 중요도가 젤 높을땐 인쇄
            arr.popleft()
            cnt+=1
    cnt=1
    arr.clear()