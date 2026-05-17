import decimal
from decimal import Decimal

def get_emp_data():
    emp_id = input("Employee ID: ")
    emp_name = input("Employee Name: ")
    try:
        base_salary = Decimal(input("Current Base Salary ($): "))
        prod_score = int(input("Productivity Score (0-100): "))
        team_score = int(input("Teamwork Score (0-100): "))
        qual_score = int(input("Quality of Work Score (0-100): "))
    except ValueError:
        print("Invalid numeric input. Please restart.")
        return None
    
    return {
        "id": emp_id,
        "name": emp_name,
        "base_salary": base_salary,
        "prod_score": prod_score,
        "team_score": team_score,
        "qual_score": qual_score
    }

def calc_scores(data):
    total_score = data["prod_score"] + data["team_score"] + data["qual_score"]
    avg_score = Decimal(total_score) / 3
    
    if avg_score >= 90:
        rating_txt = "OUTSTANDING"
        bonus_pct = Decimal("0.15")
    elif avg_score >= 80:
        rating_txt = "EXCEEDS ELIG"
        bonus_pct = Decimal("0.10")
    elif avg_score >= 70:
        rating_txt = "MEETS ELIG"
        bonus_pct = Decimal("0.05")
    else:
        rating_txt = "NEEDS IMPRV"
        bonus_pct = Decimal("0.00")
        
    return avg_score, rating_txt, bonus_pct

def calc_bonus(base_salary, bonus_pct):
    bonus_amt = base_salary * bonus_pct
    new_comp = base_salary + bonus_amt
    return bonus_amt, new_comp

def show_results(data, avg_score, rating_txt, base_salary, bonus_amt, new_comp):
    def fmt_currency(val):
        return f"${val:,.2f}"

    print("\n========================================")
    print("      PERFORMANCE REVIEW SUMMARY        ")
    print("========================================")
    print(f"Employee: {data['name']} ({data['id']})")
    print("----------------------------------------")
    print(f"Productivity: {data['prod_score']}")
    print(f"Teamwork:     {data['team_score']}")
    print(f"Quality:      {data['qual_score']}")
    print(f"Average:      {avg_score:.2f}")
    print(f"Overall Rating: {rating_txt}")
    print("----------------------------------------")
    print(f"Base Salary:    {fmt_currency(base_salary)}")
    print(f"Earned Bonus:   {fmt_currency(bonus_amt)}")
    print("========================================")
    print(f"TOTAL PACKAGE:  {fmt_currency(new_comp)}")
    print("========================================")

def main():
    print("--- ANNUAL HR EVALUATION SCHEME ---")
    eval_loop = 'Y'
    while eval_loop.upper() == 'Y':
        data = get_emp_data()
        if data is None:
            break
            
        avg_score, rating_txt, bonus_pct = calc_scores(data)
        bonus_amt, new_comp = calc_bonus(data["base_salary"], bonus_pct)
        show_results(data, avg_score, rating_txt, data["base_salary"], bonus_amt, new_comp)
        
        eval_loop = input("Evaluate another employee? (Y/N): ")

if __name__ == "__main__":
    main()
