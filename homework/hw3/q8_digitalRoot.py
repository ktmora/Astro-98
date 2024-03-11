#homework 3 question 8 : Digital Root

y = 2319

def digitalRoot(x) : 
    myList = [int(i) for i in str(y) ]
    s = sum(myList)
    return s
print(digitalRoot(y))

#Return : 15
#Had to look up how to use the sum command here : https://www.geeksforgeeks.org/sum-function-python/
#And also had to look up how to turn an integer/string into a list here : https://stackoverflow.com/questions/13905936/converting-integer-to-digit-list
#Rest of the code in the function is mine :)