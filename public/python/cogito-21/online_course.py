class OnlineCourse:
    def __init__(self):
        self.student_name = ""
        self.course_code = ""
        self.course_name = ""
        self.wants_cert = False
        self.wants_tutor = False
        self.is_alumni = False
        self.base_fee = 0.0
        self.cert_fee = 0.0
        self.tutor_fee = 0.0
        self.discount_amt = 0.0
        self.final_due = 0.0

    def get_input(self):
        print("--- E-LEARNING REGISTRATION ---")
        self.student_name = input("Student Name: ")
        
        while True:
            self.course_code = input("Course (P=Python, C=COBOL, J=Java): ").upper()
            if self.course_code in ['P', 'C', 'J']:
                break
            print("Invalid course code. Please enter P, C, or J.")
        
        self.wants_cert = input("Add Verified Certificate ($50)? (Y/N): ").upper() == 'Y'
        self.wants_tutor = input("Add 1-on-1 Tutoring ($150)? (Y/N): ").upper() == 'Y'
        self.is_alumni = input("Are you a returning alumni (10% off)? (Y/N): ").upper() == 'Y'

    def process_registration(self):
        course_map = {
            'P': ("Python Masterclass", 200.00),
            'C': ("Legacy Sys COBOL", 500.00),
            'J': ("Java Fundamentals", 300.00)
        }
        
        self.course_name, self.base_fee = course_map.get(self.course_code, ("Default Course", 200.00))
        
        if self.wants_cert:
            self.cert_fee = 50.00
            
        if self.wants_tutor:
            self.tutor_fee = 150.00
            
        if self.is_alumni:
            self.discount_amt = self.base_fee * 0.10
            
        self.final_due = self.base_fee + self.cert_fee + self.tutor_fee - self.discount_amt

    def print_invoice(self):
        def format_currency(amount):
            return f"${amount:,.2f}"
        
        print("\n======================================")
        print("      COURSE ENROLLMENT RECEIPT       ")
        print("======================================")
        print(f"Student: {self.student_name}")
        print(f"Course:  {self.course_name}")
        print("--------------------------------------")
        print(f"Tuition Fee:      {format_currency(self.base_fee)}")
        
        if self.cert_fee > 0:
            print(f"Certificate Fee:  {format_currency(self.cert_fee)}")
            
        if self.tutor_fee > 0:
            print(f"Tutoring Add-on:  {format_currency(self.tutor_fee)}")
            
        if self.discount_amt > 0:
            print(f"Alumni Discount: -{format_currency(self.discount_amt)}")
            
        print("--------------------------------------")
        print(f"TOTAL ENROLLMENT: {format_currency(self.final_due)}")
        print("======================================")

def main():
    course = OnlineCourse()
    course.get_input()
    course.process_registration()
    course.print_invoice()

if __name__ == "__main__":
    main()
