#advanced_version
days_in_month = {
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

months = int(input("Enter a month number (1-12): "))

if months in days_in_month:
    if months == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        print("Days: 29" if leap == "yes" else "Days: 28")
    else:
        print(f"{months}: {days_in_month[months]}")
else:
    print("It has to be between 1-12, please write number between 1-12.")