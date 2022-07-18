s1=int(input())
s2=int(input())
a=[]
s=0
for n in range(s1):
    a.append([int(y) for y in input().split()])
for i in a:
    for j in i:
        s+=j
print(s)