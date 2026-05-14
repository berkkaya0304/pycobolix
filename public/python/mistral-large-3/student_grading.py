def student_grading_system():
    print("*** STUDENT GRADING SYSTEM ***")

    while True:
        student_id = input("----------------------------\nEnter Student ID: ")
        student_name = input("Enter Student Name: ")

        math_mark = int(input("Enter Math Score (0-100): "))
        sci_mark = int(input("Enter Science Score (0-100): "))
        eng_mark = int(input("Enter English Score (0-100): "))
        hist_mark = int(input("Enter History Score (0-100): "))

        total_marks = math_mark + sci_mark + eng_mark + hist_mark
        average_mark = total_marks / 4

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

        print("\n===== ACADEMIC REPORT =====")
        print(f"Student: {student_name} ({student_id})")
        print(f"Total Marks:   {total_marks} / 400")
        print(f"Average Score: {average_mark:.2f}")
        print(f"Final Grade:   {letter_grade}")
        print(f"Status:        {pass_fail}")
        print("===========================")

        exit_choice = input("Grade another student? (N/Y): ").strip().upper()
        if exit_choice != 'Y':
            print("System terminated.")
            break

if __name__ == "__main__":
    student_grading_system()
