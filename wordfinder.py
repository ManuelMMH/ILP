def finder (word):
    f = open("test.txt")
    text = f.read()
    list = text.split(" ")
    count = 0

    for n in list:
        ## print (n) Allows to see location of words.
        if(n.lower()==word):
            count+= 1
    return count

word = input("Type the word you are looking for: ")
print ("Times found: ",finder(word))