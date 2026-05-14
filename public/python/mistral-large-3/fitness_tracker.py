def fitness_tracker():
    print("--- DAILY FITNESS TRACKER ---")
    user_name = input("User Name: ").strip()
    weight_lbs = int(input("Weight (lbs): "))
    height_in = int(input("Height (inches): "))
    daily_steps = int(input("Steps taken today: "))
    activity_level = int(input("Activity (1=Sedentary, 2=Active, 3=Pro): "))

    bmi_score, cals_burned, total_cals = compute_metrics(weight_lbs, height_in, daily_steps, activity_level)
    print_dashboard(user_name, bmi_score, daily_steps, cals_burned, total_cals)

def compute_metrics(weight_lbs, height_in, daily_steps, activity_level):
    bmi_score = (weight_lbs / (height_in ** 2)) * 703
    baseline_bmr = weight_lbs * 11
    cals_burned = daily_steps * 0.04

    if activity_level == 1:
        total_cals = baseline_bmr * 1.2
    elif activity_level == 2:
        total_cals = baseline_bmr * 1.5
    elif activity_level == 3:
        total_cals = baseline_bmr * 1.8
    else:
        total_cals = baseline_bmr * 1.2

    total_cals += cals_burned
    return bmi_score, cals_burned, total_cals

def print_dashboard(user_name, bmi_score, daily_steps, cals_burned, total_cals):
    print("\n=======================================")
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
    print(f"Steps Today:   {daily_steps:,}")
    print(f"Active Cals Burned: {int(cals_burned):,}")
    print(f"Total TDEE Cals:    {int(total_cals):,}")
    print("=======================================")

if __name__ == "__main__":
    fitness_tracker()
