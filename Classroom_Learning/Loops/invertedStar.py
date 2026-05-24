#Print an invrete full  pyramid stars decrease each row, centres with spaces
rows = int(input("Rows: "))
for i in range(rows,0,-1):
    stars = 2 * i -1
    spaces = rows-i
    print (" "* spaces,"*"*stars)