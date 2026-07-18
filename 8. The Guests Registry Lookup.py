# 8. The VIP Guest Registry Lookup

# Step 1: Initialize the structural Key-Value data container
guest_registry = {
    "Alice": "VIP",
    "Bob": "General Admission",
    "Charlie": "Staff",
    "Diana": "VIP"
}

def check_in_guest(registry):
    # Step 2: Capture user input
    search_name = input("Enter guest name to check in: ")
    
    # Step 3: Use the 'in' keyword to safely check if the key exists
    if search_name in registry:
        # If true, extract the specific value mapped to that key using square brackets []
        access_tier = registry[search_name]
        print(f"🎟️ Access Granted! Welcome {search_name}, Tier: {access_tier}.")
    else:
        # If false, handle the missing key safely without crashing
        print(f"❌ Access Denied: {search_name} is not registered on the guest list.")

# Step 4: Run the function engine
check_in_guest(guest_registry)