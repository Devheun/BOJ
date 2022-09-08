# 체스판 다시 칠하기 8*8 크기 잘라낸 뒤 칠해야할 정사각형 개수의 최솟값

n,m=map(int,input().split())
chess=[list(input()) for _ in range(n)]
result=[]

for i in range(n-7):
    for j in range(m-7):
        count1=0 # W로 시작할 경우 바뀐 체스판의 갯수
        count2=0 # B로 시작할 경우 바뀐 체스판의 갯수
        for x in range(i,i+8): # 8*8 보드 하나씩 체크
            for y in range(j,j+8):
                if (x+y)%2==0:
                    if chess[x][y]!='W':count1+=1
                    elif chess[x][y]!='B':count2+=1
                else:
                    if chess[x][y]!='B':count1+=1
                    elif chess[x][y]!='W':count2+=1
        result.append(count1)
        result.append(count2)

print(min(result))
                    