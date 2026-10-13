import math
x = float(input("Введіть дійсне число x:"))
a = float(input("Введіть дійсне число a:"))
E = float(input("Введіть дійсне число E:"))

x_k=x
a_k=a
sum=0
factorial=1
k=1
cos_x_k=math.cos(x_k)
sin_a_k=math.sin(a_k)
numerator=cos_x_k + sin_a_k
add=(numerator/factorial)

while abs(add) >= E:
    
    sum+=add
    print (f"Сума {k} доданків = {sum}")
    k+=1
    factorial=1
    x_k=1
    a_k=1

    for i in range(1,k+1):
        x_k = x_k * x
    
    for i in range(1,k+1):
        a_k = a_k * a

    cos_x_k=math.cos(x_k)
    sin_a_k=math.sin(a_k)

    numerator=cos_x_k + sin_a_k

    n=2*k-1
    for i in range(2,n+1):
        factorial=factorial * i
    add=(numerator/factorial)


print (f"Результат sum={sum:.4f}")
print (f"К-сть доданків={k-1}")
