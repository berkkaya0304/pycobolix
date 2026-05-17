class VetAppointment:
    def __init__(self):
        self.pet_name = ""
        self.visit_reason = 0
        self.doctor_req = 0
        self.exam_fee = 0.0
        self.dr_surcharge = 0.0
        self.total_estimate = 0.0
        self.reason_txt = ""
        self.dr_txt = ""

    def get_input(self):
        print("--- VET CLINIC SCHEDULING ---")
        self.pet_name = input("Pet Name: ")
        
        print("Reason for Visit: ")
        print("1=Wellness Exam ($50)")
        print("2=Sick Visit ($85)")
        print("3=Emergency ($150)")
        self.visit_reason = int(input("Enter choice (1-3): "))
        
        print("Requested Doctor: ")
        print("1=Dr. Smith (General)")
        print("2=Dr. Jones (Specialist +$40)")
        self.doctor_req = int(input("Enter choice (1-2): "))

    def calculate_estimate(self):
        if self.visit_reason == 1:
            self.exam_fee = 50.00
            self.reason_txt = "Wellness Exam"
        elif self.visit_reason == 2:
            self.exam_fee = 85.00
            self.reason_txt = "Sick Visit"
        elif self.visit_reason == 3:
            self.exam_fee = 150.00
            self.reason_txt = "Emergency"
        else:
            self.exam_fee = 50.00
            self.reason_txt = "Wellness (Default)"

        if self.doctor_req == 1:
            self.dr_surcharge = 0.0
            self.dr_txt = "Dr. Smith"
        elif self.doctor_req == 2:
            self.dr_surcharge = 40.00
            self.dr_txt = "Dr. Jones"
        else:
            self.dr_surcharge = 0.0
            self.dr_txt = "Any Available"

        self.total_estimate = self.exam_fee + self.dr_surcharge

    def print_confirmation(self):
        print("\n" + "="*40)
        print("       APPOINTMENT CONFIRMATION         ")
        print("="*40)
        print(f"Patient: {self.pet_name}")
        print(f"Doctor:  {self.dr_txt}")
        print(f"Visit:   {self.reason_txt}")
        print("-"*40)
        print(f"Base Exam Fee:      ${self.exam_fee:,.2f}")
        if self.dr_surcharge > 0:
            print(f"Specialist Fee:     ${self.dr_surcharge:,.2f}")
        print("-"*40)
        print(f"ESTIMATED TOTAL:    ${self.total_estimate:,.2f}")
        print("="*40)

    def run(self):
        self.get_input()
        self.calculate_estimate()
        self.print_confirmation()

if __name__ == "__main__":
    appointment = VetAppointment()
    appointment.run()
