def main():
    print("--- E-LEARNING REGISTRATION ---")
    stud_name = input("Student Name: ")
    course_cde = input("Course (P=Python, C=COBOL, J=Java): ").upper()
    wants_cert = input("Add Verified Certificate ($50)? (Y/N): ").upper()
    wants_tutor = input("Add 1-on-1 Tutoring ($150)? (Y/N): ").upper()
    is_alumni = input("Are you a returning alumni (10% off)? (Y/N): ").upper()

    # Process Registration
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

    cert_fee = 50.00 if wants_cert == 'Y' else 0.00
    tutor_fee = 150.00 if wants_tutor == 'Y' else 0.00
    discount_amt = base_fee * 0.10 if is_alumni == 'Y' else 0.00

    final_due = base_fee + cert_fee + tutor_fee - discount_amt

    # Print Invoice
    print("\n======================================")
    print("      COURSE ENROLLMENT RECEIPT       ")
    print("======================================")
    print(f"Student: {stud_name}")
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
