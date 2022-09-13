# 균형잡힌 세상
import sys

while True:
    string=sys.stdin.readline().rstrip()
    if string=='.':
        break
    
    arr=[]
    
    for i in string:
        if i=='[' or i=='(':
            arr.append(i)
        elif i==']':
            if len(arr)>0 and arr[-1]=='[':
                arr.pop()
            else:
                arr.append(']')
                break

        elif i==')':
            if len(arr)>0 and arr[-1]=='(':
                arr.pop()
            else:
                arr.append(')')
                break

                
    if len(arr)==0:print('yes')
    else:print('no')
        
