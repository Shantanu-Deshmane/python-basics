# Print the pattern
for i in range(1, 6):
    result = ""
    for j in range(i):
        result += chr(97 + j)
    print(result)
