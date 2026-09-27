## table of 2
# i = 20
# while i >= 1:
#     if i%2==0:
#         print(i)
#     i = i-1

# i = 10
# while i >= 1:
#     print(i*2)
#     i = i-1

# i=2
# while i<10:
#     print(i)
#     i=i*2

# i=1
# while i<=10:
#     for j in range(1,19):
#         print(i, end=" ")
#     print()
#     i=i+1


###ForLoops Questions in WHILE_LOOP:-


# i=1
# while i<=5:
#     print("Hello", end=" ")
#     print()
#     i=i+1


# i=0
# while i<10:
#     print(i, end=" ")
#     i=i+1

# i=1
# while i<=10:
#     print(i, end=" ")
#     i=i+1

# i=10
# while i>=1:
#     print(i, end=" ")
#     i-=1


# i=5
# while i<=50:
#     print(i, end=" ")
#     i+=5

# i=1
# while i<=10:
#     print(i*5, end=" ")
#     i+=1

# i=2
# while i<=20:
#     print(i, end=" ")
#     i+=2

# i=2
# while i<=20:
#     if i%2==0:
#         print(i, end=" ")
#     i+=1

# i=1
# while i<20:
#     if i%2==1:
#         print(i, end=" ")
#     i+=1

# i=1
# while i<20:
#     print(i, end=" ")
#     i+=2


# i=3
# while i<=18:
#     print(i, end=" ")
#     i+=3

# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     print(i, end=" ")
#     i+=1


# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     if i%2==0:
#         print(i, end=" ")
#     i+=1

# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     if i%2==1:
#         print(i, end=" ")
#     i+=1


# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     if i%3==0:
#         print(i, end=" ")
#     i+=1

# n=int(input("Enter number:"))
# i=1
# while i<=n:
#     if i%3==0 and i%2==0:
#         print(i, end=" ")
#     i+=1

# n=int(input("Enter number:"))
# count=0
# i=1
# while i<=n:
#     if i%2==0:
#         # print(i, end=" ")
#         count=count+1
#     i+=1
# print("Count of numbers that are Even:", count)


# n=int(input("Enter number: "))
# add=0
# i=1
# while i<=n:
#     add=add+i
#     i+=1
# print(add)


# n=int(input("Enter number: "))
# add=0
# i=1
# while i<=n:
#     if i%2==0:
#         print(i, end=" ")
#         add=add+i
#     i+=1
# print()
# print("Sum=" ,add)

# n=int(input("Enter number: "))
# add=0
# i=1
# while i<=n:
#     if i%2==1:
#         print(i, end=" ")
#         add=add+i
#     i+=1
# print()
# print("Sum=" ,add)


# n=int(input("Enter number: "))
# i=1
# while i<=10:
#     print(i*n, end=" ")
#     i+=1

# n=int(input("Enter number: "))
# multiply=1
# i=1
# while i<=n:
#     multiply=multiply*i
#     i+=1
# print(multiply)


# string=input("Enter a string: ")
# i=0
# while i<len(string):
#     print(string[i])
#     i=i+1

# string=input("Enter a string: ")
# i=0
# while i<len(string):
#     print(string[i], end=" ")
#     i=i+1


# string=input("Enter a string: ")
# i=0
# count=0
# while i<len(string):
#     count+=1
#     i=i+1
# print("Number of characters: ", count)


# string=input("Enter a string: ")
# i=0
# count=0
# while i<len(string):
#     if string[i]=="a":
#         count+=1
#     i+=1
# print("Number of times character-`a` appears: ",count)


# string=input("Enter a string: ")
# i=0
# count=0
# while i<len(string):
#     if string[i].isupper():
#         count+=1
#     i+=1
# print("Number of upppercase letters: ",count)


i=1
while i<=3:
    j=1
    while j<=4:
        print("*", end=" ")
        j+=1
    print()
    i+=1
