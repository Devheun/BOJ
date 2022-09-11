# 부녀회장이 될테야

t=int(input())
arr=[[0]*15 for _ in range(15)]
for i in range(1,15):
    arr[0][i]=i



for x in range(1,15):
    for y in range(1,15):
        for z in range(1,y+1):
            arr[x][y]+=arr[x-1][z]
            


for _ in range(t):
    k=int(input())
    n=int(input())
    print(arr[k][n])

    