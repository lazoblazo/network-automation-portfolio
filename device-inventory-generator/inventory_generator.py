import yaml
from datetime import datetime

# Načítanie zariadení zo súboru devices.yaml
with open("devices.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

devices = data["devices"]

# Vytvorenie Markdown tabuľky
output = "# 📋 Device Inventory\n\n"
output += "| Name | IP Address | Model | Location |\n"
output += "|------|-------------|---------------------|-----------|\n"

for device in devices:
    output += f"| {device['name']} | {device['ip']} | {device['model']} | {device['location']} |\n"

output += f"\n\n*Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"

# Uloženie výsledku do Markdown súboru
with open("inventory.md", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Inventory report bol úspešne vygenerovaný ako 'inventory.md'")
