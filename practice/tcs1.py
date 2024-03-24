from math import factorial as fac
def comb(n,r):
    return fac(n)//(fac(r)*fac(n-r))
# finding combination nCr without using factorial
def combination(n,r):
    num = 1
    den = 1
    for i in range(min(n-r,r),0,-1):
        num *= n
        den *= i
        n -=1
    return num//den

def question1():
    n = int(input('enter n:'))
    m = int(input('enter m:'))
    p = int(input('enter p:'))
    e = int(input('enter e:'))
    print('ans : ',comb(n,p)*comb(m,e))
# ---------------------------------
# print(combination(5,0))

