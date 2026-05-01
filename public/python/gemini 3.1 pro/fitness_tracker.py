def main():
    print("--- DAILY FITNESS TRACKER ---")
    user_name = input("User Name: ")
    try:
        weight_lbs = float(input("Weight (lbs): "))
    except ValueError:
        weight_lbs = 150.0  # default safe value
    try:
        height_in = float(input("Height (inches): "))
    except ValueError:
        height_in = 65.0    # default safe value
    try:
        daily_steps = int(input("Steps taken today: "))
    except ValueError:
        daily_steps = 0
    activity_level = input("Activity (1=Sedentary, 2=Active, 3=Pro): ").strip()

    if height_in > 0:
        bmi_score = (weight_lbs / (height_in * height_in)) * 703
    else:
        bmi_score = 0.0

    baseline_bmr = weight_lbs * 11
    cals_burned = daily_steps * 0.04

    if activity_level == '1':
        total_cals = baseline_bmr * 1.2
    elif activity_level == '2':
        total_cals = baseline_bmr * 1.5
    elif activity_level == '3':
        total_cals = baseline_bmr * 1.8
    else:
        total_cals = baseline_bmr * 1.2

    total_cals += cals_burned

    print("\n=======================================")
    print("         FITNESS DASHBOARD             ")
    print("=======================================")
    print(f"Hello, {user_name}!")
    print("---------------------------------------")
    print(f"BMI Score:     {bmi_score:5.1f}")
    
    if bmi_score < 18.5:
        category = "Underweight"
    elif bmi_score < 25.0:
        category = "Normal Weight"
    elif bmi_score < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
        
    print(f"Category:      {category}")
    print("---------------------------------------")
    print(f"Steps Today:   {daily_steps}")
    print(f"Active Cals Burned: {int(cals_burned):6d}")
    print(f"Total TDEE Cals:    {int(total_cals):6d}")
    print("=======================================")

if __name__ == "__main__":
    main()
