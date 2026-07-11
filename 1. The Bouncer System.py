# 1. The Bouncer System

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
