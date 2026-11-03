try:
    string=input("Введіть рядок з цифрами та буквами: ")
    assert len(string)>0, "Помилка: введно порожній рядок!"

    sum=0
    count=0

    for i in string:
        try:
            digit=int(i)
            sum+=digit
            count+=1
        except ValueError:
            pass
    assert count>0, "Помилка: введено рядок без цифр!"

    print(f"Знайдено цифр: {count}")
    print(f"Сума цифр рядка: {sum}")

except AssertionError as error_msg:
    print(error_msg)
