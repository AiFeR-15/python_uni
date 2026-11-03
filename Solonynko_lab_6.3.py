count_R=0
count_T=0
count_V=0
lin=[]
while True:
    try:
        x=input("Введіть послідовність цілих чисел('досить' зупиняє послідовність)")
        if x.lower().strip()!="досить":
            lin.append(x)
        else:
            break
        for i in lin:
            val=int(i)
            if val>9:
                raise RuntimeError
                break
            elif val<0:
                raise TypeError
                break
            elif val>=0 and val<=9:
                raise ValueError
                break
    except RuntimeError:
        count_R+=1
        pass
    except TypeError:
        count_T+=1
        pass
    except ValueError:
        count_V+=1
        pass

print(f"R={count_R}")
print(f"T={count_T}")
print(f"V={count_V}")