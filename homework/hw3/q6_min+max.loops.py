#homework 3 question 6 : minimum and maximum (loop edition)

myList = [ 0, 4, 6, -2, -13, 4, 32 ]

#for loop for min
def minfl(x) :
    i = myList[0]
    for a in myList :
        if a < i : 
            i = a
    return i, 'is the minimum'

print (minfl(myList))
#Result : (-13, 'is the minimum')

#for loop for max
def maxfl(x) :
    i = myList[0]
    for a in myList :
        if a > i :
            i = a
    return i, 'is the maximum'
print(maxfl(myList))
#Result : (32, 'is the maximum')

myList = [ 0, 4, 6, -2, -13, 4, 32 ]

#while loop for min
def minw(x) : #ans = i , a = i
    i = myList[0]
    a = 0
    while a < len(myList) :
        if myList[a] < i :
            i = myList[a] 
        a += 1
    return i, 'is the minimum'
print(minw(myList))
#Used code format from StackOverflow : https://stackoverflow.com/questions/44202304/how-to-find-minimum-value-from-a-list-using-while-loop-at-the-same-time-not-usin
#Code above explained : The while statement runs for any a within the values of myList, and within that length I compare the value of an index [a] in myList to i, which
#is a set to index through myList. Thus, a will be compared to every value of my list, which is what I want to happen so that I can find the min. 
#So if the index of a, [0], is less than i, any value in myList, then i will be set to myList[a], and the while loop will keep running until there are no new myList[a] < i. 
#Since it runs until there is no new i, it has compared all values and the last value that was set to i is then the minimum, which is why the return statement is i and not a.
#The a += 1 is the condition that allows for the while loop to stop after all values of myList have been indexxed through. 
#Result : (-13, 'is the minimum')

#while loop for max
def maxw(x) :
    i = myList[0]
    a = 0
    while a < len(myList) : 
        if myList[a] > i :
            i = myList[a] 
        a += 1
    return i, 'is the maximum'
print(maxw(myList))
#Just used same code format as above 
#Result : (32, 'is the minimum')