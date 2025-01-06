a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))

largest= a if a>=b and a>=c else b if b>=a and b>=c else c
smallest= a if a<=b and a<=c else b if b<=a and b<=c else c

print(f"{largest} is largest number and {smallest} is smallest number")

