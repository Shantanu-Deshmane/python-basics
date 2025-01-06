a=int(input("Enter a number to check palindrome or not: "))
temp=a
result=0
while a>0:
    b=a%10
    result=result*10+b
    a=a//10
if temp==result:
    print("Entered number is PALINDROME")
else:
    print("Entered number is NOT PALINDROME")
