while True:
    try:
        num1=float(input("Num1: "))
        break
    except ValueError as e:
        print("Помилка! Ви ввели неправильний знак. Спробуйте ще раз!")
while True:
    try:
        sign = input("Введіть знак операції (+,-,*,/): ").strip()

        if sign not in ['+', '-', '*', '/']:
            raise ValueError("Помилка! Ви ввели неправильний знак. Спробуйте ще раз!")
        break
    except ValueError as e:
        print(e)
while True:
    try:
        num2=float(input("Num2: "))
        if sign == '+':
            print(f"Дорівнює: {num1+num2}")
        elif sign == '-':
            print(f"Дорівнює: {num1-num2}")
        elif sign == '*':
            print(f"Дорівнює: {num1*num2}")
        elif sign == '/':
            print(f"Дорівнює: {num1/num2}")
        break
    except ValueError as e:
        print(e)
    except ZeroDivisionError:
        print("Помилка! На нуль ділити не можна. Спробуйте ще раз!")