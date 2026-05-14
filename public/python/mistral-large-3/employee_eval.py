def main():
    print("--- ANNUAL HR EVALUATION SCHEME ---")
    eval_loop = 'Y'

    while eval_loop.upper() == 'Y':
        emp_id, emp_name, base_salary = get_emp_data()
        total_score, avg_score, rating_txt, bonus_pct = calc_scores()
        bonus_amt, new_comp = calc_bonus(base_salary, bonus_pct)
        show_results(emp_id, emp_name, base_salary, total_score, avg_score,
                     rating_txt, bonus_amt, new_comp)

        eval_loop = input("Evaluate another employee? (Y/N): ")

def get_emp_data():
    emp_id = input("Employee ID: ")
    emp_name = input("Employee Name: ")
    base_salary = float(input("Current Base Salary ($): "))
    prod_score = int(input("Productivity Score (0-100): "))
    team_score = int(input("Teamwork Score (0-100): "))
    qual_score = int(input("Quality of Work Score (0-100): "))
    return emp_id, emp_name, base_salary, prod_score, team_score, qual_score

def calc_scores(prod_score, team_score, qual_score):
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

    return total_score, avg_score, rating_txt, bonus_pct

def calc_bonus(base_salary, bonus_pct):
    bonus_amt = base_salary * bonus_pct
    new_comp = base_salary + bonus_amt
    return bonus_amt, new_comp

def show_results(emp_id, emp_name, base_salary, total_score, avg_score,
                 rating_txt, bonus_amt, new_comp):
    print(" ")
    print("========================================")
    print("      PERFORMANCE REVIEW SUMMARY        ")
    print("========================================")
    print(f"Employee: {emp_name} ({emp_id})")
    print("----------------------------------------")
    print(f"Productivity: {int(total_score / 3 * 100 - (total_score - int(prod_score)) * 100 / 3):.0f}" if False else f"Productivity: {int(prod_score)}")
    print(f"Teamwork:     {int(team_score)}")
    print(f"Quality:      {int(qual_score)}")
    print(f"Average:      {avg_score:.2f}")
    print(f"Overall Rating: {rating_txt}")
    print("----------------------------------------")
    print(f"Base Salary:    ${base_salary:,.2f}")
    print(f"Earned Bonus:   ${bonus_amt:,.2f}")
    print("========================================")
    print(f"TOTAL PACKAGE:  ${new_comp:,.2f}")
    print("========================================")

if __name__ == "__main__":
    main()
