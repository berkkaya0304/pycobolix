"""
Annual HR Evaluation Scheme - Employee Evaluation
Converted from COBOL (employee_eval.cbl) to Python
"""


def main():
    print("--- ANNUAL HR EVALUATION SCHEME ---")
    eval_loop = "Y"

    while eval_loop.upper() == "Y":
        # Get employee data
        emp_id = input("Employee ID: ")
        emp_name = input("Employee Name: ")
        base_salary = float(input("Current Base Salary ($): "))
        prod_score = int(input("Productivity Score (0-100): "))
        team_score = int(input("Teamwork Score (0-100): "))
        qual_score = int(input("Quality of Work Score (0-100): "))

        # Calculate scores
        total_score = prod_score + team_score + qual_score
        avg_score = total_score / 3

        if avg_score >= 90:
            rating_txt = "OUTSTANDING"
            bonus_pct = 0.15
        elif avg_score >= 80:
            rating_txt = "EXCEEDS ELIG"
            bonus_pct = 0.10
        elif avg_score >= 70:
            rating_txt = "MEETS ELIG"
            bonus_pct = 0.05
        else:
            rating_txt = "NEEDS IMPRV"
            bonus_pct = 0.00

        # Calculate bonus
        bonus_amt = base_salary * bonus_pct
        new_comp = base_salary + bonus_amt

        # Show results
        print()
        print("========================================")
        print("      PERFORMANCE REVIEW SUMMARY        ")
        print("========================================")
        print(f"Employee: {emp_name} ({emp_id})")
        print("----------------------------------------")
        print(f"Productivity: {prod_score}")
        print(f"Teamwork:     {team_score}")
        print(f"Quality:      {qual_score}")
        print(f"Average:      {avg_score:.2f}")
        print(f"Overall Rating: {rating_txt}")
        print("----------------------------------------")
        print(f"Base Salary:    ${base_salary:>12,.2f}")
        print(f"Earned Bonus:   ${bonus_amt:>12,.2f}")
        print("========================================")
        print(f"TOTAL PACKAGE:  ${new_comp:>12,.2f}")
        print("========================================")

        eval_loop = input("Evaluate another employee? (Y/N): ").strip().upper()


if __name__ == "__main__":
    main()
