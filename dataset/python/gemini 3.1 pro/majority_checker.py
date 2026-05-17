def main():
    ws_firstname = input("Enter your first name: ")
    try:
        ws_age = int(input("Enter your age: "))
    except ValueError:
        ws_age = 0

    if ws_age >= 18:
        ws_response = f"Hello {ws_firstname}, you are an adult."
    else:
        ws_response = f"Hello {ws_firstname}, you are a minor."

    print(ws_response)

if __name__ == "__main__":
    main()
