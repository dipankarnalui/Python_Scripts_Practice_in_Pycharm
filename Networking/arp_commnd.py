import subprocess

def get_arp_table():
    # Run the arp command and capture the output
    arp_output = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    
    # Check if the command ran successfully
    if arp_output.returncode != 0:
        print(f"Error running arp command: {arp_output.stderr}")
        return

    # Split the output into lines
    arp_lines = arp_output.stdout.splitlines()

    # Parse the arp table and extract useful information
    arp_table = []
    for line in arp_lines:
        # Example parsing of typical arp output line
        # Ensure the line contains enough parts before processing
        parts = line.split()
        if len(parts) >= 4 and 'at' in parts:  # Avoid lines with insufficient parts
            try:
                ip_address = parts[1].strip('()')
                mac_address = parts[3]
                arp_table.append({'IP Address': ip_address, 'MAC Address': mac_address})
            except IndexError:
                print(f"Skipping line due to format: {line}")
                continue

    return arp_table

# Get the arp table and display it
arp_table = get_arp_table()
if arp_table:
    for entry in arp_table:
        print(f"IP Address: {entry['IP Address']}, MAC Address: {entry['MAC Address']}")
