import random
squares=[]
for i in range(0,10):
    value=random.randint(1,100)
    squares.append(value**2)
    print(squares[i],end=" ")

