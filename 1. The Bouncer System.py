# 1. The Bouncer System
'''Day 1: The Bouncer System

Scenario: You are programming the digital entry gate for a restricted venue. The gate needs to automatically evaluate guests based on their age before letting them pass.
Rules:

    If the user's age is less than 18, print "Access Denied: Underage."

    If the user's age is between 18 and 21 (inclusive), print "Access Granted: Limited Pass (No alcohol allowed)."

    If the user's age is greater than 21, print "Access Granted: Full Access Pass."

    Implement data type safety handling to prevent the program from crashing if a user inputs text instead of digits.
'''
def calculate_age(age):
    if age < 0:
        return "Invalid Age"
    elif age < 5:
        return "free"
    elif age >=5 and age <= 17:
        return "$10"
    else:
        return "$20"

try:
    user_age = int(input("Enter the Age: "))
    price = calculate_age(user_age)

    print(f"The price of the ticket for age {user_age} is: {price}")

except ValueError:
    print("Error! Please enter a valid age in numbers")
