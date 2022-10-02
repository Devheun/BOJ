# 이중 우선순위 큐
import heapq,sys

t=int(sys.stdin.readline().rstrip())
for _ in range(t):
    k=int(sys.stdin.readline().rstrip())
    q=[]
    q_max=[]
    visited=[False]*1000001
    for i in range(k):
        oper,value=sys.stdin.readline().rstrip().split()
        if oper=='I':
            heapq.heappush(q,(int(value),i))
            heapq.heappush(q_max,(-int(value),i))
            visited[i]=True
        else:		# 삭제
            if value == "1" :
                while q_max and not visited[q_max[0][1]] : #visited로 min_heap에서 삭제된 값 여기서 삭제하도록
                    heapq.heappop(q_max)
                if q_max: #max_heap에서 최댓값 지우기 (위의  while문은 삭제됐어야 할 값들 제거해주는 것)
                    visited[q_max[0][1]]=False
                    heapq.heappop(q_max)
            else :
                while q and not visited[q[0][1]]: # visited로 max_heap에서 삭제된 값 여기서도 삭제되도록
                        heapq.heappop(q)
                if q: #min_heap에서 최댓값 지우기
                    visited[q[0][1]]=False
                    heapq.heappop(q)
    while q_max and not visited[q_max[0][1]]:
        heapq.heappop(q_max)
    while q and not visited[q[0][1]]:
        heapq.heappop(q)
    if q_max and q:
        print(-q_max[0][0],q[0][0])
    else:print("EMPTY")