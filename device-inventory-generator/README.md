# 📋 Device Inventory Generator

This is a simple Python script that generates a device inventory report based on a YAML configuration file.  
The output is a Markdown table that can be used for documentation or as a lightweight CMDB.

---

## 💡 What it does

- Loads device data from a YAML file (`devices.yaml`)
- Generates a formatted `inventory.md` report
- Includes device name, IP address, model, and location
- Adds a timestamp of generation

---

## 🧪 Example output

| Name     | IP Address   | Model               | Location   |
|----------|--------------|---------------------|------------|
| Router_1 | 192.168.1.1  | Cisco ISR 4331      | Bratislava |
| Switch_1 | 192.168.1.2  | Cisco Catalyst 9200 | Kosice     |

---

## ⚙️ How to run

1. Make sure you have Python and `PyYAML` installed:
