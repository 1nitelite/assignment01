"""
Title: MadLibs with User Prompts
Desc: This script asks the user for different information and reads back a MadLib story with their answers
Change Log: (Who, When, What)
NToulas, 2022-Apr-21, Created file, added header
"""

# start of main body
user_name = input("Hello! What's your name? ")
print("It's very nice to meet you, " +  user_name + "!")
input("Would you like to play a game? ")
print("Awesome! Let's play! First, tell me a little bit about yourself, using one word answers.")

# user prompted survey
adjective = input("Tell me one word that describes yourself. ")
food = input("What is your favorite food? ")
city = input("What city are you from? ")
color = input("What is your favorite color? ")
hobby = input("What is your favorite thing to do in your free time? ")
animal = input("What is your favorite animal? ")
secAdjective = input("Tell me another word that describes yourself. ")
dreamCity = input("What city would you like to visit? ")
retire = input("Lastly, what year would you like to retire? ")

# performs operation to calculate number of years until retirement
# converts string to integer then back to string
yearsToRetire = str(int(retire)-2022)

# adds user-prompted answers and prints out MadLib story
input("Now I'm going to write a short story about you. Are you ready? ")
print("Let's do it! Here it is:")
print("Today I met the most " + adjective + " person and their name is " + user_name + ". ")
print("We met while searching for a " + food + " restaurant in our hometown of " + city + ". ")
print("You told me that you " + hobby + " for a living and I thought that was " + secAdjective + "! ")
print("In about " + yearsToRetire + " years, your dream is to save enough money to live in " + dreamCity + " with your pet " + animal + ". ")
print("Wow, you’re such an inspiration!")
print("I hope you enjoyed that story! Have a nice day!")
