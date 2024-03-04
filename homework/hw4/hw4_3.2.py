#homework 4 question 3.2

#copy and pasted my code from q 3.1:

outer = []

for i in range(5) :
    row = i
    inner = []
    for j in range(1,6) :
        inner.append(row*5+j)
    outer.append(inner)
#print(outer) gives output:
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]] 


for k in range(len(outer)):
    for l in range(len(inner)):
        if outer[k][l] % 3 == 0 :
            outer[k][l] = '?'
print(outer)

#ouput: [[1, 2, '?', 4, 5], ['?', 7, 8, '?', 10], [11, '?', 13, 14, '?'], [16, 17, '?', 19, 20], ['?', 22, 23, '?', 25]]
#outer[k][l] acts as an x,y coordinate for moving through the 2D listo lists
# used https://datagy.io/python-replace-item-in-list/ for code "for k in range(len(list)):"
#for k in range(len(list)): essentially says that for every index, k, in the range of the list, then do the code afterwards.
#the len() statement is because the range() statement doesn't like lists, so len() allows for a number to be assigned to each value in the list
#in short, len() allows for the range() to read a list as a range of numbers
#Debugging error: I kept running into error that said I could not use the statement 'if outer[k] % 3 == 0' because outer[k] was registering as the rows, not the individual #s
#fixed by doing a for loop inside a for loop; previous issue was that I was trying to mod a whole list instead of actual values. initial for loop is to get into the rows (outer),
#second for loop allows me to get into the rows and the individual values (inner), which can then be modded and the rest of the code works :)
#Also, for the initial part I was struggling with a similar concept while writing the code, but it was fixed in OH by writing a for loop inside a for loop. 