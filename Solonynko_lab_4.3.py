import re
email=input("Введіть e-mail: ")
pattern= r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"

if not re.fullmatch(pattern, email):
    print("Некоректна адреса (помилка в структурі, знаку @ або домені)")
else:
    print("Ok")