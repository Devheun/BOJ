L=int(input())
string=input()
cnt=0

for i in range(len(string)):
    cnt+=(ord(string[i])-96)*(31**i)
    cnt%=1234567891

print(cnt)
    