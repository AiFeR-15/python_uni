x = int(input("Введіть число x:"))
y = float(input("Введіть число y:"))

xy=x**2 - y**2
diff=x-y

if x<y:
    max_1=x
else:
    max_1=y
    
if diff>y:
    max_2=diff
else:
    max_2=y
    
if max_1 > max_2:
    if max_1 > xy:
        f=max_1
    else:
        f=xy
else:
    if max_2 > xy:
        f=max_2
    else:
        f=xy

print (f"Значення функції f={f}")
