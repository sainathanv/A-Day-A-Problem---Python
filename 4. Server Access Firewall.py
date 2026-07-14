# 4. Server Access Firewall

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
