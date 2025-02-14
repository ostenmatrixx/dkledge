# File paths
input_file = "proxy.txt"
output_file = "proxies_numbered.txt"

try:
    # Read the proxies from the input file
    with open(input_file, "r") as infile:
        proxies = infile.readlines()
    
    # Check if the input file is actually being read
    if not proxies:
        print("No proxies found in proxies.txt.")
    
    # Open the output file in append mode
    with open(output_file, "a") as outfile:
        # Loop through each proxy and add a number
        for i, proxy in enumerate(proxies, start=1):
            proxy = proxy.strip()  # Remove any leading/trailing whitespace
            if proxy:  # Ensure the line isn't empty
                # Format the proxy with the number
                formatted_proxy = f"{proxy}:{i}"
                # Write the formatted proxy to the output file
                outfile.write(formatted_proxy + "\n")
                # Print the formatted proxy to the console
                print(formatted_proxy, flush=True)  # Ensure immediate console output

    print("Proxies have been reformatted and saved to proxies_numbered.txt.")
except FileNotFoundError:
    print(f"Error: {input_file} not found. Make sure the file exists in the same directory.")
except Exception as e:
    print(f"An error occurred: {e}")
