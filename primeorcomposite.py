num=int(input("Enter a number:"))

if num<=1:
    print("Neither Prime Nor Composite")
elif num==2:
    print("Prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Composite Number")
            break
        else:
            print("Prime Number")
