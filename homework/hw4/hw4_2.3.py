#homework 4 question 2.3

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def listC(listA, listB): 
    Aodd = [i for i in listA if i % 2 != 0]
    Bodd = [i for i in listB if i % 2 != 0]
    listC = Aodd + Bodd
    listC.sort()
    return listC

print(listC(listA, listB))


#found the list.sort() command at: https://www.w3schools.com/python/python_lists_sort.asp
#otherwise all the code above was created by yours truly
#Output : [1, 3, 5, 7, 9 , 21, 23, 25, 27, 29]
#no errors! :)