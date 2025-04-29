# VLSM Subnet Designer

This is a professional-grade CLI tool for designing IPv4 subnets using **Variable Length Subnet Masking (VLSM)**.  
It allows you to start from any custom IP block (e.g., `10.0.0.0/8`, `192.168.1.0/24`)  
and allocate subnets based on varying host requirements — largest first.

---

## 🚀 Features

- Start from **any valid IPv4 CIDR block** (e.g., `172.16.0.0/16`)
- Input **custom subnet host requirements**
- **Top-down VLSM allocation** (subnets automatically sorted from largest to smallest)
- Displays:
  - Network ID (CIDR)
  - Subnet Mask (dotted decimal)
  - Usable Host Range (first to last usable IP)
  - Number of Usable Hosts
- **Saves results** to a `.csv` file
- **(OPTIONAL) User chooses** filename and save location
- Displays filepath to the output CSV
- 100% based on Python's standard libraries (`ipaddress`, `csv`, `os`)

---

## 📦 Requirements

- Python 3.6 or higher
- No external dependencies

---

## 🧪 Example Usage

```bash
$ python main.py

Welcome to the VLSM Subnet Designer!

Enter your starting network (e.g., 10.0.0.0/8): 10.0.0.0/8
Enter the number of SUBNETS you need: 3
Enter the number of HOSTS for each subnet separated by commas: 400, 10, 4

Enter a name for the output CSV file (without .csv). Leave blank for default 'subnets_output': vlsm_design_apr28
Enter a directory path to save the file. Leave blank for current directory: ./outputs

Calculating...

✅ Subnet design complete.
📄 CSV file saved at: /home/user/projects/subnetdesigner/outputs/vlsm_design_apr28.csv
```


## 👨‍💻 Author
Built by LyricalEcho
