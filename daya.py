# Input files
address_file = "ad.txt"
private_key_file = "pk.txt"

# Output JSON file
output_file = "wallets1.json"

# Initialize the JSON array
wallets = []

# Read both files line by line
with open(address_file, 'r') as af, open(private_key_file, 'r') as pkf:
    for address, private_key in zip(af, pkf):
        # Strip any trailing newline characters
        address = address.strip()
        private_key = private_key.strip()
        
        # Append to the JSON array
        wallets.append({
            "address": address,
            "privateKey": private_key
        })

# Write to JSON file
import json
with open(output_file, 'w') as of:
    json.dump(wallets, of, indent=4)

print(f"JSON file created at {output_file}")
