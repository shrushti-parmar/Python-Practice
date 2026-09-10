#21
a=int(input("Enter 1st side length:"))
b=int(input("Enter 2nd side length:"))
c=int(input("Enter 3rd side length:"))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Valid Triangle")
        elif a==b==c:
            print("Equilateral Triangle")
        elif a==b or a==c or b==c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")