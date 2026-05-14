class PharmacyRX:
    def __init__(self):
        self.patient_name = ""
        self.insurance_provider = 'N'
        self.med_type = 1
        self.refill_months = 1
        self.base_price = 0.0
        self.copay_amt = 0.0
        self.total_charge = 0.0

    def get_input(self):
        print("--- CORNERSTONE PHARMACY RX ---")
        self.patient_name = input("Patient Name: ")
        print("Type of Medication: ")
        print("1=Generic ($25), 2=Brand ($150), 3=Specialty ($800)")
        self.med_type = int(input())
        insurance_input = input("Does patient have insurance? (Y/N): ").upper()
        self.insurance_provider = insurance_input == 'Y'
        self.refill_months = int(input("Number of months supply (1-12): "))

    def calculate_rx(self):
        if self.med_type == 1:
            self.base_price = 25.00
        elif self.med_type == 2:
            self.base_price = 150.00
        elif self.med_type == 3:
            self.base_price = 800.00
        else:
            self.base_price = 25.00

        self.total_charge = self.base_price * self.refill_months

        if self.insurance_provider:
            if self.med_type == 1:
                self.copay_amt = 10.00 * self.refill_months
            elif self.med_type == 2:
                self.copay_amt = 40.00 * self.refill_months
            elif self.med_type == 3:
                self.copay_amt = 100.00 * self.refill_months

            if self.copay_amt > self.total_charge:
                self.copay_amt = self.total_charge

            self.total_charge = self.copay_amt

    def print_label(self):
        print("\n=======================================")
        print("         PRESCRIPTION LABEL            ")
        print("=======================================")
        print(f"Patient: {self.patient_name}")
        print(f"Supply:  {self.refill_months} Month(s)")
        print("---------------------------------------")
        
        retail_value = self.base_price * self.refill_months
        print(f"Retail Value:         ${retail_value:,.2f}")
        
        insurance_status = "YES" if self.insurance_provider else "NO"
        print(f"Insurance Applied:    {insurance_status}")
        print("---------------------------------------")
        print(f"PATIENT RESPONSIBILITY: ${self.total_charge:,.2f}")
        print("=======================================")

    def run(self):
        self.get_input()
        self.calculate_rx()
        self.print_label()

if __name__ == "__main__":
    rx = PharmacyRX()
    rx.run()
