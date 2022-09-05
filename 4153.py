# 직각삼각형

while True:
    tmp=list(map(int,input().split()))
    if(tmp[0]==0 and tmp[1]==0 and tmp[2]==0):break
    small=min(tmp)
    
    tmp.remove(small)
    small2=min(tmp)

    if (small**2 + small2**2) == ((max(tmp))**2):
        print("right")
    else:print("wrong")
        
    
    