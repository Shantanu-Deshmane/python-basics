a = int(input("Enter a number :"))

if a <= 0:
    print("please enter a positive number !")
elif a == 1:
    is_prime=False
else:
    is_prime = True
    for i in range (2, int(a ** 0.5) + 1):
        if a % i == 0:
            is_prime = False
            break
    
if is_prime:
    print("PRIME")
else:
    print("NOT PRIME")