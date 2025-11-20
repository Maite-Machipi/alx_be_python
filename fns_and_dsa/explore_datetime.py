from datetime import datetime, timedelta

def display_current_datetime():
    # Part 1: Display the current date and time
    current_date = datetime.now()  # Save in variable as required
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    # Part 2: Calculate a future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # Save in variable
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    display_current_datetime()

    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
