#daily_reminder.py
#Program to give a reminder about a single priority task

#Get user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#BAse reminder message
reminder_message = ""

# Process based on priority using match-case
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' has an unknown priority level"

# Modify message if time-bound
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Output the final reminder
print("\nReminder:", reminder_message)
