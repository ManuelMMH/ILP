import math

x1= int(input("X1 position: "))
y1= int(input("Y1 position: "))
x2= int(input("X2 position: "))
y2= int(input("Y2 position: "))

def distance (x1,y1,x2,y2):
    h=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return h

print("The distance between (",x1,",",y1,") and (",x2,",",y2,") is:","%.2f"%distance(x1,y1,x2,y2))

