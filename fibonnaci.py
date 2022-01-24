n=int(input("Type a number: "))

def fibonnaci (n):
    x = 0
    y = 1
    z = 0

    for a in range (n-1):
        z = x + y
        x = y
        y = z
        print (z)
    return

fibonnaci (n)