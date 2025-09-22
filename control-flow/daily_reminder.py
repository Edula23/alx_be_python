task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
match (priority, time_bound):
    case ("high", "yes"):
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case ("medium", "yes"):
        print(f"Reminder: '{task}' is a medium priority task that needs attention today!")
    case ("medium", "no"):
        print(f"Reminder: '{task}' is a medium priority task. Please complete it soon.")
    case ("low", "yes"):
        print(f"Reminder: '{task}' is a low priority task. That can be scheduled for later.")
    case ("low", "no"):
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")