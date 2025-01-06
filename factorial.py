def fact():
    try:
        n="dfhj"
        a=1
        for i in range(1,n+1):
            a=a*i
        print(a)

    except TypeError as e:
        print("Error Occured: ",e)

fact()
