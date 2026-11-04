count_R=0
count_T=0
count_V=0
lin=[]
while True:
    x=input("Введіть послідовність цілих чисел('досить' зупиняє послідовність)")
    if x.lower().strip()=="досить":
        break
    try:
        val=int(x)
        if val>9:
            raise RuntimeError
        elif val<0:
            raise TypeError
        elif 0<= val <=9:
            raise ValueError
    except RuntimeError:
        count_R+=1
    except TypeError:
        count_T+=1
    except ValueError:
        count_V+=1

print(f"R={count_R}")
print(f"T={count_T}")
print(f"V={count_V}")