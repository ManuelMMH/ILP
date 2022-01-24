def figure ():
    size = int(input("Give me the size: "))
    s = " "

    for n in range (size):
        s = s + "T"
        print (s)

    for n in range (size):
        s = s[:-1]
        print (s)

figure()