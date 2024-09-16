# my_range = range(10, 20, 3)

# print(my_range)

# for num in my_range:
#     print(num)

# print("Today is a beautiful day!\nTomorrow will be a great day!")
# print("Hello" + "David")
# print("Hello" + " David")
# print("Hello " + input("What is your name?") + "!")

# name = "Jack"
# print(name)
#
# name = "Angela"
# print(name)

# print(len(input("What is your name?")))

# username = input("What is your name?")
# lenght = len(username)
#
# print(lenght)

# num_hours = "5"
# print("There are " + num_hours + " hours until midnight")

# print("Welcome to the Band Name Generator")
# city = input("What's the name of the city you grew up in?\n")
# pet = input("What is the name of your pet?\n")
# print("your band name could be: " + city + " " + pet)
# print("Hello"[0])

# print(type("David"))
# print(type(589))
# print(type(23.69))
# print(type(True))

# You'll get TypeError by running below code, fix it.
# print("Number of letters in your name: " + str(len(input("Enter your name"))))

# name_ot_the_user = input("Enter your name")
# lenght_of_name = len(name_ot_the_user)
#
# print(type("Number of letters in your name: "))
# print(type(lenght_of_name))
# print("Number of letters in your name: " + str(lenght_of_name))

# print("My age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(6 / 3)
#
# print(6 // 3)

# print(3 * (3 + 3) / 3 - 3)
# bmi = 84 / 1.65 ** 2
# print(bmi)
#
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2))


# score = 0

# User scores a point
# score += 1
# print(score)
# print("Your score is: " + str(score))
# print(f"Your score is  = {score}")


# score = 0
# height = 1.8
# is_winning = True
#
# print(f"Your score is  = {score}.\nYour height is = {height}.\nYou are winning is = {is_winning}.")


# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill in CAD?"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 18 20 "))
# people = int(input("How many people to split the bill? "))
#
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")

# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
#
# if height > 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# number_to_check = int(input("What is the number you want to check"))
# print(number_to_check % 2)


# number_to_check = int(input("What is the number you want to check"))
#
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is yur age? "))
#     if age <= 17:
#         print("You will pay $ 7")
#     else:
#         print("You will pay $ 12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is yur age? "))
#     if age <= 12:
#         print("You will pay $5.")
#     elif age <= 18:
#         print("You will pay $7.")
#     else:
#         print("You will pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is yur age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#       elif age
#     else:
#         bill = 12
#         print("Adult ticket are $12.")
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3  # It is the same as bill = bill + 3
#
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Write a pizza Delivery Program. Based on an user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# # todo: work out how much they need to pay based on their size choise.
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs.")
#
# # todo: work out how much to add to their bill based on their pepperoni choice. (Use nested if statement.)
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# # todo: work out their final amount based on whether if they want extra cheese.
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")
#
# bill2 = float(input("What was the total bill in CAD?"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 18 20 "))
# people = int(input("How many people to split the bill? "))
#
# tip_as_percent = tip / 100
# total_tip_amount = bill2 * tip_as_percent
# total_bill = bill2 + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is yur age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif 45 <= age <= 55:
#         print("You ride for free!")
#     else:
#         bill = 12
#         print("Adult ticket are $12.")
#     wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
#     if wants_photo == "y":
#         # Add $3 to their bill
#         bill += 3  # It is the same as bill = bill + 3
#
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************
# ''')
# print("Welcome to the treasure island.")
# print("Your mission is to find the treasure.")
#
# choice1 = input(print('You\'re at a cross road. Where do you want to go? type "left" or "right"')).lower()
#
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. '
#                     'There is an island in the middle of the lake. '
#                     'Type "wait" to wait for a boat. '
#                     'Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input(
#             "You arrive at the island unharmed. "
#             "There is house with 3 doors. "
#             "One red, one yellow and one blue. "
#             "Which colour do you choose?\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found a treasure. You win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over")
#     else:
#         print("You got attacked by an angry trout. Game Over.")
# else:
#     print("You fell into a hole. Game over.")

#
# weight = 76
# height = 1.77
#
# bmi = weight / (height ** 2)
# print(round(bmi, 2))
#
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("normal weight")
# else:
#     print("underweight")


# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)


# import random

# Define the possible outcomes
# options = ["Heads", "Tails"]

# Randomly select one of the outcomes
# random_string = random.choice(options)
# print(random_string)


# import random
#
# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

# states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticat", "Delaware",
#                      "Florida", "Georgia", "Hawaii"]
#
# states_of_america[2] = "Arizooona"
# states_of_america.append(["Idaho", "Illinois", "Texas"])
# print(states_of_america)

# Banker Roulette
# import random
#
# friends = ["David I.", "M", "David II.", "Rocky"]
#
#
# def get_random_name(friends_list):
#     return random.choice(friends_list)
#
#
# random_name = get_random_name(friends)
# print(f"The randomly selected name is: {random_name}")


# import random
#
# friends = ["David I.", "M", "David II.", "Rocky"]
#
# print(random.choice(friends))


# import random
#
# friends = ["David I.", "M", "David II.", "Rocky"]
#
# random_index = random.randint(0, 3)
# print(friends[random_index])


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#                      "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
#                      "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
#                      "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
#                      "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
#                      "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#                      "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
#                      "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
#                      "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#                      "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#
# num_of_states = len(states_of_america)
#
# print(states_of_america[50])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines",
#                "Apples", "Grapes", "Peaches", "Cherries",
#                "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes",
#           "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes",
#               "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[0][1])









