# 8. The VIP Guest Registry Lookup
'''Day 8: The VIP Guest Registry Lookup

Scenario: You are creating a security check-in console for a high-profile corporate event using a key-value dictionary to perform instant status lookups.
Rules:

    Store the setup data in a dictionary:
    guest_registry = {"Alice": "VIP", "Bob": "General Admission", "Charlie": "Staff", "Diana": "VIP"}

    Prompt the user to input a guest name to look up.

    Defensive Lookup: Check if the entered name exists as a key inside guest_registry before attempting to access its value to prevent a KeyError crash.

    Success Path: If found, retrieve the value and print: "Access Granted! Welcome [Guest Name], Tier: [Access Tier Value]."

    Failure Path: If not found, handle it safely and print: "Access Denied: [Name] is not registered on the guest list."
'''

guest_registry = {
    "Alice": "VIP",
    "Bob": "General Admission",
    "Charlie": "Staff",
    "Diana": "VIP"
}

def check_in_guest(registry):
    search_name = input("Enter guest name to check in: ")
    
    if search_name in registry:
        access_tier = registry[search_name]
        print(f"🎟️ Access Granted! Welcome {search_name}, Tier: {access_tier}.")
    else:
        print(f"❌ Access Denied: {search_name} is not registered on the guest list.")

check_in_guest(guest_registry)