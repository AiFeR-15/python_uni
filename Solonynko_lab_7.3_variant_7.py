def find_min_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    
    min_in_rest = find_min_recursive(lst[1:])
    
    if lst[0] < min_in_rest:
        return lst[0]
    else:
        return min_in_rest

print("--- Завдання 3 (Варіант 7): Мінімальне число в послідовності ---")
print("Вводьте натуральні числа по одному. Для завершення введіть 0.")

numbers = []

while True:
    try:
        val = int(input("Введіть число (0 для виходу): "))
        if val == 0:
            break
        if val < 0:
            print("Помилка: Число має бути натуральним (більшим за 0). Спробуйте ще.")
            continue
        numbers.append(val)
    except ValueError:
        print("Помилка! Будь ласка, введіть ціле число.")

if len(numbers) == 0:
    print("Ви не ввели жодного числа (окрім нуля).")
else:
    result_min = find_min_recursive(numbers)
    
    print(f"Введена послідовність : {numbers}")
    print(f"Мінімальне число      : {result_min}")