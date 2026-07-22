# 9. The System Log De-Duplicator

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