import random
temp_list_1=[]
temp_list_2=[]
for i in range(10):
    temp_list_1.append(int(random.random()*6))
tuple_1=tuple(temp_list_1)
for i in range(10):
    temp_list_2.append(int(random.random()*6)-5)
tuple_2=tuple(temp_list_2)
tuple_3=tuple_1+tuple_2
print("Кортеж №1:")
print(tuple_1)
print("Кортеж №2:")
print(tuple_2)
print("Кортеж №3(№1 + №2):")
print(tuple_3)
print("К-сть нулів у кортежі №3:")
print(tuple_3.count(0))

