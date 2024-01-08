'''basic factorial function'''
def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)
print(fact(5))