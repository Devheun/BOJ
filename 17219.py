# 비밀번호 찾기
import sys

arr={}

n,m=map(int,input().split())
for _ in range(n):
    site,pw=sys.stdin.readline().rstrip().split()
    arr[site]=pw
    
for _ in range(m):
    want_pw=sys.stdin.readline().rstrip()
    print(arr[want_pw])