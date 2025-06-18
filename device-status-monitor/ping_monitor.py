import yaml
import subprocess
from datetime import datetime

# Načíta zoznam zariadení z devices.yaml
try:
    with open("devices.yaml", "r", encoding="utf-8") as f:
        devices = yaml.safe_load(f)["devices"]
except Exception as e:
    print(f"❌ Chyba pri načítaní devices.yaml: {e}")
    exit()

# Priprav Markdown výstup
output = "# 🖥️ Device Status Report\n\n"
output += "| Name | IP Address | Status |\n"
output += "|------|-------------|--------|\n"

print("🔍 Spúšťam pingovanie zariadení...\n")

# Pre každé zariadenie spustí ping
for device in devices:
    name = device["name"]
    ip = device["ip"]
    print(f"Pinging {name} ({ip})...")

    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "1000", ip],
            stdout=subprocess.DEVNULL
        )
        status = "🟢 Online" if result.returncode == 0 else "🔴 Offline"
    except Exception:
        status = f"⚠️ Error"

    print(f"  → {status}")
    output += f"| {name} | {ip} | {status} |\n"

# Pridá čas generovania
output += f"\n\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

# Uloží výsledok
try:
    with open("status_report.md", "w", encoding="utf-8") as f:
        f.write(output)
    print("\n✅ Status report bol úspešne uložený do 'status_report.md'")
except Exception as e:
    print(f"❌ Chyba pri ukladaní výstupu: {e}")
