n=int(input())
a=list(map(int,input().split()))
o=0
for i in a:
    if(i%2!=0):
        o+=1
if(o<=2):
    print("YES")
else:
    print("NO")