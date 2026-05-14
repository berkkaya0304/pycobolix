class StudentGradingSystem:
    def __init__(self):
        self.student_id = ""
        self.student_name = ""
        self.math_mark = 0
        self.sci_mark = 0
        self.eng_mark = 0
        self.hist_mark = 0
        self.total_marks = 0
        self.average_mark = 0.0
        self.letter_grade = ""
        self.pass_fail = ""

    def input_student(self):
        print("----------------------------")
        self.student_id = input("Enter Student ID: ")
        self.student_name = input("Enter Student Name: ")
        
        while True:
            try:
                self.math_mark = int(input("Enter Math Score (0-100): "))
                if 0 <= self.math_mark <= 100:
                    break
                print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
                
        while True:
            try:
                self.sci_mark = int(input("Enter Science Score (0-100): "))
                if 0 <= self.sci_mark <= 100:
                    break
                print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
                
        while True:
            try:
                self.eng_mark = int(input("Enter English Score (0-100): "))
                if 0 <= self.eng_mark <= 100:
                    break
                print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
                
        while True:
            try:
                self.hist_mark = int(input("Enter History Score (0-100): "))
                if 0 <= self.hist_mark <= 100:
                    break
                print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    def calc_grades(self):
        self.total_marks = self.math_mark + self.sci_mark + self.eng_mark + self.hist_mark
        self.average_mark = self.total_marks / 4.0
        
        if self.average_mark >= 90:
            self.letter_grade = "A"
            self.pass_fail = "PASS"
        elif self.average_mark >= 80:
            self.letter_grade = "B"
            self.pass_fail = "PASS"
        elif self.average_mark >= 70:
            self.letter_grade = "C"
            self.pass_fail = "PASS"
        elif self.average_mark >= 60:
            self.letter_grade = "D"
            self.pass_fail = "PASS"
        else:
            self.letter_grade = "F"
            self.pass_fail = "FAIL"

    def display_report(self):
        print("\n===== ACADEMIC REPORT =====")
        print(f"Student: {self.student_name} ({self.student_id})")
        print(f"Total Marks:   {self.total_marks} / 400")
        print(f"Average Score: {self.average_mark:.2f}")
        print(f"Final Grade:   {self.letter_grade}")
        print(f"Status:        {self.pass_fail}")
        print("===========================")

def main():
    print("*** STUDENT GRADING SYSTEM ***")
    
    while True:
        system = StudentGradingSystem()
        system.input_student()
        system.calc_grades()
        system.display_report()
        
        while True:
            response = input("Grade another student? (N/Y): ").strip().upper()
            if response in ['Y', 'N']:
                break
            print("Please enter 'Y' or 'N'.")
            
        if response == 'N':
            break
    
    print("System terminated.")

if __name__ == "__main__":
    main()
