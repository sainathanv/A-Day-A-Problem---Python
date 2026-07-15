# 5. The Dangerous Baggage Scanner

luggage_items = ["Clothes", "Laptop", "Liquid", "Shoes", "Weapon", "Books"]

def scan_baggage(luggage_items):
    for item in luggage_items:
        items = item
        if item == "Weapon":
            print("SECURITY BREACH: Weapon detected! Halting conveyor belt immediately!")
            break
        elif item == "Liquid":
            print("Alert: Liquid detected. Must be removed from carry-on.")
            continue
        else:
            print(f"Scanning {items}... Clear.")

scan_baggage(luggage_items)
