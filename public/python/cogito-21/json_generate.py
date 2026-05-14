import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Record:
    name: str
    value: str
    blank: str
    enabled: bool

def main():
    # Create record with initial values
    record = Record(
        name="Test Name",
        value="Test Value",
        blank="",
        enabled=True
    )
    
    # Convert record to dictionary for JSON serialization
    record_dict = {
        "name": record.name,
        "value": record.value,
        "blank": record.blank,
        "enabled": record.enabled
    }
    
    try:
        # Generate JSON
        json_output = json.dumps(record_dict, indent=2)
        char_count = len(json_output)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON: {e}")
        return
    
    # Display results
    print(f"Generated JSON for record: {record}")
    print("----------------------------")
    print(json_output)
    print("----------------------------")
    print(f"JSON output character count: {char_count}")
    print("Done.")

if __name__ == "__main__":
    main()
