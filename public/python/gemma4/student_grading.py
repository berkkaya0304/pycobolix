def calculate_grade(average):
    if average >= 90:
        return "A", "PASS"
    elif average >= 80:
        return "B", "PASS"
    elif average >= 70:
        return "C", "PASS"
    elif average >= 60:
        return "D", "PASS"
    else:
        return "F", "FAIL"

def main():
    print("*** STUDENT GRADING SYSTEM ***")
    
    while True:
        print("----------------------------")
        try:
            stud_id = input("Enter Student ID: ")
            stud_name = input("Enter Student Name: ")
            math_mark = float(input("Enter Math Score (0-100): "))
            sci_mark = float(input("Enter Science Score (0-100): "))
            eng_mark = float(input("Enter English Score (0-100): "))
            hist_mark = float(input("Enter History Score (0-100): "))
        except ValueError:
            print("Invalid input. Please enter numeric values for scores.")
            continue

        total_marks = math_mark + sci_mark + eng_mark + hist_mark
        average_mark = total_marks / 4
        letter_grade, pass_fail = calculate_grade(average_mark)

        print("\n===== ACADEMIC REPORT =====")
        print(f"Student: {stud_name} ({stud_id})")
        print(f"Total Marks:   {total_marks:.0f} / 400")
        print(f"Average Score: {average_mark:.2f}")
        print(f"Final Grade:   {letter_grade}")
        print(f"Status:        {pass_fail}")
        print("===========================")

        want_to_exit = input("Grade another student? (N/Y): ").strip().upper()
        if want_to_exit == 'Y':
            break

    print("System terminated.")

if __name__ == "__main__":
    main()
