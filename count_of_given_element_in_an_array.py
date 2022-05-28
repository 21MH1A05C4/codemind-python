a=int(input())
b=list(map(int,input().split()))
d=int(input())
c=0
for i in b:
    if i==d:
        c+=1
print(c)