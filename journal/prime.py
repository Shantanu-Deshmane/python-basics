def checkPrime(a):
    if a<=1:
        return "NOT PRIME"
    elif a==2:
        return "PRIME"
    else:
        for i in range(2,(a//2)+1):
            if a%i!=0:
                return "PRIME"
    return "NOT PRIME"
    

a=int(input("Enter a number: "))
print(checkPrime(a))