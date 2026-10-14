import re
email=input("Введіть e-mail: ")
pattern= r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
flag=True
if not re.fullmatch(pattern, email):
    print("Некоректна адреса (помилка в структурі, знаку @ або домені)")
    flag = False
else:
    local_domain, domain = email.split("@")
    parts=domain.split(".")
    if ".." in email:
        print("Некоректна адреса: \".\" неможе йти послідовно декілька разів")
        flag = False
    elif local_domain.startswith(".") or local_domain.endswith("."):
        print("Некоректна адреса: \".\" неможе стояти на початку або вкінці локального домена")
        flag = False
    elif len(local_domain)>63:
        print(f"Некоректна адерса: частина {local_domain} перевищує 63 символи")
        flag = False
    elif domain.startswith("-") or domain.endswith("-"):
        print("Некоректна адреса: \"-\" неможе стояти на початку або вкінці домена")
        flag = False
    elif parts[-1].isdigit():
        print("Некоректна адреса: домен верхнього рівня не може складатися тільки з цифр")
        flag = False
    else:
        for part in parts:
            if len(part) > 63:
                print(f"Некоректна адреса: частина {part} перевищує 63 символи")
                flag=False
                break
            elif part.startswith("-") or part.endswith("-"):
                print(f"Некоректна адреса: частина '{part}' не може починатися або закінчуватися дефісом")
                flag=False
                break
if flag:
    print("Адреса електронної пошти абсолютно коректна!")
    
        