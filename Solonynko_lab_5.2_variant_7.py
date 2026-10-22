import re
pattern= "^[A-Z]{2}[0-9]{4}[A-Z]{2}$"
cars={}
unique_plates = set()
flag=True
while True:
    n=int(input("Введіть кількість автомобілів: "))
    if n>0:
        break
    else:
        print("Помилка: введіть коректну к-сть автомобілів!")
for i in range(n):
    print(f"Авто №{i + 1}")
    while True:
        plate=input("Введіть унікальний номер авто: ")
        if not re.fullmatch(pattern,plate):
            print("Помилка: номер має складатися з 2 великих літер, 4 цифр і 2 великих літер!")
        elif plate in unique_plates:
            print("Помилка: авто з таким номером вже існує в базі! Введіть інший номер.")
        else:
            unique_plates.add(plate)
            break
    mark=input("Введіть марку: ")
    owner=input("Введіть прізвище власника: ")

    cars[plate]={
        "mark":mark,
        "owner":owner}
print("\n=== СПИСОК АВТОМОБІЛІВ ===")
for plate, info in cars.items():
    print(f"Номер: {plate} | Марка: {info['mark']} | Власник: {info['owner']}")
    
found_mark=input("Введіть марку автомобілів: ")
count=0
for info in cars.values():
    if info["mark"].lower().strip()==found_mark.lower().strip():
        count +=1
print(f"Кількість автомобілів марки '{found_mark}':{count}")
