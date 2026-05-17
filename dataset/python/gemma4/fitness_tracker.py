import math

def main():
    print("--- DAILY FITNESS TRACKER ---")
    
    user_name = input("User Name: ")
    try:
        weight_lbs = float(input("Weight (lbs): "))
        height_in = float(input("Height (inches): "))
        daily_steps = int(input("Steps taken today: "))
        activity_level = int(input("Activity (1=Sedentary, 2=Active, 3=Pro): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for weight, height, steps, and activity.")
        return

    # Compute Metrics
    bmi_score = (weight_lbs / (height_in * height_in)) * 703
    baseline_bmr = weight_lbs * 11
    cals_burned = daily_steps * 0.04

    # Determine TDEE based on activity level
    if activity_level == 2: # Active
        total_cals = baseline_bmr * 1.5
    elif activity_level == 3: # Highly Active
        total_cals = baseline_bmr * 1.8
    else: # Sedentary or Other
        total_cals = baseline_bmr * 1.2

    total_cals += cals_burned

    # Print Dashboard
    print("\n=======================================")
    print("         FITNESS DASHBOARD             ")
    print("=======================================")
    print(f"Hello, {user_name}!")
    print("---------------------------------------")
    print(f"BMI Score:     {bmi_score:.1f}")
    
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
    print(f"Active Cals Burned: {int(cals_burned):,}")
    print(f"Total TDEE Cals:    {int(total_cals):,}")
    print("=======================================")

if __name__ == "__main__":
    main()
