# 5. The Dangerous Baggage Scanner
'''Day 5: The Dangerous Baggage Scanner

Scenario: You are writing the iteration flow control software for an airport baggage scanning conveyor belt processing a traveler's luggage list item-by-item.
Rules:

    Process a sequential fixed data collection representing a piece of luggage: luggage_items = ["Clothes", "Laptop", "Liquid", "Shoes", "Weapon", "Books"]

    Loop through the list sequentially from start to finish.

    The Prohibited Item Gate: If the scanner encounters "Liquid", print a warning message, skip processing any remaining logic for this specific item, and immediately jump to scanning the next item on the belt without stopping the conveyor.

    The Critical Threat Gate: If the scanner encounters "Weapon", print an emergency security breach alarm and terminate the loop completely right then and there, leaving any remaining items unscanned.
'''

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
