#11

# year=int(input("Enter year: "))
# if year%400==0:
#     print(f"{year} is a leap year.")
# elif year%4==0 and year%100!=0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")




#12
# char=input("Enter a character : ")
# if char.isupper():
#     print("upper case")
# elif char.islower():
#     print("lower case")
# elif char.isdigit:
#     print("digit")
# else:
#     print("special character")

#13
# ch = input("Enter a character: ")

# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print("Vowel")
# elif ch.isalpha():
#     print("Consonant")
# else:
#     print("Invalid input")

# #14
# cost_price=int(input("Enter cost price: "))
# selling_price=int(input("Enter selling price: "))
# if selling_price>cost_price:
#     print(f"Profit is {selling_price-cost_price}")
# if selling_price<cost_price:
#     print(f"Loss is {cost_price-selling_price}")
# elif selling_price==cost_price:
#     print("No profit and no loss")




#15
# cost_price=int(input("Enter cost price: "))
# selling_price=int(input("Enter selling price: "))
# if selling_price>cost_price:
#     print(f"Profit is {selling_price-cost_price} and Profit percentage is {(selling_price-cost_price)/cost_price * 100}")
# elif selling_price<cost_price:
#     print(f"Loss is {cost_price-selling_price} and Loss percentage is {(cost_price-selling_price)/selling_price * 100}")
# elif cost_price<=0:
#     print("Invalid cost price.")



#16
# units = int(input("Enter electricity units: "))
# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
# print("Electricity Bill = ₹", bill)

# unit=int(input("Enter electricity reading : "))
# if unit>0 and unit<=100:
#     bill=(unit*5)
#     print(f"Electricity bill is {unit}")
# elif unit>100 and unit<=200:
#     bill=(100*5+((unit-100)*7))
#     print(f"Electricity bill is {unit}")
# elif unit>200:
#     bill=(100*5+(100*7)+((unit-200)*10))
#     print(f"Electricity bill is {unit}")


#17
# operation=int(input("Enter a number from the following Operations that you want to perform:\n 1.Additon \n 2.Subtraction \n 3.Multiplication \n 4.Division: "))
# if operation==1 or operation==2 or operation==3 or operation==4:
#     a= int(input("Enter first number: "))
#     b= int(input("Enter second number: "))

#     if operation==1:
#         print(f"Addition is:{a+b}")
#     elif operation==2:
#         print(f"Subtraction is:{a-b}")
#     elif operation==3:
#         print(f"Multiplication is:{a*b}")
#     elif operation==4:
#         if b==0:
#             print("Error! Division by zero is not possible.")
#         else:
#             print(f"division of {a} and {b} is {a/b}")
# else:
#     print("Invalid Operation number.")



#18
# celsius=int(input("Enter celsius: "))
# if celsius>35:
#     print("Hot")
# elif celsius>=26:
#     if celsius<=35:
#         print("Normal")
# elif celsius>=16:
#     if celsius<=25:
#         print("Cold")
# elif celsius>=0:
#     if celsius<=15:
#         print("Very Cold")
# elif celsius<0:
#         print("Freezing")


#19
num=int(input("Enter a number: "))
if num < 0:
    print("Negative")
elif 0 <= num <= 10:
    print("Number is between 0-10")
elif 11 <= num <= 50:
    print("Number is between 11-50")
elif 51 <= num <= 100:
    print("Number is between 51-100")
else:
    print("Number is above 100")

#20
a=int(input("Enter 1st side length:"))
b=int(input("Enter 2nd side length:"))
c=int(input("Enter 3rd side length:"))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Valid triangle")

