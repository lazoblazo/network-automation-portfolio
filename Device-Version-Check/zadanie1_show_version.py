from netmiko import ConnectHandler
import yaml

# Načíta IP a prihlasovacie údaje zo súboru devices.yaml
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

for device in devices:
    print(f"Pripájam sa na {device['ip']}...")
    try:
        connection = ConnectHandler(
            device_type=device['device_type'],
            host=device['ip'],
            username=device['username'],
            password=device['password'],
        )
        output = connection.send_command("show version")
        connection.disconnect()

    except Exception as e:
        output = f"Chyba pri pripájaní na {device['ip']}: {e}"

    # Výstup zapíšeme vždy, aj keď ide o chybu
    with open(f"output_{device['ip']}.txt", "w") as file:
        file.write(output)
