from datetime import datetime

def get_days_from_today(date):
    try:
        return (datetime.today() - datetime.strptime(date, "%Y-%m-%d")).days
    
    except ValueError as e:
        print(f"'{date if date else 'Empty input'}' does not match format 'YYYY-MM-DD'")
    
    return None


input_date = input("Enter date in 'YYYY-MM-DD' format >>> ").strip()
difference = get_days_from_today(input_date)

if difference:
    print(f"Difference between today and '{input_date}' is {difference} days.")
else:
    print(f"Incorrect input date format: '{input_date if input_date else 'Empty input'}'")