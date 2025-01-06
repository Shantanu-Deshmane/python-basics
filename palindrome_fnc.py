a=int(input("Enter a num to check palindrome or not: "))
rev=0
temp=a
def palindrome(a):
    rev=0
    while a!=0:
        b=a%10
        rev=rev*10+b
        a=a//10
    if rev==temp:
        result="PLAINDROME!!"
        return result
    else:
        result="NOT PLAINDROME!!"
        return result    

print(palindrome(a))
    


    
