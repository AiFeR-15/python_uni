def GetDigit(c):
    if c.isdigit():
        return int(c)
    else:
        return -1

def GetSymbol(d):
    return str(d)

def AddDigit(n1,n2,p):
    Tsum=n1+n2+p
    p=Tsum//10
    n=Tsum%10
    return p, n

def AddColumn(S1, S2):

    sign1 = ""
    if S1 and S1[0] in ['+', '-']:
        sign1 = S1[0]
        S1 = S1[1:]
        
    sign2 = ""
    if S2 and S2[0] in ['+', '-']:
        sign2 = S2[0]
        S2 = S2[1:]

    if (sign1 == "-" and sign2 != "-") or (sign1 != "-" and sign2 == "-"):
        return "Помилка: Програма виконує додавання стовпчиком. Для чисел із різними знаками потрібен алгоритм віднімання."

    if "." in S1:
        int1, frac1 = S1.split(".")
    else:
        int1, frac1 = S1, ""
        
    if "." in S2:
        int2, frac2 = S2.split(".")
    else:
        int2, frac2 = S2, ""

    max_int = max(len(int1), len(int2))
    max_frac = max(len(frac1), len(frac2))

    int1 = int1.zfill(max_int)
    int2 = int2.zfill(max_int)

    if max_frac > 0:
        frac1 = frac1 + "0" * (max_frac - len(frac1))
        frac2 = frac2 + "0" * (max_frac - len(frac2))
        S1_aligned = int1 + "." + frac1
        S2_aligned = int2 + "." + frac2
    else:
        S1_aligned = int1
        S2_aligned = int2

    S = ""
    p = 0
    
    for i in range(len(S1_aligned) - 1, -1, -1):
        char1 = S1_aligned[i]
        char2 = S2_aligned[i]
        
        d1 = GetDigit(char1)
        d2 = GetDigit(char2)
        
        if d1 == -1 or d2 == -1:
            S = char1 + S
        else:
            p, n = AddDigit(d1, d2, p)
    
            S = GetSymbol(n) + S
            
    if p > 0:
        S = GetSymbol(p) + S
        
    if sign1 == sign2 and sign1 != "":
        S = sign1 + S
        
    return S


print("--- Програма: Додавання чисел у стовпчик ---")
print("Підтримуються цілі та дробові числа, а також однакові знаки (+ або -).")

num1_str = input("Введіть перше число (S1): ").strip()
num2_str = input("Введіть друге число (S2): ").strip()

result_str = AddColumn(num1_str, num2_str)

print(f"Результат додавання: {result_str}")