# Завдання 2
# Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

import random

def get_numbers_ticket(min, max, quantity):
    if 1 <= min <=1000 and 1 <= max <=1000 and min < max and quantity < max - min:
        numbers = list(range(min, max+1))
        print("Список чисел", numbers)
        list_numbers = random.sample(numbers, quantity)
        print("Список випадкових чисел зі списку", list_numbers)
        return list_numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
try:
    lottery_numbers.sort()
    print("Ваші лотерейні числа:", lottery_numbers)
except:
    print("Enter correct data")    
