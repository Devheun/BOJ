# 이중 우선순위 큐
import heapq

t=int(input())
for _ in range(t):
    k=int(input())
    q=[]
    for _ in range(k):
        oper,value=input().split()
        if oper=='I':
            heapq.heappush(q,int(value))
        else :		# 삭제
            if len(q) > 0 :
                if value == "1" :
                    q.pop(q.index(heapq.nlargest(1, q)[0]))
                else :
                    heapq.heappop(q)
    if q:
        print(max(q),q[0])
    else:
        print("EMPTY")
            