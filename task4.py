# Завдання 4
# У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
# У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.

from datetime import datetime, timedelta, date

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    result = []

    for user in users:
        user_name = user['name']
        user_birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            result.append({
                "name": user_name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return result

users = [
    {"name": "John Doe", "birthday": "1985.06.16"},
    {"name": "Jane Smith", "birthday": "1990.06.21"},
    {"name": "Nazar G", "birthday": "2005.10.04"},
    {"name": "Sofia G", "birthday": "2024.06.18"}
    ]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)