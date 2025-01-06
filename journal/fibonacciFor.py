limit=10
a=0
b=1
print(a,b,end=" ")
for i in range(2,limit+1):
    c=a+b
    a=b
    b=c
    print(c,end="")