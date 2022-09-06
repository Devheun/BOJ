t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    floor=n%h 
    room_number=n//h
    print(floor*100 + room_number+(100*h if n%h==0 else 1))