def main():
    print("--- E-LEARNING REGISTRATION ---")
    student_name = input("Student Name: ").strip()
    course_code = input("Course (P=Python, C=COBOL, J=Java): ").strip().upper()
    wants_cert = input("Add Verified Certificate ($50)? (Y/N): ").strip().upper()
    wants_tutor = input("Add 1-on-1 Tutoring ($150)? (Y/N): ").strip().upper()
    is_alumni = input("Are you a returning alumni (10% off)? (Y/N): ").strip().upper()

    base_fee, course_name = process_registration(course_code)
    cert_fee = 50.00 if wants_cert == 'Y' else 0.00
    tutor_fee = 150.00 if wants_tutor == 'Y' else 0.00
    discount_amt = base_fee * 0.10 if is_alumni == 'Y' else 0.00
    final_due = base_fee + cert_fee + tutor_fee - discount_amt

    print_invoice(student_name, course_name, base_fee, cert_fee, tutor_fee, discount_amt, final_due)

def process_registration(course_code):
    course_mapping = {
        'P': (200.00, "Python Masterclass"),
        'C': (500.00, "Legacy Sys COBOL"),
        'J': (300.00, "Java Fundamentals")
    }
    return course_mapping.get(course_code, (200.00, "Default Course"))

def print_invoice(student_name, course_name, base_fee, cert_fee, tutor_fee, discount_amt, final_due):
    print("\n======================================")
    print("      COURSE ENROLLMENT RECEIPT       ")
    print("======================================")
    print(f"Student: {student_name}")
    print(f"Course:  {course_name}")
    print("--------------------------------------")
    print(f"Tuition Fee:      ${base_fee:,.2f}")

    if cert_fee > 0:
        print(f"Certificate Fee:  ${cert_fee:,.2f}")

    if tutor_fee > 0:
        print(f"Tutoring Add-on:  ${tutor_fee:,.2f}")

    if discount_amt > 0:
        print(f"Alumni Discount: -${discount_amt:,.2f}")

    print("--------------------------------------")
    print(f"TOTAL ENROLLMENT: ${final_due:,.2f}")
    print("======================================")

if __name__ == "__main__":
    main()
