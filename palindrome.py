a =int(input("Enter a number to check palindrome: "))
rev=0
temp=a
while a!=0:
    b=a%10
    rev=rev*10+b
    a=a//10

if rev==temp :
    print("Entered num is palindrome")
else:
    print("Entered num is not palindrom")
