text=input("Введіть будь ласка ваше речення: ")
total_sum=0
for char in text:
    if(char.isdigit()):
        total_sum += int(char)
print("Сума цифр що входять до рядка:")
print(f"{text}")
print(f"Дорівнює: {total_sum}")
