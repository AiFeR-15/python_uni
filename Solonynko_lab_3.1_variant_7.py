import random
squares=[]
flag=0
print("Виберіть спосіб створення списка(натуральних чисел):")
print("1. Введення з клавіатури")
print("2. Згенерувати список")
while(flag==0):
    way=int(input("Введіть номер способу: "))
    if(way>0 and way<3):
        flag=1
match way:
    case 1:
        for i in range(0,10):
            flag=0
            while(flag==0):
                value_0=int(input(f"Введіть значення елемента списка №{i+1}: "))
                if(value_0 > 0):
                    flag=1
            squares.append(value_0**2)
    case 2:
        for i in range(0,10):
            value=random.randint(1,100)
            squares.append(value**2)
for i in range(0,10):
    print(squares[i],end=" ")

