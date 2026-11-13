import math

def calculate_ln(x, eps=0.00000001):
    s=0
    den=1
    term = x / den
    while abs(term)>eps:
        s+=term
        term=term*(x**2)*den/(den+2)
        den+=2
    return s*2


try:
    x=float(input("Введіть значення x (|x| < 1): "))
    eps = float(input("Введіть точність eps (пд, 0.1): "))

    assert abs(x) < 1, "Обмеження порушено: модуль x має бути строго меншим за 1!"
    assert eps > 0, "Обмеження порушено: точність eps має бути більшою за 0!"

    result = calculate_ln(x, eps)
    val = math.log((1+x)/(1-x))
    error=abs(result-val)
    print("=== РЕЗУЛЬТАТИ ===")
    print(f"Обчислено через ряд Тейлора (s) : {result:.10f}")
    print(f"Точне значення (math.log)     : {val:.10f}")
    print(f"Різниця (похибка)             : {error:.16f}")
except ValueError:
    print("Помилка вводу: Будь ласка, введіть числове значення.")
except AssertionError as error_msg:
    print(error_msg)