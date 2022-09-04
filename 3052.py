# 나머지

cnt=0
check=set()

for _ in range(10):
    number=int(input())%42
    check.add(number) # set에 원소 하나씩 추가 -> add

print(len(check))
