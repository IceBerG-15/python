def func(n,ans):
    if n==1:
        return ans+1
    ans +=1
    for i in range(2,n+1):
        ans+=2*i
    return func(n-1,ans)

print(func(7,0))