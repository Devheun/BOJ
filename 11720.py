N=int(input())
numbers=list(map(int,input())) # 공백 없이 주어졌을때

result=0
for i in numbers:
    result+=i

print(result)
