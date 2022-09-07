# 요세푸스 문제 0


queue=[]
n,k=map(int,input().split())
for i in range(1,n+1):
    queue.append(i)
    

print("<",end='')
tmp=k-1
while queue:
    if tmp>=len(queue):
        tmp-=len(queue)
    if tmp<len(queue):
        if len(queue)!=1:
            print(queue[tmp],end=', ')
        elif len(queue)==1:
            print(queue[tmp],end='')
        del queue[tmp]
        tmp=tmp+k-1
print(">")