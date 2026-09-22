#Q1
string=input("Enter a string: ")
count=0
for i in string:
    if i.isupper():
        count=count+1
print(count)
count=0
for i in string:
    if i.islower():
        count=count+1
print(count)
count=0
for i in string:
    if i.isdigit():
        count=count+1
print(count)
space_count = 0
for char in string:
   if char == " ":
       space_count += 1
print(f"Number of spaces: {space_count}")



# #2

fail_count = 0
pass_count = 0
good_count = 0
excellent_count = 0

for i in range(1, 11):
    marks = int(input(f"Enter marks for student {i} (0-100): "))

    if marks < 35:
        print("Fail")
        fail_count += 1
    elif marks <= 49:
        print("Pass")
        pass_count += 1
    elif marks <= 74:
        print("Good")
        good_count += 1
    elif marks <= 100:
        print("Excellent")
        excellent_count += 1
    else:
        print("Invalid marks entered.")


print("Fail:", fail_count)
print("Pass:", pass_count)
print("Good:", good_count)
print("Excellent:", excellent_count)



# #5

sentence = input("Enter a sentence: ")

words = sentence.split()

short_count = 0
medium_count = 0
long_count = 0


for word in words:
   
    clean_word = word.strip(".,!?;:\"'")
    word_length = len(clean_word)
    
    if word_length <= 3:
        category = "Short"
        short_count += 1
    elif word_length <= 6:
        category = "Medium"
        medium_count += 1
    else:
        category = "Long"
        long_count += 1
        
    print(f"Word: '{clean_word}' | Length: {word_length} | Category: {category}")

print("Short words:", short_count)
print("Medium words:", medium_count)
print("Long words:", long_count)

