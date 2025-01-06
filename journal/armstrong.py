def armstrong(a):
    length=len(a)#3
    result=0
    for i in a:
        result=result+(int(i)**length)#res=126 126+3**3
    print(result)

    if a==result:
        return("Number is armstrong")
    else:
        return("Number is not armstrong")


