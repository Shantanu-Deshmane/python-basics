def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

def series(n):
    total=0
    for i in range(n+1):
        total+=1/fact(i)
    return total

n=int(input("enter a number: "))
result=series(n)
print(f"sum of the series of n={n} is {result}")