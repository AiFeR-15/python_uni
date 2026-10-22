import math
numbers=[]
counts={}
flag=0
while True:
    n= int(input("Введіть к-сть чисел послідовності: "))
    if n>0:
        break
    print("Помилка! n має бути більшим за нуль.")
for i in range(n):
       date=int(input(f"№{i+1}: "))
       numbers.append(date)
for num in numbers:
    if num in counts:
        counts[num]+=1
    else:
        counts[num]=1
for key, value in counts.items():
    if value > 1:
        flag=1
        break 

    if key<=1:
        flag=1
        break
    
    if key%2==0 and key !=2:
        flag=1
        break
    
    sqrt=math.isqrt(key)
    
    for j in range(3,sqrt+1,2):
        if key%j==0:
            flag=1
            break
        
    if flag==1:
        break
if flag==0:
    print("Правда: всі задані числа є простими й різними!")
else:
    print("Неправда: числа не є повністю простими або унікальними.")
    
            
        
