def compute_tva_pricing():
    net_price = float(input("Enter the net price (before VAT): "))
    vat_rate = float(input("Enter the VAT rate (e.g. 1.2 for 20%): "))

    gross_price = net_price * vat_rate
    print(f"The total price including VAT is: {gross_price:.2f}")

if __name__ == "__main__":
    compute_tva_pricing()
