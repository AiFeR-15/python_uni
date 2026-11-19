def add_book(filename):
    """Додає відомості про нову книжку у файл (створює файл, якщо його немає)."""
    author = input("Введіть прізвище автора: ").strip()
    title = input("Введіть назву книжки: ").strip()
    year = input("Введіть рік видання: ").strip()

    if not author or not title or not year:
        print("Помилка: Усі поля (автор, назва, рік) мають бути заповнені!")
        return

    if ';' in author or ';' in title:
        print("Помилка: Не використовуйте символ ';' у тексті.")
        return

    if not year.isdigit():
        print("Помилка: Рік видання має складатися лише з цифр.")
        return

    # Режим 'a' (append) створює файл, якщо його ще немає, 
    # або додає новий рядок у кінець існуючого файлу
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{author};{title};{year}\n")
    
    print(f"Книжку «{title}» успішно збережено у файл '{filename}'!")


def search_books_by_title(filename, search_title):
    """Шукає книжки із заданою назвою та виводить авторів і рік видання."""
    with open(filename, 'r', encoding='utf-8') as f:
        found = False
        print("-" * 45)
        
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue

            try:
                author, title, year = clean_line.split(';')
            except ValueError:
                # Пропускаємо рядок, якщо він записаний у неправильному форматі
                continue

            if title.strip().lower() == search_title.strip().lower():
                print(f"Автор: {author.strip()} | Рік видання: {year.strip()}")
                found = True

        if not found:
            print(f"Книжок із назвою «{search_title}» у файлі не знайдено.")
        print("-" * 45)


def main():
    filename = input("Введіть назву файлу для роботи (наприклад, books.txt): ").strip()
    if not filename:
        filename = "books.txt"
    elif not filename.endswith(".txt"):
        filename += ".txt"

    while True:
        print(f"\n=== БІБЛІОТЕКА (Файл: {filename}) ===")
        print("1. Додати книжку до файлу")
        print("2. Знайти книжку за назвою")
        print("0. Вихід")

        choice = input("Оберіть дію: ").strip()

        if choice == '1':
            add_book(filename)

        elif choice == '2':
            search_title = input("Введіть назву книжки для пошуку: ").strip()
            if not search_title:
                print("Помилка: Назва для пошуку не може бути порожньою.")
                continue

            try:
                search_books_by_title(filename, search_title)
            except FileNotFoundError:
                print(f"Помилка: Файл '{filename}' ще не створено. Спочатку додайте хоча б одну книжку (пункт 1).")

        elif choice == '0':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Введіть 1, 2 або 0.")


if __name__ == "__main__":
    main()