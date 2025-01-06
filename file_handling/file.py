inputs=int(input("Enter a number of row you want: "))
numbers=[]
even_file="file_handling/even.txt"
odd_file="file_handling/odd.txt"

for i in range(1,inputs+1):
    values=int(input(f"Enter a {i} of {inputs}: "))
    numbers.append(values)
print(numbers)

with open(even_file,'a') as file:
    for i in numbers:
        if i%2==0:
            file.writelines(str(i)+"\n")

with open(odd_file,'a') as file:
    for i in numbers:
        if i%2!=0:
            file.writelines(str(i)+"\n")

    print("data added!!")

with open (even_file,'r') as file:
    data=file.read()
    print("DATA FROM EVEN FILE: \n",data)
with open (odd_file,'r') as file:
    data=file.read()
    print("DATA FROM ODD FILE: \n",data)


