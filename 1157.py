# 단어 공부 (가장 많이 사용된 알파벳이 무엇인지, 대소문자 구분 X)

string=input()
string=string.upper()

check=[0]*26
for i in string:
    check[ord(i)-65]+=1

tmp1=max(check)
index1=check.index(tmp1) # tmp1의 인덱스 값 가져오기
check.remove(tmp1)
tmp2=max(check)
index2=check.index(tmp2)

if tmp1==tmp2:
    print("?")
else:
    print(chr(65+index1))


