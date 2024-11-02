print("Half pyramid pattern")

r = int(input("ENTER THE NO. OF ROWS: "))

for i in range(r):
    for j in range(i+1):
        print("*",end=' ')
    print()