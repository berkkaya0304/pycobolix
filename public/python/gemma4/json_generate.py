import json

def main():
    # Initialize record data
    # COBOL pic x(10) is simulated by strings. 
    # The 'ws-record-blank' is present in the COBOL structure but not assigned.
    record = {
        "name": "Test Name",
        "value": "Test Value",
        "blank": "",
        "enabled": True
    }

    try:
        # The COBOL 'json generate' maps specific fields to JSON keys
        # We create a dictionary containing only the mapped fields
        output_data = {
            "name": record["name"],
            "value": record["value"],
            "enabled": record["enabled"]
        }
        
        # Generate JSON string
        json_output = json.dumps(output_data)
        char_count = len(json_output)
        
        print("JSON document successfully generated.")
        
        # Display the raw record state (simulating the display of the group level)
        # COBOL displays the fixed-length record; Python displays the dict/values
        record_display = f"{record['name']:<10}{record['value']:<10}{record['blank']:<10}{str(record['enabled']).lower():<5}"
        
        print(f"Generated JSON for record: {record_display}")
        print("----------------------------")
        print(json_output)
        print("----------------------------")
        print(f"JSON output character count: {char_count}")
        print("Done.")

    except Exception as e:
        print(f"Error generating JSON error {e}")

if __name__ == "__main__":
    main()
