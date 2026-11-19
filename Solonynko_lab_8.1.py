def create_file():
    """Створює новий текстовий файл із послідовністю дійсних чисел."""
    filename = input("Введіть назву нового файлу (наприклад, data.txt): ").strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    raw_data = input("Введіть дійсні числа через пробіл: ").strip()
    parts = raw_data.split()

    if not parts:
        print("Помилка: Послідовність не може бути порожньою!")
        return

    # Перевіряємо, чи всі введені дані дійсно є числами перед записом у файл
    try:
        [float(item) for item in parts]
    except ValueError:
        print("Помилка: Усі елементи мають бути дійсними числами (дробові пишуться через крапку).")
        return

    try:
        # Режим 'x' гарантує, що ми не перезапишемо вже існуючий файл
        with open(filename, 'x', encoding='utf-8') as f:
            f.write(" ".join(parts))
        print(f"Файл '{filename}' успішно створено та збережено!")
    except FileExistsError:
        print(f"Помилка: Файл '{filename}' вже існує! Виберіть іншу назву.")


def calc_first_last_diff(filename):
    """Обчислює різницю першої та останньої компоненти текстового файлу."""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    parts = text.split()
    if not parts:
        raise ValueError("Файл порожній, у ньому немає чисел.")

    numbers = [float(x) for x in parts]
    
    # Повертаємо різницю: перше число (індекс 0) мінус останнє (індекс -1)
    return numbers[0] - numbers[-1], numbers[0], numbers[-1]


def main():
    while True:
        print("\n=== МЕНЮ (Лабораторна №8, Варіант g) ===")
        print("1. Створити новий файл із числами")
        print("2. Відкрити існуючий файл та обчислити різницю")
        print("0. Вихід")

        choice = input("Оберіть дію: ").strip()

        if choice == '1':
            create_file()

        elif choice == '2':
            filename = input("Введіть назву файлу для читання (наприклад, data.txt): ").strip()
            if not filename.endswith(".txt"):
                filename += ".txt"

            try:
                diff, first_num, last_num = calc_first_last_diff(filename)
                print("-" * 40)
                print(f"Перша компонента   : {first_num}")
                print(f"Остання компонента : {last_num}")
                print(f"Різниця (1-ша - ост.): {diff}")
                print("-" * 40)
            except FileNotFoundError:
                print(f"Помилка: Файл '{filename}' не знайдено. Спочатку створіть його (пункт 1).")
            except ValueError as err:
                print(f"Помилка даних у файлі: {err}")

        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()