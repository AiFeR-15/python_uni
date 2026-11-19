def add_toy(filename):
    """Додає відомості про нову іграшку у файл."""
    name = input("Введіть назву іграшки: ").strip()
    price_str = input("Введіть вартість у грн: ").strip()
    min_age_str = input("Введіть мінімальний вік (років): ").strip()
    max_age_str = input("Введіть максимальний вік (років): ").strip()

    if not name or not price_str or not min_age_str or not max_age_str:
        print("Помилка: Усі поля мають бути заповнені!")
        return

    if ';' in name:
        print("Помилка: Не використовуйте символ ';' у назві.")
        return

    try:
        price = float(price_str)
        min_age = int(min_age_str)
        max_age = int(max_age_str)
        if price < 0 or min_age < 0 or max_age < min_age:
            print("Помилка: Перевірте коректність ціни та вікових меж.")
            return
    except ValueError:
        print("Помилка: Ціна та вік мають бути числами.")
        return

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{name};{price};{min_age};{max_age}\n")

    print(f"Іграшку «{name}» успішно додано до файлу '{filename}'!")


def search_constructor(filename):
    """Шукає конструктор ціною 2200 грн для дітей 5-10 років.
    Якщо не знайдено — дописує повідомлення про відсутність у цей же файл.
    """
    found = False
    print("-" * 55)

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue

            # Обгортка пропускає текстові повідомлення про відсутність або биті рядки
            try:
                name, price_str, min_age_str, max_age_str = clean_line.split(';')
                price = float(price_str)
                min_age = int(min_age_str)
                max_age = int(max_age_str)
            except ValueError:
                continue

            # Перевірка трьох умов варіанту g
            if (
                "конструктор" in name.lower()
                and price == 2200
                and min_age == 5
                and max_age == 10
            ):
                print(f"Знайдено: {name.strip()} | Ціна: {price} грн | Вік: від {min_age} до {max_age} років")
                found = True

    if not found:
        absence_msg = "Відомості: Конструктор ціною 2200 грн для дітей від 5 до 10 років відсутній."
        print("Такої іграшки не знайдено. Записуємо відомості про відсутність у файл...")
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(absence_msg + "\n")

    print("-" * 55)


def main():
    filename = input("Введіть назву файлу для роботи (наприклад, toys.txt): ").strip()
    if not filename:
        filename = "toys.txt"
    elif not filename.endswith(".txt"):
        filename += ".txt"

    while True:
        print(f"\n=== МАГАЗИН ІГРАШОК (Файл: {filename}) ===")
        print("1. Додати іграшку до файлу")
        print("2. Знайти конструктор (2200 грн, вік 5-10 років)")
        print("0. Вихід")

        choice = input("Оберіть дію: ").strip()

        if choice == '1':
            add_toy(filename)

        elif choice == '2':
            try:
                search_constructor(filename)
            except FileNotFoundError:
                print(f"Помилка: Файл '{filename}' не знайдено. Спочатку додайте іграшки (пункт 1).")

        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()