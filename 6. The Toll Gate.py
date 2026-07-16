# 6. The smart toll gate

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