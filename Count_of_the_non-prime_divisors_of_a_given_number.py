def p(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
a=int(input())
c=0
b=0
for i in range(1,a+1):
    if(a%i==0):
        if(p(i)):
            c+=1
        else:
            b+=1
print(b+1)