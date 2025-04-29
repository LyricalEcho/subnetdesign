from subnet_design import (
    parse_host_requirements,
    allocate_subnets,
    save_subnets_to_csv
)
import os

def main():
    print("Welcome to the VLSM Subnet Designer!\n")

    starting_network = input("Enter your starting network (e.g., 10.0.0.0/8): ").strip()

    try:
        num_subnets = int(input("Enter the number of SUBNETS you need: ").strip())
    except ValueError:
        print("Invalid number of subnets. Exiting.")
        return

    hosts_input = input("Enter the number of HOSTS for each subnet separated by commas: ").strip()

    try:
        hosts_list = parse_host_requirements(hosts_input, num_subnets)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return

    print("\nCalculating...\n")

    try:
        allocations = allocate_subnets(starting_network, hosts_list)
    except ValueError as ve:
        print(f"Allocation Error: {ve}")
        return

    # Ask user for filename and directory
    filename_input = input("\nEnter a name for the output CSV file (without .csv). Leave blank for default 'subnets_output': ").strip()
    directory_input = input("Enter a directory path to save the file. Leave blank for current directory: ").strip()

    filename = filename_input if filename_input else "subnets_output"
    directory = directory_input if directory_input else "."

    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist. Exiting.")
        return

    # Save results
    csv_path = save_subnets_to_csv(allocations, filename, directory)

    # Final clean message
    print(f"\n✅ Subnet design complete.")
    print(f"📄 CSV file saved at: {os.path.abspath(csv_path)}\n")

if __name__ == "__main__":
    main()
