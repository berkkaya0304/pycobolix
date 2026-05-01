def main():
    print("--- E-LEARNING REGISTRATION ---")
    stud_name = input("Student Name: ")
    course_cde = input("Course (P=Python, C=COBOL, J=Java): ").strip().upper()
    wants_cert = input("Add Verified Certificate ($50)? (Y/N): ").strip().upper() == 'Y'
    wants_tutor = input("Add 1-on-1 Tutoring ($150)? (Y/N): ").strip().upper() == 'Y'
    is_alumni = input("Are you a returning alumni (10% off)? (Y/N): ").strip().upper() == 'Y'

    if course_cde == 'P':
        base_fee = 200.00
        course_name = "Python Masterclass"
    elif course_cde == 'C':
        base_fee = 500.00
        course_name = "Legacy Sys COBOL"
    elif course_cde == 'J':
        base_fee = 300.00
        course_name = "Java Fundamentals"
    else:
        base_fee = 200.00
        course_name = "Default Course"

    cert_fee = 50.00 if wants_cert else 0.0
    tutor_fee = 150.00 if wants_tutor else 0.0

    discount_amt = 0.0
    if is_alumni:
        discount_amt = base_fee * 0.10

    final_due = base_fee + cert_fee + tutor_fee - discount_amt

    print("\n======================================")
    print("      COURSE ENROLLMENT RECEIPT       ")
    print("======================================")
    print(f"Student: {stud_name}")
    print(f"Course:  {course_name}")
    print("--------------------------------------")
    print(f"Tuition Fee:      ${base_fee:10.2f}")
    
    if cert_fee > 0:
        print(f"Certificate Fee:  ${cert_fee:10.2f}")
        
    if tutor_fee > 0:
        print(f"Tutoring Add-on:  ${tutor_fee:10.2f}")

    if discount_amt > 0:
        print(f"Alumni Discount: -${discount_amt:10.2f}")
        
    print("--------------------------------------")
    print(f"TOTAL ENROLLMENT: ${final_due:10.2f}")
    print("======================================")

if __name__ == "__main__":
    main()
