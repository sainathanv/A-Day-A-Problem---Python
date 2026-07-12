def smart_savings(target_goal):
    current_savings = 0  # Keep local state inside the function
    
    while current_savings < target_goal:
        try:
            user_deposit = int(input("Enter your deposit amount: $"))
            if user_deposit < 0:
                print("Invalid Input. Please enter a positive amount.")
                continue # Skips the rest of the loop and start the next iteration
            
            current_savings += user_deposit
            
            remaining = target_goal - current_savings
            if remaining < 0:
                remaining = 0
                
            print(f"Current Savings: ${current_savings} | Remaining to goal: ${remaining}\n")
            
        except ValueError:
            print("Error: Please enter a valid whole number for the deposit.\n")
            
    print("Congratulations! You've achieved your financial goal!")


try:
    target = int(input("Enter your target savings goal: $"))
    if target <= 0:
        print("Goal must be greater than 0.")
    else:
        smart_savings(target)
except ValueError:
    print("Error: Please enter a valid number for your target goal.")
