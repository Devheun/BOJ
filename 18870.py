# 좌표 압축
import sys

n=int(input())
coor=list(map(int,sys.stdin.readline().rstrip().split()))
tmp=sorted(coor)
tmp2=dict()

cnt=0
if n==1: # 예외처리
    print(0)
    exit()

tmp2[tmp[0]]=cnt

for i in range(1,len(tmp)):
    if tmp[i]>tmp[i-1]:
        cnt+=1
        tmp2[tmp[i]]=cnt
    else: # 값이 똑같을 때
        tmp2[tmp[i]]=cnt

for j in coor:
    print(tmp2[j],end=' ')
        
