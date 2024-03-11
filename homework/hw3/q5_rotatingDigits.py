#homework 3 question 5 : rotating digits

n = 12345

def rotateDigits( n ) : 
    mod = n % 10
    #print(mod)
    floor = n // 10
    #print(floor)
    for i in range(1,5) :
       n =  5 * (10**i)
    rotate = n + floor

    return rotate

print ( rotateDigits( n ) )

#Return = 51234
