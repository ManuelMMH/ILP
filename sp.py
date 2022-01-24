def superpower (b,p):
    c=1
    num=b
    while(c<p):
        num=num*b
        c=c+1
    return num
b= int(input("Base: "))
p= int(input("Power: "))

print(superpower(b,p))