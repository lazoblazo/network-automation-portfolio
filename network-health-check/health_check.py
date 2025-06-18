import yaml
import subprocess
from netmiko import ConnectHandler
from datetime import datetime

# Nacitaj zariadenia zo suboru
with open("devices.yaml") as f:
    devices = yaml.safe_load(f)

print("=== Network Health Check Report ===\n")
for device in devices:
    hostname = device.get("hostname")
    ip = device.get("ip")

    print(f"[{hostname}] Pinging {ip}...", end=" ")

    # Ping test
    response = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if "TTL=" not in response.stdout:
        print("❌ Ping failed")
        continue

    print("✅ Ping OK")

    try:
        conn = ConnectHandler(**device)
        version = conn.send_command("show version", use_textfsm=True)
        uptime = version[0]["uptime"] if version and isinstance(version, list) else "N/A"
        os_version = version[0]["version"] if version and isinstance(version, list) else "N/A"

        print(f"    OS Version: {os_version}")
        print(f"    Uptime: {uptime}")

        conn.disconnect()
    except Exception as e:
        print(f"    ⚠️ SSH error: {e}")

print(f"\nDone at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
