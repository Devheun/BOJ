t=int(input())
cnt=0 # 중첩 몇번 됐는지 체크하는 변수
result=0 # 점수 저장 변수

for i in range(t):
    s=input()
    for j in s:
        if j=='O':
            cnt+=1
            result+=cnt
        else:
            cnt=0
    print(result)
    result=0
    cnt=0
            