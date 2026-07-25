# 4. Server Access Firewall
'''
Day 4: The Server Access Firewall

Scenario: You are developing a low-level security module for a corporate network server that evaluates database access permissions based on an index list position.
Rules:

    Maintain a fixed structural list mapping clearance tiers: clearance_levels = ["Guest", "Developer", "DevOps", "Manager", "Root_Admin"]

    The restricted database requires a minimum index position tier of 2 (DevOps) to allow entry.

    Ask the user to input their numeric clearance index position.

    Safely look up the corresponding text string name from the data structure inside a protected error-trapping block to catch out-of-bounds inputs (e.g., index 5 or higher) before they trigger a system crash.

    Grant entry if the index is valid and greater than or equal to 2, or deny entry showing the explicit tier name if it falls below the minimum requirement.
'''

def server_access_firewall(levels):
    clearance_levels = ["Guest", "Developer", "DevOps", "Manager", "Root_Admin"]
    try:
        tier_level = clearance_levels[levels]
        if levels >=2:
            print(f"Access Granted! Welcome {tier_level}.")
        else:
            print(f"Access denied! Tier: {tier_level} has insufficient permission")
    except IndexError:
        print("Error! Enter valid tier level (0-4)")

try:
    level_input = int(input("Enter your Tier Level: "))
    server_access_firewall (level_input)

except ValueError:
        print("Error! Enter valid input.")