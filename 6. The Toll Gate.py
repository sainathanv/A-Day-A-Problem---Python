'''Day 6: The Smart Toll Gate

Scenario: You are architecting the integration software engine for an automated highway toll booth processing a queue of vehicle type indexes while managing transactional state data safely.
Rules:

    Map vehicle metadata across parallel indexed data collections: vehicle_type = ["Motorcycle", "Car", "Truck"] and toll_rates = [5, 10, 20].

    Accept an incoming processing queue list containing numeric indexes representing incoming vehicles (e.g., [1, 0, 4, 2, 1]).

    Implement clean functional encapsulation: initialize and maintain a local processing balance variable purely inside the function scope, avoiding any structural reliance on the global scope.

    Iterate through the queue using an inner safety net block:

        Catch index lookup errors cleanly to display an invalid vehicle warning and continue processing the rest of the queue automatically.

        Sound an inspection alarm and execute an immediate structural loop break the exact moment a "Truck" (index 2) is identified.

        Accumulate appropriate financial rates and print individual receipts for safe vehicles.

    Hand the final calculated balance back to the outside driver code using a proper output return statement.
    '''

vehicle_type = ["Motorcycle", "Car", "Truck"]
toll_rates = [5, 10, 20]

def toll_gate_scanner(vehicle_queue):
    booth_balance = 0
    for vehicle_index in vehicle_queue:
        try:
            name = vehicle_type[vehicle_index]
            rate = toll_rates[vehicle_index]
            if name == "Truck":
                print("Truck detected. Locking booth for inspection.")
                break
            booth_balance = booth_balance + rate
            print(f"Processed {name}. Collected ${rate}.")
        except IndexError:
            print("Error: Unrecognized vehicle type index. Skipping Vehicle.")
            continue

    return print("Total booth amount collected = ", booth_balance)


test_queue = [1,0,4,4,1,2]
toll_gate_scanner(test_queue)