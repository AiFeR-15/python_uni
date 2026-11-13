import math

try:
    x=float(input("Введіть значення x (|x| < 1): "))
    eps = float(input("Введіть точність eps (пд, 0.1): "))

    assert abs(x) < 1, "Обмеження порушено: модуль x має бути строго меншим за 1!"
    assert eps > 0, "Обмеження порушено: точність eps має бути більшою за 0!"

    s=1
    term=x/2
    n=2
    while abs(term) >eps:
        s+=term
        multiplier=-x*(2*n-3)/(2*n)
        term=term * multiplier
        n+=1
    val= math.sqrt(1+x)
    error=abs(s-val)
    print("=== РЕЗУЛЬТАТИ ===")
    print(f"Обчислено через ряд Тейлора (s) : {s:.10f}")
    print(f"Точне значення (math.sqrt)     : {val:.10f}")
    print(f"Різниця (похибка)             : {error:.16f}")
except ValueError:
    print("Помилка вводу: Будь ласка, введіть числове значення.")
except AssertionError as error_msg:
    print(error_msg)