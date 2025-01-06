filename="file_handling/data.txt"
vowel="aeiouAEIOU"
consonent="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vowel_count=0
consonent_count=0
other_count=0
upper_count=0
lower_count=0

file=open(filename,'r')
content=file.read()
for i in content:
    if i in vowel:
        vowel_count+=1
    elif i in consonent:
        consonent_count+=1
    else:
        other_count+=1

for i in content:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1


print("vowels count in file :",vowel_count)
#or
print(f"Vowels count in file: {vowel_count}")
print(f"Consonent count in file: {consonent_count}")         
print(f"Other characters count in file: {other_count}")
print(f"Lowercase characters count in file: {lower_count}")
print(f"Upperacse characters count in file: {upper_count}")     