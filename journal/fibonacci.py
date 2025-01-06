limit=int(input("Enter a limit: "))
a=0
b=1
list=[a,b]
count=2
while count<limit:
    c=a+b
    a=b
    b=c
    list.append(c)
    count+=1
print(list)