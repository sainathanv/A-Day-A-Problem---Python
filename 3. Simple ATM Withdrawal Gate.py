'''
Day 3: The ATM Withdrawal Gate

Scenario: You are building the core backend checking system for a bank’s automated teller machine. The system must process a one-time withdrawal request against strict boundary parameters.
Rules:

    Initialize the account parameters with an account_balance of 500 and a daily_limit of 200.

    Take a single user input for the requested withdraw_amount.

    Evaluate the amount across a single conditional chain:

        Check for an overdraft violation: If the request is greater than the available balance, deny the transaction with "Insufficient Balance!"

        Check for a regulatory limit violation: If the request is greater than the daily processing allowance, deny the transaction with "Exceeds daily limit!"

        Safe Execution: If it passes both gates, deduct the funds, update the balance state, and print the remaining amount.

    Implement input type exception handling to guard against invalid non-numeric data entries.
'''

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
