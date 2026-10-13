import math
a = float(input("Введіть число а:"))
b = float(input("Введіть число b:"))

numerator = 11.21 * (1+math.log(b/a))
denominator = 1-math.sin(a/b*math.pi) * math.cos(a/b * math.pi)

y =(numerator / denominator)**(2/3)
print (f"Результат y={y:.4f}")
