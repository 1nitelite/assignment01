"""
Title: MadLibs with User Prompts
Desc: This script asks the user for different information and reads back a MadLib story with their answers
Change Log: (Who, When, What)
NToulas, 2022-Apr-21, Created file, added header
NToulas, 2022-Apr-26,
"""

# start of main body
user_name = input("Hello! What's your name? ")
# input("It's very nice to meet you, " +  user_name + "! Would you like to play a game? ")
# print("Awesome! Let's play! First, tell me a little bit about yourself, using one word answers.")

# user prompted survey
adjective = input("Tell me one word that describes yourself. (Like an adjective) ")
# food = input("What is your favorite food? ")
# city = input("What city are you from? ")
# color = input("What is your favorite color? ")
# hobby = input("What is your favorite thing to do in your free time? ")
# animal = input("What is your favorite animal? ")
# secAdjective = input("Tell me another word that describes yourself. ")
dreamCity = input("What city would you like to visit? ")
retire = input("Lastly, what year would you like to retire? ")

# performs operation to calculate number of years until retirement
# converts string to integer then back to string
yearsToRetire = str(int(retire)-2022)

# adds user-prompted answers and prints out MadLib story
# input("Now I'm going to write a short story about you. Are you ready? ")
a = "Let's do it! Here it is:"
b = "Today I met the most"
c = "person and their name is"
d = ".\nWe met while searching for a"
e = "restaurant in our hometown of"
f = ".\nYou told me that you"
g = "for a living and I thought that was"
h = "!\nIn about"
i = "years, your dream is to save enough money to live in"
j = "with your pet"
k = ".\nWow, you’re such an inspiration!\nI hope you enjoyed that story! Have a nice day!"
# print(a,b,adjective,c, user_name, d, food, e, city, f, hobby, g, secAdjective, \
#       h, yearsToRetire, i, dreamCity, j, animal, k)
print(a,b,adjective,c,user_name,h, yearsToRetire, i, dreamCity, k)