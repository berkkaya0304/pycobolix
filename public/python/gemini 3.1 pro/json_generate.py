import json

def main():
    ws_record_name = "Test Name"
    ws_record_value = "Test Value"
    ws_record_flag_enabled = True

    record = {
        "name": ws_record_name.strip(),
        "value": ws_record_value.strip(),
        "enabled": "true" if ws_record_flag_enabled else "false"
    }

    try:
        ws_json_output = json.dumps(record)
        ws_json_char_count = len(ws_json_output)
        print("JSON document successfully generated.")
    except Exception as e:
        print(f"Error generating JSON error {e}")
        return

    # In COBOL, record was displayed in raw format:
    print(f"Generated JSON for record: {ws_record_name.ljust(10)}{ws_record_value.ljust(10)}{''.ljust(10)}{'true ' if ws_record_flag_enabled else 'false'}")
    print("----------------------------")
    print(ws_json_output.strip())
    print("----------------------------")
    print(f"JSON output character count: {ws_json_char_count:04d}")
    print("Done.")

if __name__ == "__main__":
    main()
