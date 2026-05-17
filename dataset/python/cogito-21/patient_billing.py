class PatientBilling:
    def __init__(self):
        self.patient_id = ""
        self.patient_name = ""
        self.admit_days = 0
        self.room_type = 0
        self.room_charge = 0.0
        self.surgery_charge = 0.0
        self.medication_charge = 0.0
        self.total_charge = 0.0
        self.insurance_cover = 0.0
        self.patient_owes = 0.0

    def input_phase(self):
        print("+++ GENERAL HOSPITAL BILLING +++")
        self.patient_id = input("Patient ID: ")
        self.patient_name = input("Patient Name: ")
        self.admit_days = int(input("Days Admitted: "))
        self.room_type = int(input("Room Type (1=Ward, 2=Semi, 3=Private): "))
        self.surgery_charge = float(input("Surgery Charges ($): "))
        self.medication_charge = float(input("Medication Charges ($): "))

    def process_phase(self):
        room_rates = {1: 150.00, 2: 250.00, 3: 400.00}
        rate = room_rates.get(self.room_type, 150.00)
        if self.room_type not in room_rates:
            print("(Defaulted room to Ward)")
        self.room_charge = self.admit_days * rate
        
        self.total_charge = self.room_charge + self.surgery_charge + self.medication_charge
        self.insurance_cover = self.total_charge * 0.80
        self.patient_owes = self.total_charge - self.insurance_cover

    def output_phase(self):
        def format_currency(amount):
            return f"${amount:,.2f}"

        print("\n-----------------------------------------")
        print(" HOSPITAL DISCHARGE BILL")
        print("-----------------------------------------")
        print(f"Patient: {self.patient_name}  [ID: {self.patient_id}]")
        print(f"Days in Hospital: {self.admit_days}")
        print(f"Room Charges:    {format_currency(self.room_charge)}")
        print(f"Surgery:         {format_currency(self.surgery_charge)}")
        print(f"Medication:      {format_currency(self.medication_charge)}")
        print("-----------------------------------------")
        print(f"GROSS TOTAL:     {format_currency(self.total_charge)}")
        print(f"Insurance Pays: -{format_currency(self.insurance_cover)}")
        print("=========================================")
        print(f"PATIENT TO PAY:  {format_currency(self.patient_owes)}")
        print("=========================================")

    def run(self):
        self.input_phase()
        self.process_phase()
        self.output_phase()
        print("Billing cycle complete.")

if __name__ == "__main__":
    billing = PatientBilling()
    billing.run()
