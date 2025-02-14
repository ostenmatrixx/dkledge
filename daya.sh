#!/bin/bash

# Input files
address_file="ad.txt"
private_key_file="pk.txt"

# Output JSON file
output_file="wallets1.json"

# Initialize the JSON array
echo "[" > "$output_file"

# Read both files line by line
paste "$address_file" "$private_key_file" | while IFS=$'\t' read -r address private_key; do
    # Append to JSON array
    echo "    {" >> "$output_file"
    echo "        \"address\": \"$address\"," >> "$output_file"
    echo "        \"privateKey\": \"$private_key\"" >> "$output_file"
    echo "    }," >> "$output_file"
done

# Remove last comma and close the JSON array
sed -i '$ s/,$//' "$output_file"  # Remove last comma
echo "]" >> "$output_file"

echo "JSON file created at $output_file"
