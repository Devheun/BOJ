# 달팽이는 올라가고 싶다

import math

a,b,v=map(int,input().split())


cnt=a-b
cnt2=v-a
cnt3=int(math.ceil(cnt2/cnt)) if cnt2>=cnt else cnt2
print(cnt3+1)