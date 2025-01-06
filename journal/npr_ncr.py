def fact(num):
    result=1
    while num>0:
        result=result*num
        num=num-1
    return result

def npr(n,r):
    result=fact(n)//fact(n-r)
    return result
def ncr(n,r):
    result=fact(n)//(fact(r)*fact(n-r))
    return result

n=int(input("Enter a value of n: "))
r=int(input("Enter a value of r: "))
print(f"nPr of n={n} and r={r} is {npr(n,r)}")
print(f"nCr of n={n} and r={r} is {ncr(n,r)}")