a=int(input("Enter a number: "))
def prime(a):
    if a<=1:
        return "NOT PRIME"
    elif a==2:
        return "PRIME"
    else:
        for i in(2,(a//2)+1):
            if a%2==0:
                return ("PRIME")
            else:
                return ("NOT PRIME")

print(prime(a))

    
