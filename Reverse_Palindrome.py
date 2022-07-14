def pali(n):
    return(rev(n)==n)
def rev(n):
    rev=0
    while(n):
        rev=rev*10+n%10
        n//=10
    return rev
n=int(input())
r=0
while(n):
    r=rev(n)
    n=n+r
    if(pali(n)):
        print(n)
        break