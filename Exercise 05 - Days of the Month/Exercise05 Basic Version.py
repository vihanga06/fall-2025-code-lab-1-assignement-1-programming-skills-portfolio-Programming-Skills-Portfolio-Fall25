# basic_version

days_in_months = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

months = input("Enter a number of a month between (1-12): ")

if months.isdigit():
    month_numbers = int(months)
    if month_numbers in days_in_months:
        print(f"Month {month_numbers} has {days_in_months[month_numbers]} days.")
    else:
        print("Your number is not between 1-12, Enter a number between 1-12.")

else: 
    print("What you entered is not a number. Please enter a NUMBER.")