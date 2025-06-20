# Завдання 3
# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ '+'. Якщо номер не містить міжнародного коду, функція автоматично додає код '+38' (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

import re

def normalize_phone(phone_number):
    pattern = r"\D"
    replacement = ""
    modified_number = re.sub(pattern, replacement, phone_number)
    match = re.search(r"38", modified_number)
    if match:
        modified_number = "+" + modified_number
    else:
        modified_number = "+38" + modified_number
    return modified_number 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = []

for num in raw_numbers:
    numbers = normalize_phone(num)
    sanitized_numbers.append(numbers)

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
