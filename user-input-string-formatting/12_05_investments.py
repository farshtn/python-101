# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

invest_amount = int(input("please enter your investment amount: "))
interest_rate_percent = float(input("please enter your interest rate in percentage: "))/100
years_number = int(input("please enter the number of years to invest: "))
future_value = float((invest_amount * ((1 + interest_rate_percent) ** years_number)))

print(f"The future value of the investment is: ${future_value}")