seasons = {
    "Зима": ("Грудень", "Січень", "Лютий"),
    "Весна": ("Березень", "Квітень", "Травень"),
    "Літо": ("Червень", "Липень", "Серпень"),
    "Осінь": ("Вересень", "Жовтень", "Листопад")
}

all_months = ["Січень", "Лютий",
              "Березень", "Квітень", "Травень",
              "Червень", "Липень", "Серпень",
              "Вересень", "Жовтень", "Листопад",
              "Грудень"]

rainfall={}
for i in range(len(all_months)):
    num=1+i
    month=all_months[i]
    while True:
        try:
            val= int(input(f"Опади '{month}; №{num} мм: "))
            if val>-1:
                break
            else:
                print("Помилка: значенння опадів не може бути від'ємне!")
        except ValueError:
            print("Помилка: введіть значення заново!")
    rainfall[num]=val
        
season_totals={}
min_fall=-1
dry_seasons=[]

for season ,months in seasons.items():
    total=0
    for month in months:
        month_num = all_months.index(month)+1
        total+=rainfall[month_num]
    season_totals[season]=total
    print(f"Сума опадів за {season}: {total} мм")
    
    if min_fall == -1 or total<min_fall:
        min_fall=total
        dry_seasons=[season]
    elif min_fall == total:
        min_fall=total
        dry_seasons.append(season)
print("Найсухіша(і) пора(и) року:")
for s in dry_seasons:
    print(f"{s}: {min_fall} мм")
        
