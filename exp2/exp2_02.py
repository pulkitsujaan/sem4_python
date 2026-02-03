# Recursive Approach
def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)

def factIterr(n):
    if(n==0):
        return 1
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

print(fact(6))
print(fact(6))