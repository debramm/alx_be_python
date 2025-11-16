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
        priority_message = "high priority task"
    case "medium":
        priority_message = "medium priority task"
    case "low":
        priority_message = "low priority task"


if time_bound == "yes":
    reminder_message = f"{task}' is a {priority_message} that requires immediate attention today!"
else:
    reminder_message = f"'{task}' is a {priority_message}. Consider completing it when you have free time."


print(f"Reminder: {reminder_message}")