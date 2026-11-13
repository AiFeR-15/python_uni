import math
import time # Додаємо бібліотеку для роботи з часом

# === Створюємо декоратор ===
def benchmark(func):
    """Декоратор для вимірювання часу виконання функції"""
    def wrapper(*args, **kwargs): # Приймає будь-які аргументи
        # 1. Засікаємо час ДО виконання
        start_time = time.perf_counter() 
        
        # 2. Виконуємо саму функцію (calculate_ln)
        result = func(*args, **kwargs) 
        
        # 3. Засікаємо час ПІСЛЯ виконання
        end_time = time.perf_counter()
        
        # 4. Рахуємо різницю і виводимо
        execution_time = end_time - start_time
        print(f"\n[Декоратор] Час виконання функції '{func.__name__}': {execution_time:.10f} сек")
        
        # 5. Повертаємо результат, щоб програма працювала як раніше
        return result 
    return wrapper

# === Застосовуємо декоратор до твоєї функції ===
# Символ @ застосовує декоратор benchmark до calculate_ln
@benchmark 
def calculate_ln(x, eps=0.00000001):
    s = 0
    den = 1
    term = x / den
    while abs(term) > eps:
        s += term
        term = term * (x**2) * den / (den + 2)
        den += 2
    return s * 2


# === ГОЛОВНА ПРОГРАМА (твій код без змін) ===
try:
    x = float(input("Введіть значення x (|x| < 1): "))
    eps = float(input("Введіть точність eps (пд, 0.1): "))

    assert abs(x) < 1, "Обмеження порушено: модуль x має бути строго меншим за 1!"
    assert eps > 0, "Обмеження порушено: точність eps має бути більшою за 0!"

    result = calculate_ln(x, eps)
    val = math.log((1+x)/(1-x))
    error = abs(result - val)
    
    print("\n=== РЕЗУЛЬТАТИ ===")
    print(f"Обчислено через ряд Тейлора (s) : {result:.10f}")
    print(f"Точне значення (math.log)       : {val:.10f}")
    print(f"Різниця (похибка)               : {error:.16f}")
    
except ValueError:
    print("Помилка вводу: Будь ласка, введіть числове значення.")
except AssertionError as error_msg:
    print(error_msg)