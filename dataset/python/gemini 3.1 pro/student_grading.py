def main():
    want_to_exit = 'N'

    print("*** STUDENT GRADING SYSTEM ***")
    while want_to_exit not in ('Y', 'y'):
        print("----------------------------")
        try:
            stud_id = int(input("Enter Student ID: "))
        except ValueError:
            stud_id = 0
            
        stud_name = input("Enter Student Name: ")
        
        try:
            math_mark = int(input("Enter Math Score (0-100): "))
        except ValueError:
            math_mark = 0
        try:
            sci_mark = int(input("Enter Science Score (0-100): "))
        except ValueError:
            sci_mark = 0
        try:
            eng_mark = int(input("Enter English Score (0-100): "))
        except ValueError:
            eng_mark = 0
        try:
            hist_mark = int(input("Enter History Score (0-100): "))
        except ValueError:
            hist_mark = 0

        total_marks = math_mark + sci_mark + eng_mark + hist_mark
        average_mark = total_marks / 4.0

        if average_mark >= 90:
            letter_grade = "A"
            pass_fail = "PASS"
        elif average_mark >= 80:
            letter_grade = "B"
            pass_fail = "PASS"
        elif average_mark >= 70:
            letter_grade = "C"
            pass_fail = "PASS"
        elif average_mark >= 60:
            letter_grade = "D"
            pass_fail = "PASS"
        else:
            letter_grade = "F"
            pass_fail = "FAIL"

        print(" ")
        print("===== ACADEMIC REPORT =====")
        print(f"Student: {stud_name} ({stud_id:06d})")
        print(f"Total Marks:   {total_marks:04d} / 400")
        print(f"Average Score: {average_mark:3.2f}")
        print(f"Final Grade:   {letter_grade}")
        print(f"Status:        {pass_fail}")
        print("===========================")

        want_to_exit = input("Grade another student? (N/Y): ").strip()
        
    print("System terminated.")

if __name__ == "__main__":
    main()
