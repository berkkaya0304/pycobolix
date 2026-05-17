class EmployeeEvaluation:
    def __init__(self):
        self.emp_id = ""
        self.emp_name = ""
        self.base_salary = 0.0
        self.prod_score = 0
        self.team_score = 0
        self.qual_score = 0
        self.total_score = 0
        self.avg_score = 0.0
        self.bonus_pct = 0.0
        self.bonus_amt = 0.0
        self.new_comp = 0.0
        self.rating_txt = ""

    def get_emp_data(self):
        self.emp_id = input("Employee ID: ")
        self.emp_name = input("Employee Name: ")
        self.base_salary = float(input("Current Base Salary ($): "))
        self.prod_score = int(input("Productivity Score (0-100): "))
        self.team_score = int(input("Teamwork Score (0-100): "))
        self.qual_score = int(input("Quality of Work Score (0-100): "))

    def calc_scores(self):
        self.total_score = self.prod_score + self.team_score + self.qual_score
        self.avg_score = self.total_score / 3.0

        if self.avg_score >= 90:
            self.rating_txt = "OUTSTANDING"
            self.bonus_pct = 0.15
        elif self.avg_score >= 80:
            self.rating_txt = "EXCEEDS ELIG"
            self.bonus_pct = 0.10
        elif self.avg_score >= 70:
            self.rating_txt = "MEETS ELIG"
            self.bonus_pct = 0.05
        else:
            self.rating_txt = "NEEDS IMPRV"
            self.bonus_pct = 0.00

    def calc_bonus(self):
        self.bonus_amt = self.base_salary * self.bonus_pct
        self.new_comp = self.base_salary + self.bonus_amt

    def show_results(self):
        print("\n" + "=" * 40)
        print("      PERFORMANCE REVIEW SUMMARY        ")
        print("=" * 40)
        print(f"Employee: {self.emp_name} ({self.emp_id})")
        print("-" * 40)
        print(f"Productivity: {self.prod_score}")
        print(f"Teamwork:     {self.team_score}")
        print(f"Quality:      {self.qual_score}")
        print(f"Average:      {self.avg_score:.2f}")
        print(f"Overall Rating: {self.rating_txt}")
        print("-" * 40)
        print(f"Base Salary:    ${self.base_salary:,.2f}")
        print(f"Earned Bonus:   ${self.bonus_amt:,.2f}")
        print("=" * 40)
        print(f"TOTAL PACKAGE:  ${self.new_comp:,.2f}")
        print("=" * 40)

def main():
    print("--- ANNUAL HR EVALUATION SCHEME ---")
    while True:
        emp = EmployeeEvaluation()
        emp.get_emp_data()
        emp.calc_scores()
        emp.calc_bonus()
        emp.show_results()
        
        another = input("Evaluate another employee? (Y/N): ").strip().upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
