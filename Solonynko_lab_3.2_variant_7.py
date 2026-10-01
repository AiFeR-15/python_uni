import random
flag=0
a_vector=[]
b_vector=[]
sum_vector=[]
while(flag==0):
    n=int(input("Введіть розмірність векторів (n<101):"))
    if(n>0 and n<=100):
        flag=1
for i in range(n):
    a_vector.append(random.uniform(-100.0,100.0))
    b_vector.append(random.uniform(-100.0,100.0))
    sum_vector.append(a_vector[i]+b_vector[i])
print(f"Координати вектора а:\n{a_vector}")
print(f"Координати вектора b:\n{b_vector}")
print(f"Сума двох векторів:\n{sum_vector}")
