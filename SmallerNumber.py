a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=int(input("Enter your third number:"))

if a < b and a < c:
    print("a is smaller")
elif b < a and b < c:
    print("b is smaller")
else:
    print("c is smaller")
