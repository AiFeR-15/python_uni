count = 0
for i in range(ord('A'), ord('X')+1):
    big=chr(i)
    small=chr(i+32)
    print(f"{big}{small}", end=" ")
    count=count+1
    if(count%8==0):
        print("")