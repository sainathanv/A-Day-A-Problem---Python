#10. Server Configuration Vault
'''
Day 10: The Immutable Server Configuration Vault

Scenario: You are designing a startup configuration loader for a cloud server that relies on fixed system settings. To prevent accidental modifications during runtime, these settings are stored in an immutable tuple.
Rules:
    Store setup data in a tuple:
    server_config = ("Production_Server_01", 8080, "PRODUCTION", True)
    Write a function load_server_config(config_tuple) that extracts the values (Server Name, Port, Environment, SSL Status) and prints a startup banner.
    The Immunity Trap Test: Inside a try-except TypeError block, simulate an accidental attempt to alter a value in the tuple (e.g., config_tuple[1] = 9090).
    Catch the TypeError gracefully and print a security alert: "SECURITY ALERT: Configuration is locked and immutable. Tampering blocked!"
'''

server_config = ("Production_Server_01", 8080, "PRODUCTION", True)

def load_server_config(config_tuple):
    server_name, port, environment, ssl_active = config_tuple

    print("SERVER CONFIGURATION VAULT")
    print(f"Server Name    : {server_name}")
    print(f"Running Port   : {port}")
    print(f"Environment    : {environment}")

    if ssl_active:
        print("SSL Encryption : Enabled")
    else:
        print("SSL Encryption : Disabled")

    print("\nTesting Vault Immunity")

    try:
        config_tuple[1] = 9090
    except TypeError:
        print(
            "SECURITY ALERT: Configuration is locked and immutable. Tampering blocked!"
        )


load_server_config(server_config)