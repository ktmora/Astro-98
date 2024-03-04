x = 2
y = 8
def pwr(x,y):
    p = 1
    if (y == 0):
        return 1
    elif (y == 1):
        return x
    elif (y > 0):
        while y > 0:
            p = p * x 
            y -= 1
        return p
    elif (y < 0):
        y = -y
        while y > 0:
            p = p * x
            y -= 1
    return 1/p
print(pwr(x,y))
#I understand why there is a built in function for this...pain
#tested -2, -3, -4, 0, 8
