a=int(input("Enter a number to check armstrong: "))
length=len(str(a))
temp = a
sum=0
while a!=0:
    b=a%10
    sum=sum+(b**length)
    a=a//10

if temp == sum:
    print("Entered Number is ARMSTRONG")
else:
    print("Entered Number is NOT ARMSTRONG")
    
