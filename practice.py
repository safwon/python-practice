import random
*******tips calculator*******

print("Welcome to the tip calclulator.")
total_bill = float(input("What was the total bill? $"))
split_bill = int(input("How many people to split the bill? "))
tips_percentage = int(input(
    "What percentage tip would you like to give? 10, 12 or 15? "))

people_split = float(total_bill/split_bill)
tips_result = float(((people_split) * (tips_percentage/100)))
total = float(people_split + tips_result)
final = round(total, 2)
print(f"You will pay each {final}")


******age calculator******

age = input("What is your current age? ")
expect_to_live = input("how many years you will desire to live? ")

age_int = int(age)
expected_int = int(expect_to_live)

left_age = (expected_int-age_int)

days = left_age*365
weeks = left_age*56
months = left_age*12

print(f"You have {left_age} years left")
print(f"You have left {days} days, {weeks} weeks , {months} months")


even or odd

number = int(input("what is the number "))

if (number % 2) == 0:
    print("Even")
else:
    print("odd")

*******BMI calculator*******

weight = float(input("what is your weight in kg"))
height = float(input("What is your height in meter"))

result = round(float(weight/(height**2)))

if result <= 18.5:
    print(f"your BMI is {result}, you are underweight")
elif result <= 25:
    print(f"your BMI is {result}, you have normal weight")
elif result <= 30:
    print(f"your BMI is {result}, you are slightly overweight")
elif result <= 35:
    print(f"your BMI is {result}, you are obese")
elif result > 35:
    print(f"your BMI is {result}, yout are clinically obese")
else:
    print("try again")


leap year

year = int(input("What is the year you want to know? "))

if (year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("Leap year")

    else:
        print("Leap year")
else:
    print("Not a leap year")


*******ticket and picture*******

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("$5")
    elif age <= 18:
        bill = 7
        print("$7")
    elif age >= 46 and age <= 56:
        bill = 0
        print("You are free of charge: $0")
    elif age > 18:
        bill = 12
        print("$12")

    photo = input("if you want photo type Y and if not type N: ")
    if photo == "Y":
        bill += 3
        print(f"Your total is ${bill}")
    if photo == "N":
        print(f"${bill}")
else:
    print("can not ride")


*******pizza order program*******

pizza_size = input("To Order pizza press Small:S, Medium:M, Large:L ")

if pizza_size == "S":
    bill = int(15)
    print("$15")
elif pizza_size == "M":
    bill = int(20)
    print("$20")
elif pizza_size == "L":
    bill = int(25)
    print("$25")
else:
    print("You have not press any")

pepperoni = input("Do you want to add Pepperoni Y/N: ")
if pepperoni == "N":
    print(f"Your bill is ${bill}")
elif pepperoni == "Y":
    Pepperoni_size = input("Give the size of Pepperoni S, M:  ")
    if Pepperoni_size == "S":
        bill += 2
        print(f"Your Bill is ${bill}")
    elif Pepperoni_size == "M":
        bill += 3
        print(f"Your Bill is ${bill}")
else:
    print("Enjoy our pizza")
Cheese = input("Do you want extra cheese Y/N:")
if Cheese == "Y":
    bill += 1
    print(f"Your total is ${bill}")
else:
    print("Enjoy our pizza")


*******love calclulator*******


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))


if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


********Randomization******


toss = random.randint(0, 1)

if toss == 1:
    print(f"Heads")
else:
    print(f"Tails")


******who will pay the bill*******


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# start = 0
# length = len(names)
# random_name = random.randrange(start, length)
# guess = names[random_name]

# different way
length = len(names)
random_name = random.randint(0, length-1)
guess = names[random_name]
print(f"{guess} is going to buy the meal!")


people = random.choice(names)
print(f"{people} is going to buy the meal!")


*****matrix game*****

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

# map[vertical - 1][horizontal - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")


****** Rock paper scisssors*******


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

games = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Invalid number")
else:
    print(games[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer choose:")
    print(games[computer_choice])

    if computer_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 0 and computer_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("Its draw!")


*****Average calculator*****
# can't use sum(),len().
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights[n])


# # total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height

# # total_student = len(student_heights)
nums_of_student = 0
for students in student_heights:
    nums_of_student += 1

# # average = round(total_height/total_student)
average = round(total_height/nums_of_student)
print(average)


# ********MAX value of the list*********
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_scores)

# # max_value = max(student_scores)
highest = 1
for score in student_scores:
    if score > highest:
        highest = score

# print(max_value)
print(f"The highest score is: {highest}")

*********Sum of even number**********
total = 0
for even in range(2, 101, 2):
    total += even
print(total)

*******fizzbuzzz*************

for value in range(1, 101):
    if value % 3 == 0 and value % 5 == 0:
        print("FizzBuzz")
    elif ((value % 3) == 0):
        print("fizz")
    elif ((value % 5) == 0):
        print("Buzz")
    else:
        print(value)


**************PASSword*******************
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []
for char in range(1, nr_letters + 1):
    password += random.choice(letters)


for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))


for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)


print(password)
random.shuffle(password)
print(password)

word = ""
for char in password:
    word += char

print(word)
