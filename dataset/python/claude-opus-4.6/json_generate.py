"""
JSON Generate Example
Converted from COBOL (json_generate.cbl) to Python

Demonstrates generating a JSON document from a record structure,
equivalent to COBOL's JSON GENERATE command.
"""
import json


def main():
    ws_record = {
        "name": "Test Name",
        "value": "Test Value",
        "ws_record_blank": "",
        "enabled": True,
    }

    try:
        ws_json_output = json.dumps(ws_record)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON: {e}")
        return

    print(f"Generated JSON for record: {ws_record}")
    print("----------------------------")
    print(ws_json_output)
    print("----------------------------")
    print(f"JSON output character count: {len(ws_json_output)}")
    print("Done.")


if __name__ == "__main__":
    main()
