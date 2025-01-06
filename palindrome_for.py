a=input("enter a string to check pallindrome: ")
temp=a
rev=a[::-1]
if rev==temp:
    print("PALINDROME")
else:
    print("NOT PALINDROME")

