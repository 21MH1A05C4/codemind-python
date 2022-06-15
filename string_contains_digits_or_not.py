n=int(input())
for i in range(1,n+1):
    a=input()
    c=0
    for j in a:
        if j in '1234567890':
            c+=1
    if c==0:
        print('No')
    else:
        print('Yes')