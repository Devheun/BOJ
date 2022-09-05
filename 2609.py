# 최대공약수와 최소공배수

def gcd_f(a,b):
    while b>0:
        a,b=b,a%b
    return a

def lcm_f(a,b):
    return a*b/gcd

a,b=map(int,input().split())
gcd=gcd_f(a,b)
lcm=lcm_f(a,b)
print(int(gcd))
print(int(lcm))