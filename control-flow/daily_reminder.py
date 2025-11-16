task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it as soon as possible.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. Complete it as soon as possible!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Complete it when you have the chance.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task. Complete it when you have time.")
        else:
            print(f"Reminder: '{task}' is a low priority task. Complete it when you're free.")

    case _:
        print("Invalid priority level entered.")
