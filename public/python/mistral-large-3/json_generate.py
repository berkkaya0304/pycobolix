import json

def main():
    record = {
        "name": "Test Name",
        "value": "Test Value",
        "enabled": True
    }

    try:
        json_output = json.dumps(record, indent=2)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON: {e}")
        return

    print("Generated JSON for record:", record)
    print("----------------------------")
    print(json_output)
    print("----------------------------")
    print(f"JSON output character count: {len(json_output)}")
    print("Done.")

if __name__ == "__main__":
    main()
