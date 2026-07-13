def ATM_withdraw(amount):
    if amount > 0:
        if amount > account_balance:
            print("Insufficient Balance!")
        elif amount > daily_limit:
            print("Exceeds daily limit!")
        else:
            new_balance = account_balance - amount
            print(f"Withdrawal successful.\n Your updated balance is {new_balance}")


account_balance = 500
daily_limit = 200

try:
    withdraw_amount = int(input("How much money would you like to withdraw?\n"))
    ATM_withdraw(withdraw_amount)

except ValueError:
    print("Error! Enter valid number...")
