from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    greetings_list = []
    date_pattern = "%Y.%m.%d"

    current_date = datetime.today().date()
    current_year = current_date.year

    for user in users:
        user_borne_date = datetime.strptime(user["birthday"], date_pattern).date()
        birthday = datetime(current_year, user_borne_date.month, user_borne_date.day).date()

        delta_days = (birthday - current_date).days
        is_upcoming = delta_days >= 0 and delta_days <= 7

        if is_upcoming:
            extra_days = 0 if birthday.weekday() < 5 else (7 - birthday.weekday())
            greetings_date = birthday + timedelta(extra_days)
            user_greeting_data = {
                "name": user["name"], 
                "congratulation_date": datetime.strftime(greetings_date, date_pattern)
            }
            greetings_list.append(user_greeting_data)
        
    return greetings_list


test_users = [
    {"name": "John 01", "birthday": "1985.10.05"},
    {"name": "John 02", "birthday": "1985.10.06"},
    {"name": "John 03", "birthday": "1985.10.07"},
    {"name": "John 04", "birthday": "1995.10.08"},
    {"name": "John 05", "birthday": "1995.10.09"},
    {"name": "John 06", "birthday": "1985.10.10"},
    {"name": "John 07", "birthday": "1985.10.11"},
    {"name": "Tony 08", "birthday": "1985.10.12"},
    {"name": "Tony 09", "birthday": "1985.10.13"},
    {"name": "Jane 10", "birthday": "1975.10.14"},
    {"name": "Jane 11", "birthday": "1965.10.15"},
    {"name": "Jane 12", "birthday": "1985.10.16"},
    {"name": "Jane 13", "birthday": "1985.10.17"},
    {"name": "Jane 14", "birthday": "1985.10.18"}
]

upcoming_birthdays = get_upcoming_birthdays(test_users)
print("This week's Greetings List:")
for row in upcoming_birthdays:
    print(f"Name: {row['name']:<16} Date:{row['congratulation_date']:<16}")
