
x = float(input("Введіть дійсне число x:"))
E = float(input("Введіть точність eps(E>0): "))

a_prev = x
print(f"a_0={a_prev}")

found = False

for n in range(1,101):
    a_curr = (4/5)* a_prev + x/(5*a_prev**4)
    print(f"a_{n}={a_curr: .4f}")
    if abs(a_curr - a_prev)<E:
        print("\nУмова виконана!")
        print(f"Шуканий член a_{n} = {a_curr}")
        print(f"Його номер n = {n}")
        found = True
        break
    a_prev = a_curr
if not found:
    print("\nУмову не було досягнуто за 100 кроків.")
