import random
squares=[]
lis=[]
flag=0
count=0
print("Виберіть спосіб створення списка(натуральних чисел):")
print("1. Введення з клавіатури")
print("2. Згенерувати список")
while(flag==0):
    way=int(input("Введіть номер способу: "))
    if(way>0 and way<3):
        flag=1
    else:
        print("Будь ласка, введіть 1 або 2.")
match way:
    case 1:
        for i in range(0,10):
            flag=0
            while(flag==0):
                try:
                    value_0=int(input(f"Введіть значення елемента списка №{i+1}: "))
                    if(value_0 > 0):
                        flag=1
                    else:
                        print("Число має бути натуральним (більшим за 0)!")
                except ValueError:
                    print("Помилка! Ви ввели не ціле число. Спробуйте ще раз.")
            squares.append(value_0)
    case 2:
        for i in range(0,10):
            value=random.randint(1,100)
            squares.append(value)
print("Створений список:")
for i in range(0,10):
    print(squares[i],end=" ")
    if (squares[i] ** 0.5) % 1 == 0:
        lis.append(squares[i])
        count=count+1
print()
print("Список у якому всі елементи є повними квадратами: ")
for i in range(0,count):
    print(lis[i],   end=" ")

