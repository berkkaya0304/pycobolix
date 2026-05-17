class FitnessTracker:
    def __init__(self):
        self.user_name = ""
        self.weight_lbs = 0
        self.height_in = 0
        self.daily_steps = 0
        self.activity_level = 1
        self.bmi_score = 0.0
        self.cals_burned = 0
        self.baseline_bmr = 0
        self.total_cals = 0

    def get_user_input(self):
        print("--- DAILY FITNESS TRACKER ---")
        self.user_name = input("User Name: ")
        self.weight_lbs = int(input("Weight (lbs): "))
        self.height_in = int(input("Height (inches): "))
        self.daily_steps = int(input("Steps taken today: "))
        print("Activity (1=Sedentary, 2=Active, 3=Pro): ")
        self.activity_level = int(input())

    def compute_metrics(self):
        self.bmi_score = (self.weight_lbs / (self.height_in * self.height_in)) * 703
        self.baseline_bmr = self.weight_lbs * 11
        self.cals_burned = self.daily_steps * 0.04
        
        if self.activity_level == 1:
            self.total_cals = self.baseline_bmr * 1.2
        elif self.activity_level == 2:
            self.total_cals = self.baseline_bmr * 1.5
        elif self.activity_level == 3:
            self.total_cals = self.baseline_bmr * 1.8
        else:
            self.total_cals = self.baseline_bmr * 1.2
            
        self.total_cals += self.cals_burned

    def print_dashboard(self):
        print("\n=======================================")
        print("         FITNESS DASHBOARD             ")
        print("=======================================")
        print(f"Hello, {self.user_name}!")
        print("---------------------------------------")
        print(f"BMI Score:     {self.bmi_score:.1f}")
        
        if self.bmi_score < 18.5:
            print("Category:      Underweight")
        elif self.bmi_score < 25.0:
            print("Category:      Normal Weight")
        elif self.bmi_score < 30.0:
            print("Category:      Overweight")
        else:
            print("Category:      Obese")
            
        print("---------------------------------------")
        print(f"Steps Today:   {self.daily_steps:,}")
        print(f"Active Cals Burned: {self.cals_burned:,.0f}")
        print(f"Total TDEE Cals:    {self.total_cals:,.0f}")
        print("=======================================")

    def run(self):
        self.get_user_input()
        self.compute_metrics()
        self.print_dashboard()

if __name__ == "__main__":
    tracker = FitnessTracker()
    tracker.run()
