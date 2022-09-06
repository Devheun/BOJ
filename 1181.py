# 단어 정렬

n=int(input())
check1=[]
check2=[]

for _ in range(n):
    check1.append(input())

for i in check1: # 중복된 값 제거
    if i not in check2:
        check2.append(i)

check2.sort() # 알파벳 순으로 정렬
check2=sorted(check2,key=lambda i:len(i)) # 짧은 순으로 정렬
for i in check2:
    print(i)