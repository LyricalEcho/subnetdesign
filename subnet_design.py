import ipaddress
import csv
import os

def parse_host_requirements(hosts_input: str, expected_count: int):
    hosts_list = [int(h.strip()) for h in hosts_input.split(",")]
    if len(hosts_list) != expected_count:
        raise ValueError("Number of hosts provided does not match the number of subnets requested.")
    return sorted(hosts_list, reverse=True)

def find_subnet_for_hosts(hosts_needed):
    bits = 0
    while (2 ** bits - 2) < hosts_needed:
        bits += 1
    subnet_prefix = 32 - bits
    return subnet_prefix

def dotted_decimal_mask(prefix_length):
    return str(ipaddress.IPv4Network(f"0.0.0.0/{prefix_length}").netmask)

def allocate_subnets(starting_network_str, hosts_list):
    starting_network = ipaddress.ip_network(starting_network_str, strict=False)
    current_ip = starting_network.network_address
    allocations = []

    for idx, hosts_needed in enumerate(hosts_list, 1):
        subnet_prefix = find_subnet_for_hosts(hosts_needed)
        subnet = ipaddress.ip_network(f"{current_ip}/{subnet_prefix}", strict=False)

        if subnet.network_address < starting_network.network_address or subnet.broadcast_address > starting_network.broadcast_address:
            raise ValueError(f"Not enough address space to allocate subnet {idx} with {hosts_needed} hosts.")

        hosts = list(subnet.hosts())
        if hosts:
            first_usable = hosts[0]
            last_usable = hosts[-1]
        else:
            first_usable = subnet.network_address
            last_usable = subnet.broadcast_address

        allocations.append({
            "Subnet Number": idx,
            "Network ID": str(subnet.network_address),
            "CIDR": f"/{subnet_prefix}",
            "Subnet Mask": dotted_decimal_mask(subnet_prefix),
            "First Usable IP": str(first_usable),
            "Last Usable IP": str(last_usable),
            "Usable Hosts": len(hosts),
        })

        current_ip = subnet.broadcast_address + 1

    return allocations

def save_subnets_to_csv(allocations, filename="subnets_output.csv", directory="."):
    if not filename.endswith(".csv"):
        filename += ".csv"
    full_path = os.path.join(directory, filename)

    with open(full_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Subnet Number", "Network ID", "CIDR", "Subnet Mask", "First Usable IP", "Last Usable IP", "Usable Hosts"])
        writer.writeheader()
        for allocation in allocations:
            writer.writerow(allocation)
    
    return full_path  # Return the full file path for confirmation
