#finance_calculator.py
#Program to calculate monthly and projected annual savings with interest

#Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#calculate projected annual savings with 5% annual interest
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

#Display the results
print(f"\nYour monthly savings are ${monthly_savings:.2f}.")
print(f"projected savings after one year, with interest is: ${projected_savings:.2f}.")
