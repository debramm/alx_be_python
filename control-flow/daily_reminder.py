task = input("Enter your task: ").strip()


priority = input("Priority (high/medium/low): ").strip().lower()
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter 'high', 'medium', or 'low'.")
    priority = input("Priority (high/medium/low): ").strip().lower()


time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
while time_bound not in ["yes", "no"]:
    print("Invalid input! Please enter 'yes' or 'no'.")
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."


print("\nReminder:", reminder)