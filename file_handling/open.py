file= open ("file_handling/demo.txt",'r')
result=file.read()

print(result)

upper=0
lower=0
for  i in result:
    if i.isupper():
        upper=upper+1
    else:
        lower+=1
print("Uppercase characters= ",upper)    
print("Lowercase characters= ",lower)    