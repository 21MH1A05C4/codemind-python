n=int(input())
a=list(map(int,input().split()))
min=a[0]
c=0
for i in range(0,n):
    if min>a[i]:
        min=a[i]
while min:
    c=0
    for j in range(0,n):
        if(a[j]%min==0):
            c+=1
    if(c==n):
        print(min)
        break
    min-=1