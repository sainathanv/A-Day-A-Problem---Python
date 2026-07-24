#10. Server Configuration Vault

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