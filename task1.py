# Завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

import datetime

today = datetime.date.today()

from datetime import datetime

def get_days_from_today(date):    
    try:
        user_date = datetime.strptime(date, "%Y-%m-%d")
        number_of_days = today.toordinal() - user_date.toordinal()
        return number_of_days
    except ValueError:
        print("Enter corect date")

res = get_days_from_today("2020-10-09")
print(f"Між заданою датою і сьогодні - {res} днів")