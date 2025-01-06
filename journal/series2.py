def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)

print(factorial(4))
# a=int(input("Enter a number: "))
# for i in range(1,a+1):
#     result=1+(1/factorial(i))
#     print(result)