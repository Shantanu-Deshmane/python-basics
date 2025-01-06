filename="file_handling/demo.txt"
file= open (filename,'r')
result=file.read()
upper=0
lower=0
for  i in result:
    # print(i.isupper())
    if i.isupper():
        upper+=1
        
    else:
        lower+=1
print("Uppercase characters= ",upper)    
print("Lowercase characters= ",lower)    