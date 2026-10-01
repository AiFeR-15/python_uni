import random
M=[]
flag=0
count=0
while(flag==0):
    n=int(input("Введіть розмірність векторів (n=<100):"))
    if(n>0 and n<=100):
        flag=1
flag=0
while(flag==0):
    m=int(input("Введіть розмірність векторів (m=<200):"))
    if(m>0 and m<=200):
        flag=1
for row in range(n):
    new_row=[]
    for elem in range(m):
        new_row.append(round(random.uniform(-10,10),2))
    M.append(new_row)

print(f"Матриця({n}*{m})")
for row in range(n):
    for elem in range(m):
        print(f"{M[row][elem]:6.2f}", end=" ")
    print()
un_elem=set()
for row in range(n):
    for elem in range(m):
        un_elem.add(M[row][elem])
print(f"К-сть всіх різних елементів матриці{len(un_elem)}")


        
