def create_text_file():
    """Створює новий текстовий файл із кількома рядками тексту."""
    filename = input("Введіть назву нового файлу (наприклад, text.txt): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    print("Вводьте рядки тексту (щоб завершити ввід, натисніть Enter на порожньому рядку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line + "\n")

    if not lines:
        print("Помилка: Файл має містити принаймні один непорожній рядок!")
        return

    try:
        with open(filename, 'x', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"Файл '{filename}' успішно створено!")
    except FileExistsError:
        print(f"Помилка: Файл '{filename}' вже існує! Оберіть іншу назву.")


def print_short_lines(filename):
    """Виводить усі рядки файлу, що містять менше 40 символів."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = 0  # Лічильник знайдених рядків
    print("-" * 40)
    
    for line in lines:
        clean_line = line.rstrip('\n')
        # Перевірка обов'язково всередині циклу (з відступом)
        if len(clean_line) < 40:
            print(f"[{len(clean_line)} симв.]: {clean_line}")
            count += 1

    print("-" * 40)
    if count == 0:
        print("Рядків, які містять менше 40 символів, не знайдено.")
    else:
        print(f"Усього знайдено рядків: {count}")


def main():
    while True:
        print("\n=== МЕНЮ (Завдання 2, Варіант g) ===")
        print("1. Створити текстовий файл")
        print("2. Вивести рядки (< 40 символів) з існуючого файлу")
        print("0. Вихід")

        choice = input("Оберіть дію: ").strip()

        if choice == '1':
            create_text_file()

        elif choice == '2':
            filename = input("Введіть назву файлу (наприклад, text.txt): ").strip()
            if not filename.endswith(".txt"):
                filename += ".txt"

            try:
                print_short_lines(filename)
            except FileNotFoundError:
                print(f"Помилка: Файл '{filename}' не знайдено.")

        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()