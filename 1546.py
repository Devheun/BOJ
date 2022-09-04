# 평균

N=int(input())
scores=list(map(int,input().split()))
M=max(scores)

new_scores=[]

for i in scores:
    i=i/M*100
    new_scores.append(i) # 리스트에 값 추가

print(sum(new_scores)/len(new_scores))