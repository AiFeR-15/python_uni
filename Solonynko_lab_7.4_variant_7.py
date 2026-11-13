import math

def cos_sequence_generator(n):
    for i in range(n + 1):  

        term = math.cos(math.pi / (2 ** i))
        print(f"Доданок №{i+1} = {term:.8f}")
        # yield повертає значення і "ставить функцію на паузу"
        yield term 

print("--- Виконання ---")

while True:
    try:
        n = int(input("Введіть натуральне число n: "))
        if n < 1:
            print("n має бути натуральним (більше 0).")
            continue
        break
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Створюю об'єкт генератора
generator = cos_sequence_generator(n)

# 2. Функція sum() автоматично "прокручує" генератор до кінця,
# дістаючи числа по одному через yield, і додає їх усі разом
total_sum = sum(generator)

print(f"Сума ряду для n={n} дорівнює: {total_sum}")