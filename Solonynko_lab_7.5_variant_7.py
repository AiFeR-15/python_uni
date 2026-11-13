import math

def root4_generator(x):
    x_prev = x / 4
    yield x_prev
    
    while True:
        x_curr = (1 / 4) * (3 * x_prev + x / (x_prev ** 3))
        yield x_curr
        x_prev = x_curr



print("--- Корінь 4-го степеня ---")

while True:
    try:
        x = float(input("Введіть число x (x > 0): "))
        epsilon = float(input("Введіть точність epsilon (наприклад, 0.0001): "))
        
        assert x > 0, "Число x має бути строго більшим за 0."
        assert epsilon > 0, "Точність epsilon має бути більшою за 0."
        
        
        break 
        
    except ValueError:
        print("Помилка: Ви ввели літери або інші некоректні символи. Будь ласка, вводьте числа!")
    except AssertionError as error_msg:
        print(f"Помилка логіки: {error_msg}")


gen = root4_generator(x)

x_prev = next(gen)

step = 1
while True:
    x_curr = next(gen)

    if abs(x_curr - x_prev) < epsilon:
        final_result = x_curr 
        break
        
    x_prev = x_curr
    step += 1

math_result = math.pow(x, 0.25)
error=abs(final_result-math_result)
print("-" * 40)
print(f"Знайдено за {step} кроків.")
print(f"Наш результат (генератор) : {final_result}")
print(f"Результат бібліотеки math : {math_result}")
print(f"Похибка : {error:.16f}")
print("-" * 40)