a=input()
c=0
for i in a:
    if i in ' ':
        c+=1
if c>=0:
    print(c+1)
else:
    print(-1)