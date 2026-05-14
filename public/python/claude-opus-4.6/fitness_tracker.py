"""
Daily Fitness Tracker
Converted from COBOL (fitness_tracker.cbl) to Python
"""


def main():
    print("--- DAILY FITNESS TRACKER ---")
    user_name = input("User Name: ")
    weight_lbs = int(input("Weight (lbs): "))
    height_in = int(input("Height (inches): "))
    daily_steps = int(input("Steps taken today: "))
    activity_level = int(input("Activity (1=Sedentary, 2=Active, 3=Pro): "))

    bmi_score = (weight_lbs / (height_in * height_in)) * 703
    baseline_bmr = weight_lbs * 11
    cals_burned = int(daily_steps * 0.04)

    if activity_level == 1:
        total_cals = int(baseline_bmr * 1.2)
    elif activity_level == 2:
        total_cals = int(baseline_bmr * 1.5)
    elif activity_level == 3:
        total_cals = int(baseline_bmr * 1.8)
    else:
        total_cals = int(baseline_bmr * 1.2)

    total_cals += cals_burned

    print()
    print("=======================================")
    print("         FITNESS DASHBOARD             ")
    print("=======================================")
    print(f"Hello, {user_name}!")
    print("---------------------------------------")
    print(f"BMI Score:     {bmi_score:.1f}")
    if bmi_score < 18.5:
        print("Category:      Underweight")
    elif bmi_score < 25.0:
        print("Category:      Normal Weight")
    elif bmi_score < 30.0:
        print("Category:      Overweight")
    else:
        print("Category:      Obese")
    print("---------------------------------------")
    print(f"Steps Today:   {daily_steps}")
    print(f"Active Cals Burned: {cals_burned:>9,}")
    print(f"Total TDEE Cals:    {total_cals:>9,}")
    print("=======================================")


if __name__ == "__main__":
    main()
