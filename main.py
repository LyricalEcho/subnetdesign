from subnet_design import (
    parse_host_requirements,
    allocate_subnets,
    save_subnets_to_csv
)
import os
import datetime

def log_error(error_message: str):
    """Logs error messages with timestamps into log_errors.txt"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_errors.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {error_message}\n")

def main():
    print("Welcome to the VLSM Subnet Designer!\n")

    try:
        starting_network = input("Enter your starting network (e.g., 10.0.0.0/8): ").strip()
        num_subnets = int(input("Enter the number of SUBNETS you need: ").strip())
        hosts_input = input("Enter the number of HOSTS for each subnet separated by commas: ").strip()

        hosts_list = parse_host_requirements(hosts_input, num_subnets)

        print("\nCalculating...\n")
        allocations = allocate_subnets(starting_network, hosts_list)

        filename_input = input("\nEnter a name for the output CSV file (without .csv). Leave blank for default 'subnets_output': ").strip()
        directory_input = input("Enter a directory path to save the file. Leave blank for current directory: ").strip()

        filename = filename_input if filename_input else "subnets_output"
        directory = directory_input if directory_input else "."

        csv_path = save_subnets_to_csv(allocations, filename, directory)

        print(f"\n✅ Subnet design complete.")
        print(f"📄 CSV file saved at: {os.path.abspath(csv_path)}\n")

    except Exception as e:
        user_friendly_error = f"🚨 Error: {e}"
        print(f"\n{user_friendly_error}\n")
        log_error(str(e))

if __name__ == "__main__":
    main()
