# 7. The Fraud Detector

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