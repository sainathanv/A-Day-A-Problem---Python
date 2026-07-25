# 9. The System Log De-Duplicator
'''
Day 9: The System Log De-Duplicator

Scenario: You are building an automated log-cleaning pipeline for a network monitoring tool that receives raw IP addresses and purges repeated entries.
Rules:
    Process a raw log list containing duplicates:
    raw_logs = ["192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.5", "10.0.0.1", "192.168.1.1"]
    Measure the initial total log count using len().
    Convert the list into a set to automatically strip out all duplicate IP addresses.
    Measure the size of the unique set and calculate the total number of purged duplicates (Original Count−Unique Count).
    Display a final report showing total raw logs, total unique IPs, number of duplicates purged, and iterate through the set to print each unique IP address.'''

raw_logs = [
    "192.168.1.1",
    "10.0.0.1",
    "192.168.1.1",
    "172.16.0.5",
    "10.0.0.1",
    "192.168.1.1"
]

def clean_system_logs(log_list):
    total_raw_count = len(log_list)
    unique_ips = set(log_list)
    unique_count = len(unique_ips)
    duplicates_removed = total_raw_count - unique_count
    print(f"Total raw logs processed: {total_raw_count}")
    print(f"Unique IPs identified: {unique_count}")
    print(f"Duplicate entries purged: {duplicates_removed}")
    print("\nUnique IPs List:")
    
    for ip in unique_ips:
        print(f"{ip}")

clean_system_logs(raw_logs)