#1
# num=int(input("Enter a number: "))
# if num>0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# elif num==0:
#     print("Zero")

#2
# num=int(input("Enter a number: "))
# if num>0:
#     if num%2==0:
#         print("Positive Even")
#     elif num%2==1:
#                 print("Positive Odd")
# if num<0:
#     if num%2==0:
#         print("Negative Even")
#     elif num%2==1:
#                 print("Negative Odd")
# elif num==0:
#     print("Zero")

# #3
# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))
# if num1>num2:
#     print(f"The larger number is {num1}.")
# elif num2>num1:
#     print(f"The larger number is {num2}.")
# elif num1==num2:
#     print("Both are equal.")

#4
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# if num1<num2 and num1<num3:
#       print(f"Smallest number is {num1}.")
# elif num2<num3 and num2<num1:
#       print(f"Smallest number is {num2}.")
# elif num3<num1 and num3<num2:
#       print(f"Smallest number is {num3}.")

#5
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))
# if num1>num2 and num1>num3:
#       print(f"Largest number is {num1}.")
# elif num2>num3 and num2>num1:
#       print(f"Largest number is {num2}.")
# elif num3>num1 and num3>num2:
#       print(f"Largest number is {num3}.")

#6
# num= int(input("Enter a number: "))
# if num/5 and num/11:
#     print(f"{num} is Divisible by both 5 and 11.")
# elif num/5 and num:
#     print(f"{num} is only Divisible by 5.")
# elif num/11:
#     print(f"{num} is only Divisible by 11.")
# else: 
#     print("Divisible by neither.")

#6
# num= int(input("Enter a number: "))
# if num%5==0 and num%11==0:
#     print("Divisble by both 5 and 11.")
# elif num%5==0 and num%11!=0:
#     print("Divisible by only 5.")
# elif num%11==0 and num%5!=0:
#     print("Divisible by only 11.")
# else:
#     print("Divisible by neither.")

#7
# num= int(input("Enter a number: "))
# if num%3==0 and num%7==0:
#     print("Divisble by both 3 and 7.")
# elif num%3==0 and num%7!=0:
#     print("Divisible by only 3.")
# elif num%7==0 and num%3!=0:
#     print("Divisible by only 7.")
# else:
#     print("Divisible by neither.")

#8
# marks=int(input("Enter marks: "))
# if marks<0:
#     print("Invalid marks")
# elif marks>100:
#     print("Invalid marks")
# elif marks>=40:
#     print("Pass")
# elif marks<40:
#     print("Fail")

#9
marks=int(input("Enter marks: "))
if marks>100:
    print("Invalid marks")
elif marks>=90:
    if marks<=100:
        print("Grade A")
elif marks>=80:
    if marks<=89:
        print("Grade B")
elif marks>=70:
    if marks<=79:
        print("Grade C")
elif marks>=60:
    if marks<=69:
        print("Grade D")
elif marks>=40:
    if marks<=59:
        print("Grade E")
elif marks<40:
    if marks>=0:
        print("Fail")
elif marks<0:
    print("Invalid marks.")

#10
age= int(input("Enter age:"))
if age<0:
    print("Invalid age")
elif age<18:
    print("Cannot vote")
elif age>=18 and age<=120:
    print("Can vote")
else:
    print("Reject")