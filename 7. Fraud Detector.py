# 7. The Fraud Detector
'''
Day 7: The Batch Credit Card Fraud Detector
Scenario: You are writing the fraud detection script for a payment processing gateway. The gateway receives a batch of transaction amounts processed by a single account in a single minute and must audit them.
Rules:
    Process a list of transactions: transactions = [45, 80, 999, 120, 5000, 25]
    Maintain a boolean flag fraud_detected initialized to False and a fraud_counter tracker.
    Critical Threshold: If any transaction is greater than $1,000, print a critical alert, set fraud_detected = True, increment the counter, and immediately break the loop.
    Warning Threshold: If a transaction is between $500 and $1,000 (inclusive), print a warning alert, set fraud_detected = True, increment the counter, and continue scanning.
    Safe Path: For transactions under $500, print a clear message.

    Final Evaluation: After the loop, check the flag/counter. If fraud was detected, print "BATCH AUDIT FAILED: Account locked pending review." Otherwise, print "BATCH AUDIT SUCCESSFUL: All transactions cleared."
'''

def detect_fraud(amounts):
    fraud_detected = False
    fraud_counter = 0
    for transaction in amounts:
        fraud_detected = False
        transaction_amount = transaction
        if transaction_amount > 1000:
            print(f"Critical Alert: Single transaction exceeds limit: ${transaction_amount}")
            fraud_detected = True
            fraud_counter +=1
            break
        elif transaction_amount > 500 and transaction_amount <= 1000:
            print(f"Warning: High value transaction observed: ${transaction_amount}.")
            fraud_detected = True
            fraud_counter +=1
            continue
        else:
            print(f"Transaction: ${transaction_amount} checked... clear.")

    if fraud_counter !=0:
        print("BATCH AUDIT FAILED: Account locked pending review.")
    else:
        print ("BATCH AUDIT SUCCESSFUL: All transactions cleared.")




transaction_amounts = [45, 80, 999, 120, 5000, 25]
detect_fraud(transaction_amounts)