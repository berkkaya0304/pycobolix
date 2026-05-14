def main():
    try:
        ws_net_price = float(input("Enter the net price (before VAT): "))
        ws_vat_rate = float(input("Enter the VAT rate (e.g. 1.2 for 20%): "))
    except ValueError:
        return

    ws_gross_price = ws_net_price * ws_vat_rate
    print(f"The total price including VAT is: {ws_gross_price:7.2f}")

if __name__ == "__main__":
    main()
