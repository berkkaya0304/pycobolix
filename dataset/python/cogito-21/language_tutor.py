class LanguageTutor:
    def __init__(self):
        self.student_name = ""
        self.language = 0
        self.level = 0
        self.hours = 0.0
        self.base_hourly = 0.0
        self.level_surcharge = 0.0
        self.final_hourly = 0.0
        self.total_cost = 0.0
        self.discount = 0.0
        self.net_payable = 0.0

    def get_input(self):
        print("--- GLOBAL VOICES TUTORING ---")
        self.student_name = input("Student Name: ")
        
        print("Language (1=Spanish $30/hr, 2=French $35/hr, ")
        print("          3=Mandarin $45/hr): ")
        self.language = int(input())
        
        print("Level (1=Beginner, 2=Advanced +$10/hr): ")
        self.level = int(input())
        
        print("Hours per week requested: ")
        self.hours = float(input())

    def calculate_costs(self):
        language_rates = {1: 30.00, 2: 35.00, 3: 45.00}
        self.base_hourly = language_rates.get(self.language, 30.00)
        
        self.level_surcharge = 10.00 if self.level == 2 else 0.0
        self.final_hourly = self.base_hourly + self.level_surcharge
        self.total_cost = self.hours * self.final_hourly
        
        if self.hours >= 5.0:
            self.discount = self.total_cost * 0.10
        
        self.net_payable = self.total_cost - self.discount

    def display_invoice(self):
        print("\n" + "=" * 40)
        print("          TUTORING INVOICE              ")
        print("=" * 40)
        print(f"Student: {self.student_name}")
        print(f"Hours:   {self.hours} / week")
        print("-" * 40)
        print(f"Hourly Rate Applied: ${self.final_hourly:.2f}")
        print(f"Gross Weekly Cost:   ${self.total_cost:.2f}")
        
        if self.discount > 0:
            print(f"Volume Discount:    -${self.discount:.2f}")
        
        print("-" * 40)
        print(f"NET WEEKLY PAYABLE:  ${self.net_payable:.2f}")
        print("=" * 40)

def main():
    tutor = LanguageTutor()
    tutor.get_input()
    tutor.calculate_costs()
    tutor.display_invoice()

if __name__ == "__main__":
    main()
