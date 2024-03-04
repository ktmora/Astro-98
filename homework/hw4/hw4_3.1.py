#homework 4 question 3.1
# i = row
# j = column

outer = []

for i in range(5) :
    row = i
    inner = []
    for j in range(1,6):
        inner.append(row*5+j)
    outer.append(inner)
print(outer)

#output: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#play around with print statements to understand what exactly the code is doing 

#Error said cannot have a list in the range() function, so removed the range and used "for i in list1 : ". Fixed the error but now returning "None"
#TypeError: 'int' object is not iterable, took out len() command to fix this