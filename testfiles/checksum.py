import math
x= input("Enter x: ")


def checksum(): 
    
    x1 = float(x)/256
    y1 = math.floor(float(x1))
    z = y1 * 256
    print( float(x) - float(z))

checksum()